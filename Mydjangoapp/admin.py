from django.contrib import admin

# Register your models here.

from django.contrib import admin
from Mydjangoapp import models


class Adata(admin.ModelAdmin):
    list_display = ['ip_info', 'serv_info', 'cpu_info', 'disk_info', 'mem_info', 'load_info', 'mark_info']

class UInfo(admin.ModelAdmin):
    list_display = ['username', 'password']

class Host(admin.ModelAdmin):
    list_display = ['hostname', 'cpu', 'mem', 'speed', 'os', 'remarks']

class Source(admin.ModelAdmin):
    list_display = ['name']

class Disk(admin.ModelAdmin):
    list_display = ['path', 'size', 'remarks']

class Login(admin.ModelAdmin):
    list_display = ['login_name', 'login_pwd', 'auth']

class Lable(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(models.UserInfo, UInfo)
admin.site.register(models.AdmDat, Adata)
admin.site.register(models.Host, Host)
admin.site.register(models.Source, Source)
admin.site.register(models.Disk, Disk)
admin.site.register(models.Os)
admin.site.register(models.Login, Login)
admin.site.register(models.Lable, Lable)