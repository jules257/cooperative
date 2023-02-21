from django.contrib import admin
from django.urls import path

from app.views import home,categories




urlpatterns = [
    path('',home.index, name='home'),
    
    path('categories/',categories.index, name='categories_index'),
    path('categories/store',categories.store, name='categories_store'),
    path('categories/delete/<int:id>',categories.delete, name='categories_delete'),
    path('categories/update',categories.update, name='categories_update'),
    path('categories/edit/<int:id>',categories.edit, name='categories_edit'),
    
   
    
    

]
