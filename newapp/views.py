from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())

def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())


