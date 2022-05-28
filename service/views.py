from django.shortcuts import render, get_object_or_404
from .models import Service
from .forms import ServiceForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Service


def service_list(request):
    services = Service.objects.all()
    return render(request, 'service/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service/service_detail.html', {'service': service})

@login_required
def service_new(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm()
    return render(request, 'service/service_edit.html', {'service_form': form})

@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save(commit=False)
            service.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service/service_edit.html', {
        'service_form': form})

