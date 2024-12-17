from django.shortcuts import render
from .models import MasterClass, Comments
# Create your views here.
def masterClasses(request):
    context = {}
    context['masterClasses'] = MasterClass.objects.all()
    return render(request, "masterClasses/allClasses.html", context=context)

def masterClass(request, id):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comments.objects.create(comment=comment, masterClass=MasterClass.objects.get(id=id))
        
    context = {
        'masterClass':MasterClass.objects.get(id=id),
        'comments':Comments.objects.all()
    }
   

    return render(request, "masterClasses/masterClass.html", context=context)