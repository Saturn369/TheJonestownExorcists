from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactFormSubmission

def home(request):
    return render(request, 'homepage/index.html')

def About(request):
    return render(request, 'homepage/About.html')

def Services(request):
    return render(request, 'homepage/Services.html')

def Contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to the database using the model
            submission = ContactFormSubmission(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            submission.save()
            return redirect('success_page')
    else:
        form = ContactForm()
    return render(request, 'homepage/Contact.html', {'form': form})

def Redirect(request):
    return render(request, 'homepage/redirect_page.html')

