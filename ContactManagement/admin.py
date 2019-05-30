# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','email')

admin.site.register(Contact, ContactAdmin)
# Register your models here.
