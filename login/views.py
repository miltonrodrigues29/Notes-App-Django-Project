from django.shortcuts import render, redirect
from django.http import *
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout 
from .models import *
from .forms import CreateUserForm,notesForm
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required   

@login_required(login_url='login_page')
def notes_view(request):
    queryset = Notes.objects.all()
    form = notesForm(request.POST, request.FILES)
    # v_url
    if form.is_valid():
        n = form.cleaned_data["title"]
        des = form.cleaned_data["description"]
        i=  form.cleaned_data["image"]
        p= form.cleaned_data["pdf"]
        d=form.cleaned_data["doc"]
        v= form.cleaned_data["video"]
        a=form.cleaned_data["audio"]
        t = Notes(title=n,description=des,image=i,pdf=p,doc=d,video=v,audio=a)
        t.save()
        request.user.notes.add(t)
        return redirect('notes_page')
    context={'form':form ,
            'items':queryset
    }   
    return render(request,"notes.html",context)


# @login_required(login_url='login_page')
def home_view(request,*args,**kwargs):
    key_content={}
    return render(request,"index.html",key_content)

@login_required(login_url='login_page')
def contact_view(request,*args,**kwargs):
    return HttpResponse("<h1>Contact Page</h1>")


def login_view(request,*args,**kwargs):
    if request.user.is_authenticated:
        return redirect('notes_page')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('notes_page')
            else:
                messages.info(request, 'Username OR Password Incorrect')
        return render(request,"login.html",{})

def logoutUser(request):
    logout(request)
    return redirect('login_page')


def register_view(request,*args,**kwargs):
    if request.user.is_authenticated:
        return redirect('notes_page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form  = CreateUserForm(request.POST)
            if(form.is_valid()):
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,"Account was created for "+user)
                return redirect('login_page') 
        context = { 'form':form } 
        return render(request,"register.html",context)

def update_view(request,pk ):
    note = Notes.objects.get(id=pk)
    queryset = Notes.objects.all()
    form = notesForm(instance=note)
    if request.method == 'POST':
            form = notesForm(request.POST,request.FILES,instance=note)
            if form.is_valid():
                form.save()
                return redirect('notes_page')
    context={'form':form ,
            'items':queryset
    }
    return render(request,"notes.html",context)

def delete_view(request,pk):
    note = Notes.objects.get(id=pk)
    if request.method == "POST":
        note.delete()
        return redirect('notes_page')
    context = {'item':note}
    return render(request, 'delete.html',context)

def print_view(request,pk):
    note= Notes.objects.get(id=pk)
    context={
            'item':note
    }
    return render(request,"print_view.html",context)

def insight_view(request,pk):
    queryset = Notes.objects.all()
    form = notesForm(request.POST, request.FILES)
    context={'form':form ,
            'items':queryset
              } 
    
    return render(request,"insight.html",context)

def documents_view(request,pk):
    queryset = Notes.objects.all()
    form = notesForm(request.POST, request.FILES)
    context={'form':form ,
            'items':queryset
              } 
    
    return render(request,"documents.html",context)
def doc_view(request,pk):
    queryset = Notes.objects.all()
    form = notesForm(request.POST, request.FILES)
    context={'form':form ,
            'items':queryset
              } 
    
    return render(request,"doc.html",context)

def video_view(request,pk):
    queryset = Notes.objects.all()
    form = notesForm(request.POST, request.FILES)
    context={'form':form ,
            'items':queryset
              } 
    
    return render(request,"videos.html",context)


def image_view(request,pk):
    queryset = Notes.objects.all()
    form = notesForm(request.POST, request.FILES)
    context={'form':form ,
            'items':queryset
              } 
    
    return render(request,"images.html",context)

def audio_view(request,pk):
    queryset = Notes.objects.all()
    form = notesForm(request.POST, request.FILES)
    context={'form':form ,
            'items':queryset
              } 
    
    return render(request,"audios.html",context)


def go_back_view(request,pk):
    queryset = Notes.objects.all()
    form = notesForm(request.POST, request.FILES)
    # v_url
    context={'form':form ,
            'items':queryset
     }   
    return render(request,"notes.html",context)

def about_view(request):

    # v_url
    return render(request,"aboutus.html")

def support_view(request):

    # v_url
    return render(request,"support.html")

def publish_view(request,pk):
    t = Notes.objects.get(id=pk)
    t.publish= 1 # change field
    t.save()
    queryset = Notes.objects.filter(publish=1)
    form = notesForm(request.POST, request.FILES)
    context={'form':form ,
             'items':queryset
              } 
    
    return render(request, 'public_pages.html',context)

def public_view(request):
    queryset = Notes.objects.filter(publish=1)
    form = notesForm(request.POST, request.FILES)
    # v_url
    context={'form':form ,
            'items':queryset
          }   
    return render(request,"public_pages.html",context)
    
def private_view(request,pk):
    t = Notes.objects.get(id=pk)
    t.publish= 0 # change field
    t.save()
    queryset = Notes.objects.filter(publish=1)
    form = notesForm(request.POST, request.FILES)
    context={'form':form ,
             'items':queryset
              } 
    
    return render(request, 'public_pages.html',context)


