from django import forms
from test_two.bincomapp.models import Lga, AnnouncedPuResults
from django.forms import modelformset_factory





class Lga_form(forms.ModelForm):
    lgName = [
        ("fhgjgj", "xgchvhnnvv"), 
        ("cfhjvcvc", "vhfjgfhgjgj"),
    ]
    lga_name = forms.ChoiceField(label = "Local Government", required=False)
    
    
    class Meta:
        model = Lga
        fields = [
            "lga_name",
        ] 

class PollingUnitResultForm(forms.ModelForm):
    class Meta:
        model = AnnouncedPuResults
        fields = ["party_abbreviation", "party_score"]



PollingUnitResultFormSet = modelformset_factory(AnnouncedPuResults, fields=('party_abbreviation', ' party_score'))

