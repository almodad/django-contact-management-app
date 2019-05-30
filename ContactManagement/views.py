# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Contact
# Create your views here.

def contacts(request):
    clist = Contact.objects.all()
    return render(request,'contacts.html',{'data':clist})
