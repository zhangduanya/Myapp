from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=128,null=False)    # max_length为约束长度，default为默认值
    password = models.CharField(max_length=128,null=False)    # null=True为允许为空
    confirmpassword = models.CharField(max_length=128,null=False)

class AdmDat(models.Model):
    ip_info = models.CharField(max_length=50)
    serv_info = models.CharField(max_length=50)
    cpu_info = models.CharField(max_length=50)
    disk_info = models.CharField(max_length=50)
    mem_info = models.CharField(max_length=50)
    load_info = models.CharField(max_length=50)
    mark_info = models.CharField(default='BEIJING_IDC', max_length=50, blank=True)
    def __str__(self):
        return self.ip_info


class Host(models.Model):
    '''主机,阿里云eth0 内网网卡， eth1 公网网卡'''
    hostname = models.CharField(max_length=64, blank=True, null=True, verbose_name='阿里云主机名')
    ecsname = models.CharField(max_length=64, blank=True, null=True, verbose_name='阿里云实例ID')
    logining = models.ManyToManyField(to='Login', blank=True, null=True, verbose_name='授权用户')
    login_port = models.CharField(max_length=16, default='22', blank=True, null=True, verbose_name='ssh登录端口')
    cpu = models.CharField(max_length=8, blank=True, null=True, verbose_name='CPU')
    lab = models.ForeignKey(to='Lable', blank=True, null=True, verbose_name='标签', on_delete=models.CASCADE)
    mem = models.CharField(max_length=8, blank=True, null=True, verbose_name='内存/M')
    speed = models.CharField(max_length=8, blank=True, default='5', null=True, verbose_name='带宽/M')
    disks = models.ManyToManyField(to='Disk', blank=True, null=True, verbose_name='磁盘')
    eth1_network = models.CharField(max_length=32, blank=True, null=True, verbose_name='公网IP')
    eth0_network = models.CharField(max_length=32, verbose_name='私网IP')
    sn = models.CharField(max_length=64, blank=True, null=True, verbose_name='sn')
    os = models.ForeignKey(to='Os', blank=True, null=True, verbose_name='操作系统', on_delete=models.CASCADE)  # os+版本号
    kernel = models.CharField(max_length=64, blank=True, null=True, verbose_name='系统内核')  # 内核+版本号
    the_upper = models.ForeignKey(to='Host', blank=True, null=True, verbose_name='宿主机', related_name='upper', on_delete=models.CASCADE)
    source = models.ForeignKey(to='Source', blank=True, null=True, verbose_name='来源类型', related_name='qq', on_delete=models.CASCADE)
    remarks = models.CharField(max_length=2048, blank=True, null=True, verbose_name='备注')
    createtime = models.CharField(max_length=32, blank=True, null=True, verbose_name='创建时间')
    expirytime = models.CharField(max_length=32, blank=True, null=True, verbose_name='到期时间')
    state_choices = (
        (1, 'Running'),
        (2, '下线'),
        (3, '关机'),
        (4, '删除'),
    )
    state = models.SmallIntegerField(verbose_name='主机状态', choices=state_choices, blank=True, null=True, )

    def __str__(self):
        return self.eth0_network

    class Meta:
        verbose_name_plural = "主机表"


class Source(models.Model):
    '''来源：阿里云、物理机（某机房等）'''
    name = models.CharField(max_length=16, blank=True, null=True, verbose_name='来源')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "主机来源表"


class Disk(models.Model):
    '''磁盘'''
    path = models.CharField(max_length=64, blank=True, null=True, verbose_name='挂载路径')
    size = models.CharField(max_length=16, blank=True, null=True, verbose_name='磁盘大小/G')
    remarks = models.CharField(max_length=2048, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.size

    class Meta:
        verbose_name_plural = "磁盘表"


class Os(models.Model):
    '''系统'''
    name = models.CharField(max_length=16, blank=True, null=True, verbose_name='系统名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "操作系统表"


class Login(models.Model):
    '''登录相关'''
    login_name = models.CharField(max_length=16, default='root', verbose_name='登录用户名')
    login_pwd = models.CharField(max_length=64, blank=True, null=True, verbose_name='登录密码')
    auth = models.CharField(max_length=8, blank=True, null=True, verbose_name='具有权限')

    def __str__(self):
        return self.login_name

    class Meta:
        verbose_name_plural = "主机用户表"


class Lable(models.Model):
    # 标签
    name = models.CharField(max_length=16, blank=True, null=True, verbose_name='标签')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "标签"

