from django.shortcuts import render,redirect
from .models import Fundraiser
from .models import Fundraiser,FundraiserFormModel



def campaign(request):
    objects = Fundraiser.objects.all()
    print(objects)
    context = {'objects':objects}
    return  render(request, 'crowdfund/crowd_campaign.html',context)

# Create your views here.
def crowdfund(request):

    if request.method == "POST":
        form = FundraiserFormModel(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return render(request, 'crowdfund/crowdfund1.html')

        else:
            print(form.errors,form.non_field_errors)
        # name=request.POST.get('title')
        # amount_funded = request.POST.get('amount_funded')
        # amount_goal = request.POST.get('amount_goal')
        # date_goal = request.POST.get('date_goal')
        # date_fin = request.POST.get('date_fin')
        # description = request.POST.get('description')
        # print(name,amount_funded,amount_goal,date_fin,date_goal,description)
        #
        # form = Fundraiser.objects.create(title=name,description=description,date_goal=date_goal,date_finished=date_fin,amount_funded=amount_funded,amount_goal=amount_goal)
        context = {'error':form.errors}
        return render(request, 'crowdfund/crowdfund1.html',context)

    return render(request,'crowdfund/crowdfund1.html')



