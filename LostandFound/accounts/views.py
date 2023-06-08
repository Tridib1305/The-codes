from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Lost_Object

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class Lost_ObjectList(generic.ListView):
    queryset=Lost_Object.objects.filter(Status="Lost").order_by('-Lost_on')
    template_name='home.html'

class Lost_ObjectDetail(generic.DetailView):
    model=Lost_Object
    template_name='Lost_Object_detail.html'

