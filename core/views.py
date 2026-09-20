import json

from pathlib import Path

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Contract

BASE_DIR = Path(__file__).resolve().parent.parent


# 前台首页数据接口，供 Vue 前端调用
def api_home(request):
    return JsonResponse({
        'project': '小李外贸',
        'message': 'Django API 运行正常',
        'server_time': timezone.localtime().strftime('%Y-%m-%d %H:%M:%S'),
    })


# 前台入口：直接返回 Vue 构建后的 index.html
def frontend_index(request):
    index_file = BASE_DIR / 'frontend' / 'dist' / 'index.html'
    if index_file.exists():
        return HttpResponse(index_file.read_text(encoding='utf-8'), content_type='text/html; charset=utf-8')
    return JsonResponse({'message': '前端尚未构建，请先在 frontend 目录运行 npm run build'}, status=503)


# 访问码验证页面
def access_page(request):
    error = False
    if request.method == 'POST':
        code = request.POST.get('code', '')
        if code == settings.ACCESS_CODE:
            request.session['access_granted'] = True
            return redirect('/')
        error = True
    return render(request, 'access.html', {'error': error})


# 联系表单序列化辅助
def serialize_contract(contract):
    return {
        'id': contract.pk,
        'contact_name': contract.contact_name,
        'contact_phone': contract.contact_phone,
        'company': contract.company,
        'project_type': contract.project_type,
        'quantity': contract.quantity,
        'delivery_city': contract.delivery_city,
        'budget': contract.budget,
        'requirement': contract.requirement,
        'created_at': contract.created_at.strftime('%Y-%m-%d %H:%M:%S'),
    }


def parse_body(request):
    try:
        return json.loads(request.body or '{}')
    except json.JSONDecodeError:
        return None


# 联系表单集合接口：GET 查询列表，POST 新增记录
@csrf_exempt
def contract_list(request):
    if request.method == 'GET':
        contracts = Contract.objects.all().order_by('-created_at')
        return JsonResponse({
            'count': contracts.count(),
            'results': [serialize_contract(item) for item in contracts],
        })

    if request.method == 'POST':
        data = parse_body(request)
        if data is None:
            return JsonResponse({'error': '请求数据格式错误'}, status=400)

        required = ['contact_name', 'contact_phone', 'project_type', 'quantity', 'delivery_city', 'budget', 'requirement']
        missing = [field for field in required if not data.get(field)]
        if missing:
            return JsonResponse({'error': '缺少必填字段', 'fields': missing}, status=400)

        contract = Contract.objects.create(
            contact_name=data['contact_name'],
            contact_phone=data['contact_phone'],
            company=data.get('company', ''),
            project_type=data['project_type'],
            quantity=data['quantity'],
            delivery_city=data['delivery_city'],
            budget=data['budget'],
            requirement=data['requirement'],
        )
        return JsonResponse({'message': '提交成功', 'data': serialize_contract(contract)}, status=201)

    return JsonResponse({'error': '不支持的请求方法'}, status=405)


# 联系表单单条接口：GET 详情，PATCH 更新，DELETE 删除
@csrf_exempt
def contract_detail(request, pk):
    try:
        contract = Contract.objects.get(pk=pk)
    except Contract.DoesNotExist:
        return JsonResponse({'error': '记录不存在'}, status=404)

    if request.method == 'GET':
        return JsonResponse({'data': serialize_contract(contract)})

    if request.method == 'PATCH':
        data = parse_body(request)
        if data is None:
            return JsonResponse({'error': '请求数据格式错误'}, status=400)

        fields = ['contact_name', 'contact_phone', 'company', 'project_type', 'quantity', 'delivery_city', 'budget', 'requirement']
        for field in fields:
            if field in data:
                setattr(contract, field, data[field])
        contract.save()
        return JsonResponse({'message': '更新成功', 'data': serialize_contract(contract)})

    if request.method == 'DELETE':
        contract.delete()
        return JsonResponse({'message': '删除成功'})

    return JsonResponse({'error': '不支持的请求方法'}, status=405)
