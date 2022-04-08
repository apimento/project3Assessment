from django.shortcuts import render , redirect
import os  
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from .forms import WidgetForm
from .models import Widgets 


class WidgetDelete(DeleteView): 
    model = Widgets 
    success_url = "/"


def home(request):
    widgets = Widgets.objects.all()
    print(widgets)
    widget_form = WidgetForm()
    if widget_form.is_valid(): 
        new_widget = widget_form.save(commit=False)
        new_widget.save()
    return render(request, 'html.html', {'widgets': widgets , "widget_form":widget_form }) 

def add_widget(request): 
    print(request.POST)
    widgets = Widgets.objects.all()
    form = WidgetForm(request.POST)  
    
    if form.is_valid(): 
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('/')  

# def delete_widget(request, widget_id): 
#     Widgets.objects.delete(id=widget_id)
#     return redirect('/')


# Create your views here.
