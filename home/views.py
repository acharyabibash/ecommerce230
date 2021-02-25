from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View


from home.models import Category,Slider,Ad,Item

class BaseView(View):
    views = {}


class HomeView(BaseView):
    def get(self,request):
        self.views['categories']= Category.objects.all()
        self.views['slider']=Slider.objects.all()
        self.views['ads']=Ad.objects.all()
        self.views['new-items']=Item.objects.filter(label='new')
        self.views['hot-items']=Item.objects.filter(label='new')
        self.views['sale-items']=Item.objects.filter(label='new')
        
        return render(request,'index.html',self.views)
