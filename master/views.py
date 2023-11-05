from django.http import JsonResponse
from django.core import serializers
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import EnquiryForm

def home_view(request):
    form = EnquiryForm()

    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            subject = f'New Enquiry by: {enquiry.name}'
            message = f'Name: {enquiry.name}\nEmail: {enquiry.email}\nMobile Number: {enquiry.mobile_number}\nTopic: {enquiry.message}'
            from_email = 'sbhatkar1994@gmail.com'
            recipient_list = ['sbhatkar1994@gmail.com']

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Return a JSON response to indicate a successful submission
            return JsonResponse({'success': True})
        else:
            # Form is invalid, return the form errors as JSON
            errors = {}
            for field, messages in form.errors.items():
                errors[field] = [str(message) for message in messages]
            return JsonResponse({'success': False, 'errors': errors})

    return render(request, 'index.html', {'form': form})