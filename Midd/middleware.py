# from django.utils.deprecation import MiddlewareMixin        ##django新版本不支持这种导入方式

##推荐如下方式，将中间件写在自己的文件中↓↓
from django.shortcuts import render,HttpResponse,redirect


class MiddlewareMixin(object):      ##此处的代码是从如上导入的MiddlewareMixin 使用ctrl+鼠标左键打开黏贴过来的
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

white_list=['/login/', '/register/']        ##不需要验证是否登录即可访问！！

class MiddleDemo1(MiddlewareMixin):
    def process_request(self, request):
        print("demo1_process_request")
        # return HttpResponse("Python...666")
        print(request.META.get('PATH_INFO'))
        print(request.META)
        if not request.META.get('PATH_INFO') in white_list:
            if not request.session.get('IS_LOGIN'):
                return redirect('/login/')

    def process_response(self, request, response):
        print("demo1_process_response")
        return response      ##为什么需要返回response呢？ 是因为后端view处理完成返回给用户的时候是直接走的最近的一个中间件的process_response

# class MiddleDemo2(MiddlewareMixin):
#     def process_request(self, request):
#         print("demo2_process_request")
#
#     def process_response(self, request, response):
#         print("demo2_process_response")
#         return response