from django.shortcuts import render

# Create your views here.

def home_view(request):
    """
    Renders the home page.
    """
    return render(request, 'home/index.html')