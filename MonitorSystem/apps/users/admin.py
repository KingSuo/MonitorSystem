from django.contrib import admin

from users.models import UserProfile

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'mobile']
    search_fields = ['username', 'email', 'mobile']
    list_filter = ['username', 'email', 'mobile']

admin.site.site_header = 'KingSuo后台管理系统'
admin.site.site_title = 'KingSuo'
