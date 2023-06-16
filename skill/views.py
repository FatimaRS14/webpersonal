from django.shortcuts import render
from .models import Acerca

# Create your views here.
def skill(request):

    skill = Acerca.objects.all()
    return render(request, "skill/about.html", {'skill': skill})
    