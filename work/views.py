from django.shortcuts import render
from .models import Work

# Create your views here.
def homework(request):
    engineer = Work.objects.filter(work="Engineer")
    dev27 = Work.objects.filter(work="Developer", age__gte = 27)
    p1991 = Work.objects.filter(birthday_date__year=1991)
    return render(request, 'correctionmodel/work/work.html', {"engineer":engineer, "devs": dev27, "p1991": p1991})