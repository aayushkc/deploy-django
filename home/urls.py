from django.urls import path
from .views import home, about,contact

urlpatterns = [
    path("", view=home, name='home' ),
    path("about", view=about, name='about'),
    path("contact", view=contact, name="contact")
]