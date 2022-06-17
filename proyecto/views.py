from pickletools import read_unicodestring4
from xml.sax.handler import property_declaration_handler
from django.shortcuts import render
from .models import familiar
# Create your views here.

def index(request):
    Familiar = familiar.objects.all()
    ctx = {"familiar": familiar, }
    return render (request, "proyecto/index.html", ctx)