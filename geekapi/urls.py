from django.contrib import admin
from django.urls import path,include
from .views import create_view,list_view,detail_view,update_view,delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create_view,name='create-view'),
    path('', list_view,name='list-view'),
    path('<id>', detail_view,name='detail-view'),
    path('<id>/update', update_view,name='update-view'),
    path('<id>/delete', delete_view,name='delete-view'),
]