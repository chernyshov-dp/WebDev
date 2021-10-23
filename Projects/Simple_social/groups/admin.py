from django.contrib import admin
from . import models


class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
