from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages, auth

from .forms import SchoolForm

from django.core import serializers
import json

from .models import School


# Create your views here.
def index(request):
    return render(request,'homepage.html')



def order(request):
    # depart=department.objects.all()
    # courses=Courses.objects.all()
    if request.method == "POST":
        name = request.POST.get('name',)
        dob = request.POST.get('dob', )
        age = request.POST.get('age', )
        gender = request.POST.get('gender',)
        phone = request.POST.get('phone', )
        emailid= request.POST.get('emailid', )
        address = request.POST.get('address', )
        dept = request.POST.get('dept', )
        courses1 = request.POST.get('courses', )
        purpose = request.POST.get('purpose', )
        materials = request.POST.get('materials', )
        school=School(name=name,dob=dob,age=age,gender=gender,phone=phone,emailid=emailid,address=address,
                      dept=dept,courses1=courses1,purpose=purpose,materials=materials)

        return render(request,'confirm.html')

    # return render(request,'order.html',{'department':depart,'courses':courses})
    return render(request,'order.html')






