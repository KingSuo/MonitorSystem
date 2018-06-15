# -*- encoding:utf-8 -*-
from django.contrib import admin

from cluster.models import ServerModel, CpuModel, MemoryModel, DiskModel, NetworkModel, ProcessModel

# Register your models here.


@admin.register(ServerModel)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['server_id', 'server_ip', 'hostname', 'owner', 'detail', 'location',
                    'create_time', 'is_deleted', 'update_time']
    search_fields = ['server_id', 'server_ip', 'hostname', 'owner', 'detail', 'location',
                     'create_time', 'is_deleted', 'update_time']
    list_filter = ['server_id', 'server_ip', 'hostname', 'owner', 'detail', 'location',
                   'create_time', 'is_deleted', 'update_time']

    actions = ['refresh_data']

    def refresh_data(modelAdmin, request, queryset):
        for server_model in queryset:
            cpu_model = CpuModel()
            cpu_model.server_id = server_model.server_id

            memory_model = MemoryModel()
            memory_model.server_id = server_model.server_id

            disk_model = DiskModel()
            disk_model.server_id = server_model.server_id

            network_model = NetworkModel()
            network_model.server_id = server_model.server_id

            process_model = ProcessModel()
            process_model.server_id = server_model.server_id

            cpu_model.save()
            memory_model.save()
            disk_model.save()
            network_model.save()
            process_model.save()

    refresh_data.short_description = u'刷新数据'


@admin.register(CpuModel)
class CpuAdmin(admin.ModelAdmin):
    list_display = ['id', 'server_id', 'status', 'current_time', 'running_time', 'system_up_date',
                    'number_of_logged_users', 'load_average', 'cpu_utilization_ratio', 'update_time']
    search_fields = ['id', 'server_id', 'status', 'current_time', 'running_time', 'system_up_date',
                     'number_of_logged_users', 'load_average', 'cpu_utilization_ratio', 'update_time']
    list_filter = ['id', 'server_id', 'status', 'current_time', 'running_time', 'system_up_date',
                   'number_of_logged_users', 'load_average', 'cpu_utilization_ratio', 'update_time']
    list_display_links = ['id', 'server_id']

    actions = ['refresh_data']

    def refresh_data(modelAdmin, request, queryset):
        pass

    refresh_data.short_description = u'刷新数据'


@admin.register(MemoryModel)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'server_id', 'mem_utilization_ratio', 'update_time']
    search_fields = ['id', 'server_id', 'mem_utilization_ratio', 'update_time']
    list_filter = ['id', 'server_id', 'mem_utilization_ratio', 'update_time']
    list_display_links = ['id', 'server_id']

    actions = ['refresh_data']

    def refresh_data(modelAdmin, request, queryset):
        pass

    refresh_data.short_description = u'刷新数据'


@admin.register(DiskModel)
class DiskAdmin(admin.ModelAdmin):
    list_display = ['id', 'server_id', 'mem_utilization_ratio', 'KB_readps', 'KB_wrtnps', 'update_time']
    search_fields = ['id', 'server_id', 'mem_utilization_ratio', 'KB_readps', 'KB_wrtnps', 'update_time']
    list_filter = ['id', 'server_id', 'mem_utilization_ratio', 'KB_readps', 'KB_wrtnps', 'update_time']
    list_display_links = ['id', 'server_id']

    actions = ['refresh_data']

    def refresh_data(modelAdmin, request, queryset):
        pass

    refresh_data.short_description = u'刷新数据'


@admin.register(NetworkModel)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ['id', 'server_id', 'public_rx_kbps', 'public_tx_kbps', 'private_rx_kbps',
                    'private_tx_kbps', 'update_time']
    search_fields = ['id', 'server_id', 'public_rx_kbps', 'public_tx_kbps', 'private_rx_kbps',
                     'private_tx_kbps', 'update_time']
    list_filter = ['id', 'server_id', 'public_rx_kbps', 'public_tx_kbps', 'private_rx_kbps',
                   'private_tx_kbps', 'update_time']
    list_display_links = ['id', 'server_id']

    actions = ['refresh_data']

    def refresh_data(modelAdmin, request, queryset):
        pass

    refresh_data.short_description = u'刷新数据'


@admin.register(ProcessModel)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['id', 'server_id', 'total_processes', 'total_tcp', 'established_tcp', 'update_time']
    search_fields = ['id', 'server_id', 'total_processes', 'total_tcp', 'established_tcp', 'update_time']
    list_filter = ['id', 'server_id', 'total_processes', 'total_tcp', 'established_tcp', 'update_time']
    list_display_links = ['id', 'server_id']

    actions = ['refresh_data']

    def refresh_data(modelAdmin, request, queryset):
        pass

    refresh_data.short_description = u'刷新数据'

