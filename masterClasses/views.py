from django.shortcuts import render
from .models import MasterClass, Comments
# Create your views here.
def masterClasses(request):
    context = {}
    context['masterClasses'] = MasterClass.objects.all()
    return render(request, "masterClasses/allClasses.html", context=context)

def masterClass(request, id):
    masterClass = MasterClass.objects.get(id=id)

    if request.method == 'POST':
        comment = request.POST.get('comment')

        Comments.objects.create(comment=comment, master_class=masterClass)

    context = {
        'masterClass': masterClass,
        'comments':  Comments.objects.filter(master_class=masterClass)
    }
    print(context)

    return render(request, "masterClasses/masterClass.html", context=context)