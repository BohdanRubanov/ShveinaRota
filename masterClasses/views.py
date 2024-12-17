from django.shortcuts import render
from .models import MasterClass
# Create your views here.
def masterClasses(request):
    context = {}
    context['masterClasses'] = MasterClass.objects.all()
    return render(request, "masterClasses/allClasses.html", context=context)

def masterClass(request, id):
    context = {}
    context['masterClass'] = MasterClass.objects.get(id=id)

    return render(request, "masterClasses/masterClass.html", context=context)