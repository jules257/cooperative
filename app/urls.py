from django.contrib import admin
from django.urls import path
from app.views import home,categories,cooperatives,users




urlpatterns = [
    path('',home.index, name='home'),
    
    path('categories/',categories.index, name='categories_index'),
    path('categories/store',categories.store, name='categories_store'),
    path('categories/delete/<int:id>',categories.delete, name='categories_delete'),
    path('categories/update',categories.update, name='categories_update'),
    path('categories/edit/<int:id>',categories.edit, name='categories_edit'),
    
    
    
    path('cooperatives/',cooperatives.index, name='cooperatives_index'),
    path('cooperatives/store',cooperatives.store, name='cooperatives_store'),
    path('cooperatives/delete/<int:id>',cooperatives.delete, name='cooperatives_delete'),
    path('cooperatives/update',cooperatives.update, name='cooperatives_update'),
    path('cooperatives/edit/<int:id>',cooperatives.edit, name='cooperatives_edit'),
    
    
    
    path('users/', users.index, name='users_index'),
    path('login/', users.user_login, name='users_login'),
    path('register/', users.register, name='users_register'),
    path('users/store', users.store, name='users_store'),
    path('logout/', users.user_logout, name='logout'),
    
    

    
   
    
    

]
