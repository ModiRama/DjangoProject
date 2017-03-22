from django.views.generic import View
from django.shortcuts import render
class Index(View):
    def get(self,request):
        params = {}
        params["name"] = "Muhammad"
        return render(request,'base.html',params)