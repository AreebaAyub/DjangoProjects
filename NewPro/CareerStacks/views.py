from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_protect
from django.utils.datastructures import MultiValueDictKeyError
from .models import Destination, Comment, Reply
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def mcat(request):
    return render(request,'mcat.html')
def ecat(request):
    return render(request,'ecat.html')
def contact(request):
    return render(request,'contactus.html')
def aboutt(request):
    return render(request,'about.html')
def how(request):
    return render(request,'howtouse.html')
def loginredircect(request):
    return render(request,'login.html')
def registerdirect(request):
    return render(request,'userreg.html')
def UserRegistration(request):
     if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        email= request.POST.get('email')
        user=User.objects.create_user(username=username,password=password)
        user.save();
        return render(request,'home.html')

def UserLogin(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,'home.html',{'username':username})
        else:
            messages.info(request,'invalid credentials')
            return redirect('login.html')
    else:
        return render(request,'home.html')

def query(request):
    comment=Comment()
    if request.method=='POST':

        comment.user=request.user
        comment.content= request.POST.get('content')
        #reply_id=request.POST.get('comment_id')
            

        

        comment.save()
        
    comments = Comment.objects.all().order_by("-id")
    parms={
        'comments':comments,
        }

    return render(request,'query.html',parms)

def commentreply(request):
    repObj=Reply()
    output = {}
    if request.method=='GET':
        comment = Comment.objects.get(id=int(request.GET.get('cmid')))
        repObj.user=request.user
        repObj.comment=comment
        repObj.body=request.GET.get("reply")
        repObj.save()

        output['body'] = repObj.body
        output['date'] = repObj.timestamp
        output['username'] = repObj.user.username


    # html = render_to_string('query.html', {'rList': rList})
    return JsonResponse(output)