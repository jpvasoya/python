from django import forms

class character_info(forms.Form):
	Name=forms.CharField(max_length=250)
	age=forms.IntegerField()
	desc=forms.CharField(max_length=500)

