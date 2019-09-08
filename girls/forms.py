from django import forms
from .models import Girl

class GirlForm(forms.ModelForm):
	class Meta:
		model = Girl
		fields = ['name','race']