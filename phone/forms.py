from django import forms
from .models import Phone, CommentPhone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"


class CommentFrom(forms.ModelForm):
    class Meta:
        model = CommentPhone
        fields = "__all__"
