from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': "text",
        'name': "res_name",
        'class': "form-control shadow-0 px-0 border-0 border-bottom",
        'id': "resName",
        'required': "",
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': "email",
        'name': "res_email",
        'class': "form-control shadow-0 px-0 border-0 border-bottom",
        'id': "resEmail",
        'required': "",
    }))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'type': "number",
        'name': "res_number",
        'class': "form-control shadow-0 px-0 border-0 border-bottom",
        'id': "resNumber",
        'required': "",
    }))
    number_of_people = forms.IntegerField(widget=forms.TextInput(attrs={
        'type': "number",
        'name': "res_people",
        'class': "form-control shadow-0 px-0 border-0 border-bottom",
        'id': "resPeople",
        'required': "",
    }))
    date_and_time = forms.DateTimeField(widget=forms.TextInput(attrs={
        'type': "datetime-local",
        'name': "res_date_and_time",
        'class': "form-control shadow-0 px-0 border-0 border-bottom",
        'id': "resDateAndTime",
        'required': "",
    }))
    message = forms.CharField(max_length=250, widget=forms.Textarea(attrs={
        'class': "form-control shadow-0 px-0 border-0 border-bottom",
        'id': "request",
        'name': "res_request",
        'rows': "7",
        'required': "",
        'placeholder': "Message",
    }))

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'number_of_people', 'date_and_time', 'message']