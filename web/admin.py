from django.contrib import admin
from web.models import Testimonial,promoter

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display =["name","description","desigination"]
admin.site.register(Testimonial,TestimonialAdmin)


class promoterAdmin(admin.ModelAdmin):
    list_display=["name","image"]

admin.site.register(promoter,promoterAdmin)
