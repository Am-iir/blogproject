from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm
# Create your views here.

def post_create(request): #takes request and returns response Create
   form=PostForm(request.POST or None , request.FILES or None)
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
   queryset_list = Post.objects.all()#.order_by("-timestamp")
   paginator = Paginator(queryset_list, 4) # Show 4 contacts per page
   page_request_var="page"
   page = request.GET.get('page_request_var')
   try:
      queryset = paginator.page(page)
   except PageNotAnInteger:
      # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
   except EmptyPage:
      # If page is out of range (e.g. 9999), deliver last page of results.
      queryset = paginator.page(paginator.num_pages)
   context = {
      "object_list":queryset,      
      "title":"List" ,
      "page_request_var":page_request_var
      }   

   # if request.user.is_authenticated(): 
   #    context = {
   #    "title":"User List"
   #     }
   # else:   
   #    context = {
   #    "title":"List"
   #    }
   return render(request,"post_list.html",context)
   # return HttpResponse("<h1>List</h1>")
   

def post_update(request,id=None): #Update
   instance =get_object_or_404(Post, id=id)
   form=PostForm(request.POST or None, request.FILES or None , instance=instance)
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
    
def post_delete(request, id=None): #Delete
   instance =get_object_or_404(Post, id=id)
   instance.delete()
   messages.success(request,"Sucessfully deleted")
   return redirect("posts:list")
    
def post_detail(request,id=None): #Detail retrieve
   #instance = Post.objects.get(id=2)
   instance =get_object_or_404(Post, id=id)
   context = {
      "title":instance.title,
      "instance":instance
   }
   return render(request,"post_detail.html",context)

