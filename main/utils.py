from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_contact_notification(contact_request):
    """
    Send a notification email when a new contact request is received
    
    Args:
        contact_request: The ContactRequest model instance
    """
    mail_subject = f"Novo Pedido de Contacto: {contact_request.get_subject_display()}"
    
    # Prepare context for email template
    context = {
        'name': contact_request.name,
        'email': contact_request.email,
        'phone': contact_request.phone,
        'subject_display': contact_request.get_subject_display(),
        'message': contact_request.message,
        'created_at': contact_request.created_at.strftime('%d/%m/%Y %H:%M'),
    }
    
    # Render the email template with context
    email_content = render_to_string('emails/contact_notification.html', context)
    
    # Recipient email
    to_email = 'marco.duarte@duarama.pt'
    
    # Create and send the email
    mail = EmailMessage(
        subject=mail_subject,
        body=email_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[to_email]
    )
    mail.content_subtype = "html"  # Set content type to HTML
    mail.send()