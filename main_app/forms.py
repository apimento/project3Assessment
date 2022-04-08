from django.forms import ModelForm
from .models import Widgets 

class WidgetForm(ModelForm): 
    class Meta:
        model = Widgets
        fields = '__all__'  
        success_url= 'html.html'