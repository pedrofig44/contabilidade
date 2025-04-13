from django.db import models

class ContactRequest(models.Model):
    SUBJECT_CHOICES = [
        ('quote', 'Pedir Orçamento'),
        ('question', 'Esclarecer Dúvidas'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=9, verbose_name='Telemóvel')
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, verbose_name='Assunto')
    message = models.TextField(verbose_name='Mensagem')
    gdpr_consent = models.BooleanField(default=False, verbose_name='Consentimento GDPR')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    
    def __str__(self):
        return f"{self.name} - {self.get_subject_display()}"
        
    class Meta:
        verbose_name = 'Pedido de Contacto'
        verbose_name_plural = 'Pedidos de Contacto'