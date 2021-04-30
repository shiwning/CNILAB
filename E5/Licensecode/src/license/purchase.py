import sqlite3
from ult.ServerAct import makeLicense, searchLicense
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django import forms
from ult.config import *

class PurchaseForm(forms.Form):
    username = forms.CharField(
        label="username",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label="password",
        max_length=20,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    usernum = forms.IntegerField(
        label="usernum",
        widget=forms.NumberInput(attrs={'class': 'form-control'}))

def purchase(request):
    if request.method == "POST":
        purchase_form=PurchaseForm(request.POST)
        # 在前端传回时也将跳转链接传回来
        next_url = request.POST.get("next_url")
        if purchase_form.is_valid():
            userName = purchase_form.cleaned_data['username']
            password = purchase_form.cleaned_data['password']
            userNum = purchase_form.cleaned_data['usernum']

            license = makeLicense()
            while searchLicense(license) == True:
                license = makeLicense()
            conn = sqlite3.connect(databaseName)
            curs = conn.cursor()
            sql = 'insert into license(Lno,userName,password,userNum) values (:license,:userName,:password,:userNum)'
            param = []
            param.append(license)
            param.append(userName)
            param.append(password)
            param.append(userNum)
            try:
                curs.execute(sql, param)
                conn.commit()
                messages.success(request, "Successfully Purchase, license:"+license)
                return redirect('/')
            except sqlite3.OperationalError as msg:
                messages.error(request, "Failed to Purchase: Database insert error")
                #返回失败
                return render(request,'purchase.html',locals())
            #print("License generated successfully")
    purchase_form = PurchaseForm()
    next_url = request.GET.get("next", '')
    return render(request,'purchase.html',locals())
    #else:
    #    purchase_form=forms(request.POST)
    #    return render(request, 'purchase.html', locals())
