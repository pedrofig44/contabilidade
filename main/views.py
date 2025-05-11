from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .utils import send_contact_notification

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
            # Save form data to database
            contact_request = form.save()
            
            # Send email notification
            try:
                send_contact_notification(contact_request)
                messages.success(request, 'Seu pedido foi enviado com sucesso. Entraremos em contato em breve.')
            except Exception as e:
                # Log the error but don't show technical details to user
                print(f"Error sending email: {e}")
                messages.warning(request, 'Seu pedido foi registrado, mas houve um problema ao enviar a notificação por email. Nossa equipe entrará em contato mesmo assim.')
            
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