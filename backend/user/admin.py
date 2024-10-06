from django.contrib import admin

from user.models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ["user_name", "first_name", "registered"]


admin.site.register(CustomUser, UserAdmin)
