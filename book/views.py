from django.shortcuts import render
from django.views import  View
from django.views.generic import TemplateView
from .models import Publisher,Book,Category,Author
from django.http import HttpResponse

class Home(View):

    def get(self,request):
        qs=Category.objects.all()
        context={'cat':qs}
        return render(request,'home.html',context)

    def get(self,request):
        qs=Book.objects.all()
        contex={'book':qs}
        return render(request,'ShowAllPruducts.html',contex)

    template_name = 'home.html'



