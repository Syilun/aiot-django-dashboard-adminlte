from django.forms import ModelForm
from .models import peoplemove


class OrderForm(ModelForm):
    class Meta:
        model = peoplemove
        fields = '__all__'