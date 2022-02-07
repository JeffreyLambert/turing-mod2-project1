from django.shortcuts import render
from django.http import HttpResponse

from .models import VeterinaryOffice

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!  Welcome to to the shelters app.")


def veterinaryoffices(request):
    office_list = VeterinaryOffice.objects.all()
    context = {'office_list': office_list}
    return render(request, "shelters/veterinaryoffices.html", context)
