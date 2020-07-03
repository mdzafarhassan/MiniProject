import re
from django.conf import settings
from django.shortcuts import redirect
from django.utils.http import is_safe_url

REQUIRED_URL = [re.compile(url) for url in settings.LOGIN_REQUIRED_URL]


class BasicMiddleware:
    def __init__(self, get_response):
        print("===========================================================\n")
        print("          custom_middleware > BasicMiddleware\n")
        print("===========================================================\n")

        self.get_response = get_response

    def __call__(self, get_response):
        response = self.get_response(get_response)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user'), "BasicMiddleWare  >>  process_view"

        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')

            if any(m.match(path) for m in REQUIRED_URL):
                redirect_to = settings.LOGIN_URL
                if len(path) > 0 and is_safe_url(
                        url=request.path_info, allowed_hosts=request.get_host()):
                    redirect_to = f"{settings.LOGIN_URL}?next={request.path_info}"
                return redirect(redirect_to)


'''
#
#
#
#
# def process_request(self, request):
#     raise Exception
#     pass

# def process_exception(self, request, exception):
#     print("BasicMiddleware > process_exception")
#     # print('process_exception')

# def process_template_response(self, request, response):
#     # print('process_template_response')
#     pass
'''
