
from django.contrib import admin

from libs.core.models.users.admin import AdminUser
from libs.core.models.users.dude import DudeUser


admin.site.register(AdminUser)
admin.site.register(DudeUser)
