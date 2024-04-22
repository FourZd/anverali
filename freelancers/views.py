from django.shortcuts import render
from .models import Freelancer

def freelancer_profile(request, id):
    freelancer = Freelancer.objects.get(id=id)
    return render(request, 'freelancers/profile.html', {'freelancer': freelancer})