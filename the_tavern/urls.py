"""
URL configuration for the_tavern project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Django AllAuth URLs
    path('', include('home.urls')),  # Home URL
    path('products/', include('products.urls')),  # Products URL
    path('bag/', include('bag.urls')),  # Bag URL
    path('checkout/', include('checkout.urls')),  # Checkout URL
    path('profile/', include('profiles.urls')), # Profiles URL
    path(
        'robots.txt',
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"
        ),
        name='robots.txt'
    ),
    path(
        'sitemap.xml',
        TemplateView.as_view(
            template_name="sitemap.xml",
            content_type="application/xml"
        ),
        name='sitemap'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'the_tavern.views.handler404'
handler500 = 'the_tavern.views.handler500'
handler403 = 'the_tavern.views.handler403'
handler400 = 'the_tavern.views.handler400'