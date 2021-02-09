from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/index', views.index, name='index'),
    path('add/add', views.addView, name='add'),
    path('add/',views.addView, name='add'),
    path('store', views.store, name='store'),
    path('view/<int:pk>', views.viewBookorMovie, name='viewBookorMovie'),
    path('delete/<int:pk>', views.deleteBookorMovie, name='deleteBookorMovie'),
    path('update/<int:pk>',views.updateBookorMovie, name='updateBookorMovie'),
    path('edit/<int:pk>', views.update, name='edit'),
    path('view/index', views.index, name='index'),
    path('view/add', views.addView, name='add'),
    path('update/index',views.index, name='index'),
    path('update/add',views.addView, name='add'),
]