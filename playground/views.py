from django.shortcuts import render
from django.http import HttpResponse
import json
import os
from django.conf import settings
# Create your views here.

def read_data(json_path):
    json_path = os.path.join(settings.BASE_DIR, json_path)
    with open(json_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data

def main_page(request):
    info = read_data("playground/static/main_nav.json")
    return render(request, "main.html", {"info": info})

def about(request):
    about_info = read_data("playground/static/about.json")
    return render(request, "about.html", {"about_info": about_info})

def digital_skills(request):
    tech_info = read_data("playground/static/data.json")
    return render(request, "dgskills.html",{"tech_info": tech_info})

def services(request):
    services = read_data("playground/static/services.json")
    return render(request, 'services.html', {'services': services})

def testimonials(request):
    data = read_data("playground/static/testimonials.json")
    return render(request, 'testimonials.html', {'data': data})

def faqs(request):
    faqinfo = read_data("playground/static/testimonials.json")
    return render(request, 'faqs.html', {'faqinfo': faqinfo})
