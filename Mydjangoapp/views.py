from django.shortcuts import render, HttpResponse, redirect
from Mydjangoapp import models
from django import forms
#from Mydjangoapp.models import UserInfo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


##登录##
def login(request):
    error_msg = ""
    obj_item = models.AdmDat.objects.all()
    userList = models.UserInfo.objects.all()
    if request.method=='POST':
        username11=request.POST.get('user').lower()
        password11=request.POST.get('pwd')
        try:
            chk_pwd = models.UserInfo.objects.get(username=username11)
        except:
                message = "用户名不存在！"
                return render(request, 'login.html', locals())
        else:
            if password11 == chk_pwd.password:
                request.session['IS_LOGIN'] = True
                request.session['USERNAME'] = username11
                # print(request.session['IS_LOGIN'])
                # print(request.session['USERNAME'])
                # return redirect('/adtm/')
                obj_list = models.AdmDat.objects.all()
                return render(request, 'main.html', locals())
            else:
                message = "密码错误！"
                return render(request,'login.html', locals())
    else:
        return render(request, 'login.html', locals())


###通过session判断用户是否登陆### （改为 “中间件” 模式）
# def chk_session(func):
#     def warpper(request, *args, **kwargs):
#         if request.session.get('IS_LOGIN', False):
#             return func(request, *args, **kwargs)
#         else:
#             return redirect('/login/')
#     return warpper


###注销###
def logout(request):
    request.session.clear()  # 把当前用户的session_data全部删除
    return redirect("/login/")


###主页###
# @chk_session
def index(request):
    return render(request, 'main.html', locals())


##表单##
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    confirmpassword = forms.CharField(label='确认密码', widget=forms.PasswordInput())


###注册###
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():       ##去如上定义的class UserForm检查格式是否符合标准
            #获得表单数据
            username = uf.cleaned_data['username'].lower()
            password = uf.cleaned_data['password']
            confirmpassword = uf.cleaned_data['confirmpassword']
            if password != confirmpassword:
                context = {'error': '密码输入不一致！'}
                return render(request, 'register.html', context)
            else:
                #添加到数据库
                filterResult=models.UserInfo.objects.filter(username=username)
                if len(filterResult)>0:
                    context={'error':'用户名已存在啦！'}
                    return  render(request,'register.html',context)
                else:
                    models.UserInfo.objects.create(username= username,password=password, confirmpassword=confirmpassword)
                    return render(request,'registersus.html', locals())
    else:
        uf = UserForm()
    return render(request,'register.html',{'uf':uf})


###分页###
# @chk_session
def fenyePage(request):
    obj_list = models.AdmDat.objects.all()

    paginator = Paginator(obj_list, 5)
    page = request.GET.get('page', 1)
    currentPage = int(page)

    try:
        print(page)
        obj_list = paginator.page(page)
    except PageNotAnInteger:
        obj_list = paginator.page(1)
    except EmptyPage:
        obj_list = paginator.page(paginator.num_pages)


    current_page_num = obj_list.number      # 获取当前页码
    # 获取前后各页
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略号
    if (page_range[0] - 1 >= 2):
        page_range.insert(0, '...')
    if (paginator.num_pages - page_range[-1] >= 2):
        page_range.append('...')
    #  加上首尾页码
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # return render(request, "main.html", locals())
    return render(request, "backend.html", locals())


###删除Admdat信息###
def admdatDel(request):
    del_id = request.GET.get("id", None)  # 获取到get请求的参数中的id内容
    del_name = request.GET.get("name", None)
    print("删除ID为{0},名称为‘{1}’的数据".format(del_id, del_name))
    if del_id:
        models.AdmDat.objects.filter(id=del_id).delete()
        return redirect('/fenye/')
    else:
        return HttpResponse("ERROR,检查数据后重试")  # 若不存在数据或其他错误


###编辑&更新Admdat信息###
def admdatEdit(request):
    if request.method == "GET":
        new_id1 = int(request.GET.get("id"))     ##get的id是str类型，需要转换成int
        obj = models.AdmDat.objects.filter(id=new_id1).first()
        ip_info = obj.ip_info
        serv_info = obj.serv_info
        cpu_info = obj.cpu_info
        disk_info = obj.disk_info
        mem_info = obj.mem_info
        load_info = obj.load_info
        mark_info = obj.mark_info
        return render(request, 'admdatEdit.html', locals())
    elif request.method == "POST":
        # new_id = int(request.GET.get("id"))
        # obj = models.AdmDat.objects.filter(id=new_id).first()
        new_id = request.POST.get("id")
        new_ip = request.POST.get('ip')
        new_serv = request.POST.get('serv')
        new_cpu = request.POST.get('cpu')
        new_disk = request.POST.get('disk')
        new_mem = request.POST.get('mem')
        new_load = request.POST.get('load')
        new_mark = request.POST.get('idc')
        try:
            chk_id = models.AdmDat.objects.filter(id=new_id)
        except:
            return render(request, 'faildedit.html', locals())
        else:
            chk_id = models.AdmDat.objects.filter(id=new_id)
            if len(chk_id) > 0:
                models.AdmDat.objects.filter(id=new_id).update(ip_info=new_ip, serv_info=new_serv, cpu_info=new_cpu,
                                                           disk_info=new_disk, mem_info=new_mem, load_info=new_load,
                                                           mark_info=new_mark)
                return redirect('/fenye/')
            else:
                return render(request, 'faildedit.html', locals())
                # return HttpResponse('<h3 style="color: red">ERROR : 您输入的id有误,请确认原id后操作!</h3>')


###增加新的AdmData信息###
def admAdd(request):
    error = ""
    if request.method == "POST":
        add_ip = request.POST.get("ip")
        add_serv = request.POST.get("serv")
        add_cpu = request.POST.get("cpu")
        add_disk = request.POST.get("disk")
        add_mem = request.POST.get("mem")
        add_load = request.POST.get("load")
        add_idc = request.POST.get("idc")
        if add_ip=="" and add_cpu=="" and add_serv=="" and add_disk=="" and add_mem=="" and add_load=="" and add_idc=="":
            error = "Error：添加数据不能为空！"
            return render(request, 'admdatAdd.html', {"error": error})
        else:
            models.AdmDat.objects.create(ip_info=add_ip, serv_info=add_serv, cpu_info=add_cpu, disk_info=add_disk,
                                         mem_info=add_mem, load_info=add_load, mark_info=add_idc)
            return redirect('/fenye/')

    return render(request, 'admdatAdd.html', locals())


###搜索###
def search(request):
    if request.method == "GET":
        search_mem = request.GET.get('mem')
        obj_mem = models.AdmDat.objects.filter(mem_info=search_mem)
        return render(request, 'search.html', locals())

    return render(request, 'backend.html', locals())

###通过id查看所有的数据###
def id_search(request):
    if request.method == 'GET':
        pass

def adtm(request):
    return render(request, 'adtm.html', locals())
