from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .models import Owl, Toy
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def owl_index(request):
  owls = Owl.objects.filter(user=request.user)
  return render(request, 'owls/index.html', { 'owls': owls })

@login_required
def owl_detail(request, owl_id):
  owl = Owl.objects.get(id=owl_id)
  toys_owl_doesnt_have = Toy.objects.exclude(id__in = owl.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'owls/detail.html', {
    'owl': owl,
    'feeding_form': feeding_form,
    'toys': toys_owl_doesnt_have
  })

@login_required
def add_feeding(request, owl_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.owl_id = owl_id
    new_feeding.save()
  return redirect('owl-detail', owl_id=owl_id)

@login_required
def assoc_toy(request, owl_id, toy_id):
  Owl.objects.get(id=owl_id).toys.add(toy_id)
  return redirect('owl-detail', owl_id=owl_id)

class OwlCreate(LoginRequiredMixin, CreateView):
  model = Owl
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class OwlUpdate(LoginRequiredMixin, UpdateView):
  model = Owl
  fields = ['breed', 'description', 'age']

class OwlDelete(LoginRequiredMixin, DeleteView):
  model = Owl
  success_url = '/owls/'

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('owl-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  return render(request, 'signup.html', {
    'form': form,
    'error_message': error_message
  })