# -*- encoding:utf-8 -*-
import uuid
import datetime

from django.db import models

# Create your models here.


class ServerInfoModel(models.Model):
    server_id = models.UUIDField(null=False, blank=False, default=uuid.uuid4, verbose_name=u'服务器ID')
    server_ip = models.CharField(max_length=15, null=False, blank=False, default='127.0.0.1', unique=True, verbose_name=u'服务器ip地址')
    location = models.CharField(max_length=50, verbose_name=u'服务器所在地区')
    hostname = models.CharField(max_length=30, null=False, blank=False, default='localhost', verbose_name=u'主机名')
    status = models.CharField(max_length=10, null=False, blank=False, verbose_name=u'运行状态', default='unknown',\
                              choices=(('running', u'运行中'), ('stop', u'停止'), ('destroy', u'损坏'), ('unknown', u'未知')))
    owner = models.CharField(max_length=20, null=False, blank=False, default='unknown', verbose_name=u'所有者')
    cpu_usage_rate = models.FloatField(max_length=6, null=False, blank=False, default=0.0, verbose_name=u'CPU使用率')
    mem_usage_rate = models.FloatField(max_length=6, null=False, blank=False, default=0.0, verbose_name=u'内存使用率')
    create_time = models.DateTimeField(null=False, blank=False, default=datetime.datetime.now,\
                                       verbose_name=u'添加时间', editable=False)
    update_time = models.DateTimeField(default=datetime.datetime.now, auto_now=True, verbose_name=u'更新时间')
    is_deleted = models.BooleanField(default=False, verbose_name=u'是否被删除')

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = u'服务器信息'
        verbose_name_plural = verbose_name


class CpuInfoModel(models.Model):

    current_time = models.CharField
    running_time = models.CharField
    number_of_logged_users = models.PositiveIntegerField
    load_average = models.CharField
    create_time = models.DateTimeField(null=False, blank=False, default=datetime.datetime.now, \
                                       verbose_name=u'添加时间', editable=False)
    update_time = models.DateTimeField(default=datetime.datetime.now, auto_now=True, verbose_name=u'更新时间')
    is_deleted = models.BooleanField(default=False, verbose_name=u'是否被删除')


class MemInfoModel(models.Model):
    pass


class DiskInfoModel(models.Model):
    pass


class NetworkInfoModel(models.Model):
    pass


class ProcessInfoModel(models.Model):
    pass
