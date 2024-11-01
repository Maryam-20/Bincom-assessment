from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Lga, AnnouncedPuResults, AnnouncedLgaResults
from .forms import Lga_form, modelformset_factory

# Create your views here.

def bincompage(request):
    polling_result  = AnnouncedPuResults.objects.all()
    return render(request, "bincomapp/index.html", {"pollingResult": polling_result})


def totalScore(request):
    local_government = Lga.objects.all()
    total = None
    
    if request.method == "POST":
        select_lga_id = request.POST.get("local_government")
        total  = AnnouncedLgaResults.objects.filter(lga_name = select_lga_id).aggregate(total_votes = sum("vote"))['total_votes']
    return render(request, "bincomapp/lga_votes.html", {"local_government": local_government, "total": total,})
    
def add_polling_unit_results(request):
    PollingUnitResultFormSet = modelformset_factory(AnnouncedPuResults, fields=('polling_unit', 'party', 'votes'))
    if request.method == 'POST':
        formset = PollingUnitResultFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('success')  # Redirect to a success page
    else:
        formset = PollingUnitResultFormSet(queryset=AnnouncedPuResults.objects.none())
    
    return render(request, 'add_polling_unit_result.html', {'formset': formset})
   
    
    
    
    