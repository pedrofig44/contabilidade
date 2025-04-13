from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def index(request):
    """
    View function for the home page.
    """
    return render(request, 'index.html')

def about(request):
    """
    View function for the about page.
    """
    return render(request, 'about.html')

def contact(request):
    """
    View function for the contact page (orçamento).
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu pedido foi enviado com sucesso. Entraremos em contato em breve.')
            return redirect('contact')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def privacy_policy(request):
    """
    View function for the privacy policy page.
    """
    return render(request, 'legal/privacy_policy.html')

def terms_of_service(request):
    """
    View function for the terms of service page.
    """
    return render(request, 'legal/terms_of_service.html')

def cookie_policy(request):
    """
    View function for the cookie policy page.
    """
    return render(request, 'legal/cookie_policy.html')