from .models import Question
from django.forms import ModelForm

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['total_savings', 'rent', 'electricity', 'gas', 'water', 'transport', 'internet', 'mobile', 'food', 'clothes', 'other', 'freq_rent', 'freq_elec', 'freq_gas', 'freq_water', 'freq_internet', 'freq_mobile', 'freq_food', 'freq_clothes', 'freq_transport','freq_other']
