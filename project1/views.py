from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Users,uploads_sl,shop,desg,category,uploads_cat,uploads_qb
from .forms import sl_form,seniority_add_form,qb_add_form,nofi_add_form
from django.core.files.storage import FileSystemStorage
from project1.function import handle_uploaded_file
from django.contrib import messages

# from .forms import CustomUserCreationForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def loginto(request):
    e=request.POST.get('uname')
    p=request.POST.get('upassword')
    v=Users.objects.get(uname=e)
    if e=='admin' and p=='0000':
        request.session['admin']=e
        return render(request,'index.html')
        # return HttpResponse('welcome Admin')

    elif e==v.uname and p==v.upassword:
        request.session['kedar']=e
        return redirect('/')
    else:
        return HttpResponse('<h1>Error</h1>')

def logout(request):
    request.session.flush()
    return redirect('/')

def admin_panel(request):
    return render(request,'admin_panel.html')

def seniority(request):
    # sop=shop.objects.filter(shopName='fitter') 'sop':sop,'dsg':dsg}
    # dsg=desg.objects.filter()
    # form=sl_form()
    # sl=uploads_sl.objects.all()
    # return render(request,'seniority.html',{'sl':sl,'form':form})
    form=sl_form()
    s=request.GET.get('shop')
    d=request.GET.get('desg')
    if d=='none':
        d='sse'
    elif s=='none':
        s='fitter'
    else:
        pass
    sl_f=uploads_sl.objects.filter(shop=s,desg=d)
    return render(request,'seniority.html',{'sl_f':sl_f,'form':form})

def collect(request):
    pass
    # form=sl_form()
    # s=request.GET.get('shop')
    # d=request.GET.get('desg')
    # sl_f=uploads_sl.objects.filter(shop=s,desg=d)
    # return render(request,'seniority.html',{'sl_f':sl_f,'form':form})

def notification(request):
    c=category.objects.all()
    if request.method == "POST":
        key=request.POST.get('dropdown')
        cat_list=uploads_cat.objects.filter(cat_name=key)
        return render(request,'notification.html',{'c':c,'cat_list':cat_list})
    return render(request,'notification.html',{'c':c})

def circular(request):
    c=category.objects.all()
    if request.method == "POST":
        key=request.POST.get('dropdown')
        cat_list=uploads_cat.objects.filter(cat_name=key)
        return render(request,'circulars.html',{'c':c,'cat_list':cat_list})
    return render(request,'circulars.html',{'c':c})

def qb(request):
    s=shop.objects.all()
    if request.method == "POST":
        key=request.POST.get('dropdown')
        qb_list=uploads_qb.objects.filter(shop=key)
        return render(request,'questionBank.html',{'s':s,'qb_li':qb_list})
    return render(request,'questionBank.html',{'s':s})
    

def add_seniority(request):
    form=seniority_add_form()
    return render(request,'add_seniority.html',{'form':form})

def add_qb(request):
    form=qb_add_form()
    return render(request,'add_QB.html',{'form':form})
# fs=FileSystemStorage(location='/media/files')
def add_notification(request):
    form=nofi_add_form()
    return render(request,'add_notification',{'form':form})



def add_sl(request):
    if request.method == 'POST':
        add=seniority_add_form(request.POST,request.FILES)
        if add.is_valid():
            handle_uploaded_file(request.FILES['files'])
        add.save()
    return render(request,'index.html')

def add_questionbank(request):
    if request.method == 'POST':
        add=qb_add_form(request.POST,request.FILES)
        if add.is_valid():
            handle_uploaded_file(request.FILES['files'])
        add.save()
    return render(request,'index.html')





def attachment(request,files):
    try:
        img_data=open("C:/Users/WALAVALKAR/Desktop/django/Railway/project1/static/upload/{files}".format(files=files),"rb").read()
        return HttpResponse(img_data,content_type="application/pdf")
    except:
        return HttpResponse('<script>alert("No such File Exist");</script>')