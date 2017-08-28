from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.core import serializers

def index(request):
    return render(request,'user_login/index.html')

def all_json(request):
    user_json = serializers.serialize("json", User.objects.all())
    return HttpResponse(user_json, content_type="application/json")

def all_html(request):
    return render(request,"user_login/all.html", {'users': User.objects.all()})

def find(request):
    users = User.objects.filter(first_name__startswith=request.POST["first_name_starts_with"])
    return render(request,"user_login/all.html", {'users': users})

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email'], age= request.POST['age'])
    return render(request, 'user_login/all.html',{ "users": User.objects.order_by("-id") })
