from django.shortcuts import render

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