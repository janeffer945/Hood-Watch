from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   path('^$',views.index,name="index"),
   path('login/',views.signin,name='login'),
   path('register/',views.register,name='register'),
   path('signout/',views.signout,name='signout'),
   path('profile/',views.profile,name='profile'),
   path('update', views.update_profile, name='update'),
   path('new-hood/', views.posthood, name='newhood'),
   path('newpost/', views.addposts, name='newpost'),
   path('displayhood/', views.displayhood, name='displayhood'),
   path('displaypost/', views.displaypost, name='displaypost'),

    path('joinhood/(?P<id>\d+)?$', views.join_hood, name='joinhood'), 
    path('leavehood/(?P<id>\d+)?$', views.leave_hood, name='leavehood'), 
   path('viewhood/(?P<hood_id>\d+)?$', views.viewhood, name='viewhood'),
   path('addpost/$', views.new_post, name='addpost'),
 path('members/(?P<hood_id>\d+)?$', views.hood_members, name='members'), 
 path('search/', views.search_business, name='search'),



]  