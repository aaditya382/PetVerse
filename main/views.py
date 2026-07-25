from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def pets(request):
    return render(request, 'pets.html')


def shop(request):
    return render(request, 'shop.html')


def medicines(request):
    return render(request, 'medicines.html')


def adoption(request):
    return render(request, 'adoption.html')


def contact(request):
    return render(request, 'contact.html')


def login_view(request):
    return render(request, 'login.html')


def appointments(request):

    if request.method == "POST":

        owner_name = request.POST.get('owner_name')
        email = request.POST.get('email')
        pet_name = request.POST.get('pet_name')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')

        try:
            send_mail(
                'PetVerse Appointment Confirmed 🐾',
                f'''
Hello {owner_name},

Your appointment has been booked successfully.

Pet Name: {pet_name}
Doctor: {doctor}
Date: {date}

Thank you for choosing PetVerse ❤️
''',
                None,
                [email],
                fail_silently=True,
            )
        except Exception:
            pass

    return render(request, 'appointments.html')