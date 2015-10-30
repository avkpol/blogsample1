from django import forms

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length=128,required=True, label="first name" )
	last_name = forms.CharField(max_length=128,required=True, label="last name" )
	email= forms.EmailField(required=True, help_text="please provide valid email")
	comment = forms.CharField(required=True, widget=forms.Textarea) 
	

