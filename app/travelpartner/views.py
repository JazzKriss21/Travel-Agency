from django.shortcuts import render,redirect
from . models import TravelPartner
from . forms import TravelPartnerForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import TravelPartner

def travelpartner_form(request):
    if request.method=='POST':
        form=TravelPartnerForm(request.POST)
        print("hh")
        if form.is_valid():
            form=form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('partners-detail')
    else:
        form=TravelPartnerForm()
    context={'form':form}
    return render(request,'travelpartner/details_form.html',context=context)




def view_partners(request):
    list_partners=TravelPartner.objects.all()
    context={'list_partners':list_partners}
    return render(request,'travelpartner/details_view.html',context=context)



def travelpartner(request):
    if request.method=='POST':
        form=TravelPartnerForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('partners-detail')
    else:
        form=TravelPartnerForm()

    return render(request,'travelpartner/travel.html')



class UploadView(CreateView):
    model = TravelPartner
    fields = ['upload_file', ]
    success_url = reverse_lazy('fileupload')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = TravelPartner.objects.all()
        return context