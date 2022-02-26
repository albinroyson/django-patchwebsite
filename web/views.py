from django.shortcuts import render
from web.models import Testimonial,promoter

# Create your views here.
def index(request):
    testimonials =Testimonial.objects.all()
    promoters=promoter.objects.all()
    context ={
        "testimonials":testimonials,
        "promoters": promoters
    }
    return render(request,"index.html",context=context)