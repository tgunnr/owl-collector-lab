from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('owls/', views.owl_index, name='owl-index'),
  path('owls/<int:owl_id>/', views.owl_detail, name='owl-detail'),
  path('owls/create', views.OwlCreate.as_view(), name='owl-create'),
  path('owls/<int:pk>/update/', views.OwlUpdate.as_view(), name='owl-update'),
  path('owls/<int:pk>/delete/', views.OwlDelete.as_view(), name='owl-delete'),
  path('owls/<int:owl_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
  path('owls/<int:owl_id>/assoc-toy/<int:toy_id>/', views.assoc_toy, name='assoc-toy'),
  path('accounts/signup/', views.signup, name='signup')
]