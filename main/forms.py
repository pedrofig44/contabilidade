from django import forms
from .models import ContactRequest

class ContactForm(forms.ModelForm):
    gdpr_consent = forms.BooleanField(
        required=True,
        label='',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input me-2'}),
        error_messages={'required': 'É necessário concordar com o processamento dos seus dados para prosseguir.'}
    )
    
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'phone', 'subject', 'message', 'gdpr_consent']
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