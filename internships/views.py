from django.shortcuts import render
from .models import Internship

def internship_list(request):
    internships = Internship.objects.all()
    return render(request, 'internship_list.html', {'internships': internships})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Internship, Application

def apply_internship(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)

    if request.method == 'POST':
        Application.objects.create(
            internship=internship,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            resume=request.FILES.get('resume')
        )
        
        return redirect('application_success')

    return render(request, 'apply_internship.html', {'internship': internship})

from django.shortcuts import render

def application_success(request):
    return render(request, 'internships/success.html')
