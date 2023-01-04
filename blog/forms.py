from django.db import models
from django import forms
from .models import PostModel
# class PostForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     body = forms.CharField(
#         widget = forms.Textarea
#     )
#     category = forms.CharField(max_length=20)

#     def clean_judul(self):
#         judul_input = self.cleaned_data.get('judul')

#         if judul_input == "Rasis":
#             raise forms.ValidationError("Rasis tidak boleh diposting")
#         return judul_input

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'author',
            'judul',
            'body',
            'category',
        ]

        widgets={
            'author': forms.TextInput (
                attrs = {
                    'class' : 'form',
                    'placeholder' : 'Masukkan Author',
                }
            )
        }
