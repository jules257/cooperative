from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect,render

from app.models import Cooperative,Membre
from app.models import Cooperative,Categorie
from app.forms import CooperativeForm
from django.contrib import messages
from app.filters import CooperativeFilter

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    # permission
    has_perm=False
    if request.user.has_perm('app.delete_cooperative','app.change_cooperative'):
        has_perm = True
 
    assert isinstance(request,HttpRequest)
    
    cooperatives = Cooperative.objects.all()

    membres = Membre.objects.all()

    categories = Categorie.objects.all()
    myfilters = CooperativeFilter(request.GET,queryset=cooperatives)
    cooperatives=myfilters.qs


    # formolaire
    form =CooperativeForm()
    return render(
        request,
        'app/cooperatives/index.html',
        {
            'cooperatives':cooperatives,

            'membres':membres,
            'categories':categories,
            'has_perm':has_perm,
            'myfilters':myfilters,
            'form':form
            
            
        }
    )
    
    
def store(request):
    if request.method == 'POST' :
        form = CooperativeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"cooperative added successfully")
            
            
           
        return redirect('/cooperatives')
    
    
def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = CooperativeForm()
        else:
            cooperative = Cooperative.objects.get(pk=id)
            form = CooperativeForm(instance=cooperative)
        return render(
            request,
            '/cooperatives',
            {
                
                'form':form
            }
        )
def update(request):
    assert isinstance(request,HttpRequest)
    if request.method == "POST" :
        form = CooperativeForm(request.POST)
        cooperative = Cooperative.objects.get(id = request.POST.get('id'))
        form = CooperativeForm(request.POST,instance=cooperative)
        if form.is_valid():
            form.save()
            messages.success(request,"cooperative updated successfully")
            return HttpResponseRedirect("/cooperatives")
         
             
        
   
    
    
def delete(request, id):
    cooperative = Cooperative.objects.get(pk=id)
    cooperative.delete()
    return redirect('/cooperatives')



    



            



    