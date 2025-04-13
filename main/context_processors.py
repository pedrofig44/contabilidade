from datetime import datetime

def add_current_date(request):
    """
    Context processor to add current date to all templates.
    """
    return {
        'current_date': datetime.now().strftime('%d/%m/%Y')
    }