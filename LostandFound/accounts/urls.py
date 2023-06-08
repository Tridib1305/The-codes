from django.urls import path
from .views import SignUpView
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('', views.Lost_ObjectList.as_view(), name='home'),
    path('<slug:slug>/', views.Lost_ObjectDetail.as_view(),name='Lost_Object_detail'),
]