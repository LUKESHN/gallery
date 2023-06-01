from django.shortcuts import render,redirect
from django.views import View
from.forms import RegisterForm,LoginForm,ImageForm
from django.contrib.auth import authenticate,login,logout

from . models import CatagoryModels,ImageModel
# Create your views here.

def signout_view(request):
    logout(request)
    return redirect('home')

class home_view(View):

    def get(self,request):

        if request.user.is_authenticated:
            return redirect('gallery')
        forms=LoginForm()
        context={'forms':forms}
        return render (request,'home.html',context)

    def post(self,request):

        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login (request,user)
            return redirect('gallery')
        return redirect('home')
        return render (request,'home.html')

class register_view(View):

    def get(self,request):
        forms=RegisterForm()
        context={'forms':forms}
        return render (request,'register.html',context)

    def post(self,request):

        forms=RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
        context={'forms':forms}


        return render (request,'register.html',context)

class gallery_view(View):

    def get(self,request):

        category = CatagoryModels.objects.all()
        Images=ImageModel.objects.all()


        context={'category':category,'Images':Images}

        return render (request,'gallery.html',context)
    def post(self,request):
        return render (request,'gallery.html')

class Cat_view(View):

    def get(self,request,id):
        Images=ImageModel.objects.filter(cat=id)

        category = CatagoryModels.objects.all()

        context={'Images':Images,'category':category}
        return render(request,'gallery.html',context)

    
class addimage_view(View):

    def get(self,request):

        forms=ImageForm()
        context={'forms':forms}

        return render (request,'addimage.html',context)

    def post(self,request):

        forms=ImageForm(request.POST,request.FILES)
        if forms.is_valid():
            task=forms.save(commit=False)
            task.uploaded_by=request.user
            task.save()
            return redirect('gallery')

        
        return render (request,'addimage.html')
class myupload_view(View):
    def get(self,request):
        Images=ImageModel.objects.filter(uploaded_by=request.user)
        context={'Images':Images}
        return render(request,'myupload.html',context)
    
