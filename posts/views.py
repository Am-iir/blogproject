from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404

from .models import Post
from .forms import PostForm
# Create your views here.

def post_create(request): #takes request and returns response Create
   form=PostForm(request.POST or None)
   if form.is_valid():
      instance=form.save(commit=False)
      print (form.cleaned_data.get("title")) #print 
      instance.save()
      #sucess message
      messages.success(request,"Sucessfully saved")
      return HttpResponseRedirect(instance.get_absolute_url())
   #else: 
    #  messages.error(request,"Failed")   #failure message

   # if request.method == "POST": #if post is available then print
   #    print (request.POST.get("content"))
   #    print (request.POST.get("title"))


   context={
      "form" : form,
   }
   return render(request,"post_form.html",context)

def post_list(request): #List
   queryset = Post.objects.all()
   context = {
      "object_list":queryset,      
      "title":"List" 
      }   
   # if request.user.is_authenticated(): 
   #    context = {
   #    "title":"User List"
   #     }
   # else:   
   #    context = {
   #    "title":"List"
   #    }
   return render(request,"index.html",context)
   # return HttpResponse("<h1>List</h1>")
   

def post_update(request,id=None): #Update
   instance =get_object_or_404(Post, id=id)
   form=PostForm(request.POST or None, instance=instance)
   if form.is_valid():
      instance=form.save(commit=False)
      print (form.cleaned_data.get("title")) #print 
      instance.save()
      #sucess message      
      messages.success(request,"Sucessfully saved")
      return HttpResponseRedirect(instance.get_absolute_url())
      
   context = {
      "title":instance.title,
      "instance":instance,
      "form" : form,
   }
   return render(request,"post_form.html",context)
    
def post_delete(request): #Delete
    return HttpResponse("<h1>Delete</h1>")
    
def post_detail(request,id=None): #Detail retrieve
   #instance = Post.objects.get(id=2)
   instance =get_object_or_404(Post, id=id)
   context = {
      "title":instance.title,
      "instance":instance
   }
   return render(request,"post_detail.html",context)

