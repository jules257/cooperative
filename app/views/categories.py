from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect,render
from app.models import Categorie
from app.forms import CategorieForm
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    # permission
    has_perm=False
    if request.user.has_perm('app.delete_categorie','app.change_categorie'):
        has_perm = True
    
 
    assert isinstance(request,HttpRequest)
    
    categories = Categorie.objects.all()
    # formolaire
    form =CategorieForm()
    return render(
        request,
        'app/categories/index.html',
        {
            'categories':categories,
            'has_perm':has_perm,
            'form':form
            
            
        }
    )
    
def store(request):
    if request.method == 'POST' :
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"categorie added successfully")
            
            
           
        return redirect('/categories')
    
    
def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = CategorieForm()
        else:
            categorie = Categorie.objects.get(pk=id)
            form = CategorieForm(instance=categorie)
        return render(
            request,
            '/categories',
            {
                
                'form':form
            }
        )
def update(request):
    assert isinstance(request,HttpRequest)
    if request.method == "POST" :
        form = CategorieForm(request.POST)
        categorie = Categorie.objects.get(id = request.POST.get('id'))
        form = CategorieForm(request.POST,instance=categorie)
        if form.is_valid():
            form.save()
            messages.success(request,"categorie updated successfully")
            return HttpResponseRedirect("/categories")
         
             
        
   
    
    
def delete(request, id):
    categorie = Categorie.objects.get(pk=id)
    categorie.delete()
    return redirect('/categories')



    



            



    