from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import ColdCoffee



class CoffeePaymentForm(forms.ModelForm):
    class Meta:
        model = ColdCoffee
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'amount',
            Submit("submit", "Buy", css_class="btn btn-primary btn-block")
        )
        
        
   
   
     
        

