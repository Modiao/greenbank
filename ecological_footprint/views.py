from django.shortcuts import render

from ecological_footprint.utils import total_borrowing_rate

from .forms import InfosVehiculeFoyerForm

def infosvehiculefoyer_view(request):
    if request.method == 'POST':
        form = InfosVehiculeFoyerForm(request.POST)
        if form.is_valid():
            # Extract data from the formula
            type_vehicule = form.cleaned_data['type_vehicule']
            energy = form.cleaned_data['energy']
            mileage = int(form.cleaned_data['mileage'])
            year = int(form.cleaned_data['year'])
            passenger = int(form.cleaned_data['passenger'])

            # Calculate borrowing rate
            borrowing_rate = total_borrowing_rate(type_vehicule, energy, mileage, year, passenger)

            # Save form data with borrowing rate
            instance = form.save(commit=False)
            instance.borrowing_rate = borrowing_rate
            instance.save()

            return render(request, 'index.html', {'form': form, 'borrowing_rate': borrowing_rate})
    else:
        form = InfosVehiculeFoyerForm()

    return render(request, 'index.html', {'form': form})
