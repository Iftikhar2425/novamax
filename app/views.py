from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings  # Import settings to access EMAIL_HOST_USER

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def do(request):
    return render(request, 'do.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=f'Contact Form Submission from {name}',
                    message=f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}',
                    from_email=settings.EMAIL_HOST_USER,  
                    recipient_list=['iftikharalisyed001@gmail.com'], 
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                messages.error(request, f'Error sending email: {e}')
                print(f'Email error: {e}')

           
            form = ContactForm()
        else:
            messages.error(request, 'There was an error. Please check your input.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
