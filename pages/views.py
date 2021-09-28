from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView

def homePageView(request):
    return HttpResponse('Hello, World!')

class HomePageView(TemplateView):
 template_name = 'pages/home.html'
