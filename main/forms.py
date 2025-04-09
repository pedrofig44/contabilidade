from django import forms
from .models import ContactRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Seu Nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Seu Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Seu Telemóvel (9 dígitos)'}),
            'subject': forms.Select(attrs={'class': 'form-control', 'id': 'subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'placeholder': 'Deixe sua mensagem aqui', 'style': 'height: 150px'}),
        }
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) != 9:
            raise forms.ValidationError('O telemóvel deve conter exatamente 9 dígitos.')
        return phone