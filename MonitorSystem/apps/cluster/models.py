# -*- encoding:utf-8 -*-
import uuid
import datetime

from django.db import models

# Create your models here.


class ServerStaticInfoModel(models.Model):
    server_id = models.UUIDField(null=False, blank=False, default=uuid.uuid4, verbose_name=u'服务器ID')
    server_ip = models.CharField(max_length=15, null=False, blank=False, default='127.0.0.1',
                                 verbose_name=u'服务器ip地址')
    # cat /etc/hostname
    hostname = models.CharField(max_length=30, null=False, blank=False, default='localhost', verbose_name=u'主机名')
    # whoami
    owner = models.CharField(max_length=20, null=False, blank=False, default='unknown', verbose_name=u'所有者')
    # cat /proc/cpuinfo
    detail = models.CharField(max_length=1024, verbose_name=u'服务器详细信息')
    # curl ip.cn/server_ip
    location = models.CharField(max_length=50, verbose_name=u'服务器所在地区')
    create_time = models.DateTimeField(null=False, blank=False, default=datetime.datetime.now,
                                       verbose_name=u'添加时间', editable=False)
    is_deleted = models.BooleanField(default=False, verbose_name=u'是否被删除')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'更新时间')

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = u'服务器信息'
        verbose_name_plural = verbose_name


class CpuModel(models.Model):
    """
    实时刷新，留历史数据，通过内存来运算并保存有限历史数据，可以通过list数据类型来缓存历史数据，
    当len（list）达到设置阈值时将数据保存到数据库。
    """
    server_id = models.UUIDField(null=False, blank=False, default=uuid.uuid4, verbose_name=u'服务器ID')
    status = models.CharField(max_length=10, null=False, blank=False, verbose_name=u'运行状态', default='unknown',
                              choices=(('running', u'运行中'), ('stopped', u'已停止'), ('stopping', u'停止中'),
                                       ('starting', u'启动中'), ('unknown', u'未知')))
    # date +"%Y-%m-%d %H:%M:%S"
    current_time = models.DateTimeField(verbose_name=u'系统当前时间')
    # uptime
    running_time = models.CharField(max_length=50, verbose_name=u'系统已运行时间')
    # uptime -s
    system_up_date = models.DateTimeField(verbose_name=u'系统创建时间')
    # uptime
    number_of_logged_users = models.PositiveIntegerField(verbose_name=u'登录用户数目')
    # uptime
    load_average = models.CharField(max_length=128, verbose_name=u'CPU最近1min,5min,15min负载')
    # vmstat
    cpu_utilization_ratio = models.FloatField(max_length=6, null=False, blank=False, default=0.0, verbose_name=u'CPU使用率')

    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'更新时间')

    def __str__(self):
        return self.server_id

    class Meta:
        verbose_name = u'CPU信息'
        verbose_name_plural = verbose_name


class MemoryModel(models.Model):   
    server_id = models.UUIDField(null=False, blank=False, default=uuid.uuid4, verbose_name=u'服务器ID')
    # cat /pro/meminfo (Active - MemFree) / MemTotal
    mem_utilization_ratio = models.FloatField(max_length=6, null=False, blank=False, default=0.0, verbose_name=u'内存使用率')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'更新时间')

    def __str__(self):
        return self.server_id

    class Meta:
        verbose_name = u'内存信息'
        verbose_name_plural = verbose_name


class DiskModel(models.Model):
    server_id = models.UUIDField(null=False, blank=False, default=uuid.uuid4, verbose_name=u'服务器ID')
    # df  “Filesystem”为“/dev/vda1”的“Use%”或“Mounted on”为"/"的“Use%”
    mem_utilization_ratio = models.FloatField(max_length=6, null=False, blank=False, default=0.0, verbose_name=u'内存使用率')
    # iostat -d
    KB_readps = models.PositiveIntegerField(verbose_name=u'系统磁盘总读KBPS')
    KB_wrtnps = models.PositiveIntegerField(verbose_name=u'系统磁盘写读KBPS')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'更新时间')

    def __str__(self):
        return self.server_id

    class Meta:
        verbose_name = u'磁盘信息'
        verbose_name_plural = verbose_name


class NetworkInfoModel(models.Model):
    server_id = models.UUIDField(null=False, blank=False, default=uuid.uuid4, verbose_name=u'服务器ID')
    # sar -n DEV [seconds][times]
    public_rx_kbps = models.FloatField(max_length=6, null=False, blank=False, default=0.0, verbose_name=u'公网网络流入带宽')
    public_tx_kbps = models.FloatField(max_length=6, null=False, blank=False, default=0.0, verbose_name=u'公网网络流出带宽')
    # sar -n DEV [seconds][times] "eth0"
    private_rx_kbps = models.FloatField(max_length=6, null=False, blank=False, default=0.0, verbose_name=u'私网网络流入带宽')
    private_tx_kbps = models.FloatField(max_length=6, null=False, blank=False, default=0.0, verbose_name=u'私网网络流出带宽')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'更新时间')

    def __str__(self):
        return self.server_id

    class Meta:
        verbose_name = u'网路信息'
        verbose_name_plural = verbose_name


class ProcessInfoModel(models.Model):
    server_id = models.UUIDField(null=False, blank=False, default=uuid.uuid4, verbose_name=u'服务器ID')
    # ps -A | wc -l
    total_processes = models.PositiveIntegerField(verbose_name=u'进程总数')
    # netstat -at | wc -l
    total_tcp = models.PositiveIntegerField(verbose_name=u'TCP进程总数')
    # netstat -at | grep ESTABLISHED | wc -l
    established_tcp = models.PositiveIntegerField(verbose_name=u'已建立TCP总数')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'更新时间')

    def __str__(self):
        return self.server_id

    class Meta:
        verbose_name = u'进程信息'
        verbose_name_plural = verbose_name
