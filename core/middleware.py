from django.conf import settings
from django.shortcuts import redirect


class AccessGuardMiddleware:
    """访问码门禁：未通过验证的访客只能访问访问码页面"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not getattr(settings, 'ENABLE_ACCESS_GUARD', True):
            return self.get_response(request)

        path = request.path
        allowed = (
            path.startswith('/static/')
            or path.startswith('/admin/')
            or path == '/access/'
            or request.session.get('access_granted')
        )
        if not allowed:
            return redirect('/access/')
        return self.get_response(request)
