from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('about.html', views.about),
    path('dgskills.html', views.digital_skills),
    path('services.html', views.services),
    path('testimonials.html', views.testimonials),
    path('faqs.html', views.faqs)
]