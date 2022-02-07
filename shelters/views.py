from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import VeterinaryOffice, Shelter

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!  Welcome to to the shelters app.")


def veterinaryoffices(request):
    office_list = VeterinaryOffice.objects.all()
    context = {'office_list': office_list}
    return render(request, "shelters/veterinaryoffices.html", context)


def shelters(request):
    shelters_list = Shelter.objects.all()
    context = {'shelters_list': shelters_list}
    return render(request, "shelters/shelters.html", context)

def shelter_by_id(request, shelter_id):
    shelter = get_object_or_404(Shelter, pk=shelter_id)
    context = {'shelter': shelter}
    return render(request, "shelters/shelter_by_id.html", context)
