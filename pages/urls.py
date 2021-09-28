from django.urls import path
from .views import homePageView, HomePageView

urlpatterns = [
  path('', homePageView, name='home'),
  path('home/', HomePageView.as_view(), name='home'),
]