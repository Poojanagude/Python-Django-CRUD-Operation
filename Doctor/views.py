from django.shortcuts import render, redirect, get_object_or_404
from .forms import DoctorForm
from .models import Doctor

# Create view
def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = DoctorForm()
    return render(request, 'create.html', {'form': form})

# List view
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'list.html', {'doctor_list': doctors})

# Update view
def update_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'update.html', {'form': form})

# Delete view
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('list')
    return render(request, 'delete_confirm.html', {'doctor': doctor})

