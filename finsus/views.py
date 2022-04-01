from django.shortcuts import render
from finsus.forms import QuestionForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            total_savings = form.cleaned_data.get('total_savings')
            rent = form.cleaned_data.get('rent')
            electricity = form.cleaned_data.get('electricity')
            gas = form.cleaned_data.get('gas')
            water = form.cleaned_data.get('water')
            internet = form.cleaned_data.get('internet')
            mobile = form.cleaned_data.get('mobile')
            transport = form.cleaned_data.get('transport')
            food = form.cleaned_data.get('food')
            clothes = form.cleaned_data.get('clothes')
            other = form.cleaned_data.get('other')
            freq_rent = form.cleaned_data.get('freq_rent')
            freq_elec = form.cleaned_data.get('freq_elec')
            freq_gas = form.cleaned_data.get('freq_gas')
            freq_water = form.cleaned_data.get('freq_water')
            freq_internet = form.cleaned_data.get('freq_internet')
            freq_mobile = form.cleaned_data.get('freq_mobile')
            freq_transport = form.cleaned_data.get('freq_transport')
            freq_food = form.cleaned_data.get('freq_food')
            freq_clothes = form.cleaned_data.get('freq_clothes')
            freq_other = form.cleaned_data.get('freq_other')
            rent_perday = rent / freq_rent
            elec_perday = electricity / freq_elec
            gas_perday = gas / freq_gas
            water_perday = water / freq_water
            internet_perday = internet / freq_internet
            mobile_perday = mobile / freq_mobile
            transport_perday = transport / freq_transport
            food_perday = food / freq_food
            clothes_perday = clothes / freq_clothes
            other_perday = other / freq_other
            perday = rent_perday + elec_perday + gas_perday + water_perday + internet_perday + mobile_perday + transport_perday + food_perday + clothes_perday + other_perday
            survival = total_savings / perday
            form.save()
            messages.success(request, "You would survive " + str(round(survival, 0)) + " days")
        else:
            print(form.errors.as_data())
            messages.error(request, "Please enter valid numbers!")
    else:
        form = QuestionForm()
    return render(request, 'finsus/home.html', {'form': form})
