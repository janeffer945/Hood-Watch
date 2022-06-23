from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='hood-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='hood-about'),
    path('neighborhood/', views.neighborhood, name='neighborhood'),
    path('neighborhood/<int:pk>/', views.neighborhoodDetail, name='neighborhood-detail'),
    path('business/', views.biz, name='business'),
    path('business/<int:pk>/', views.businessDetail, name='business-detail'),
    path('neighborhood/create/',views.createNeighborhood, name='create-hood'),
    path('neighborhood/<int:pk>/update/',views.updateNeighborhood, name='update-hood'),
    path('neighborhood/<int:pk>/delete/', views.deleteNeighborhood, name='delete-hood'),
]