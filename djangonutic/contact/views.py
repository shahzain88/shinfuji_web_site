from django.shortcuts import render, redirect
from . import model_forms
from .models import Contact
# Create your views here.


def contact_view_list(request):
    contacts = Contact.objects.all().order_by("date")
    return render(request, "contact/contact_view_list.html", {"contacts": contacts})


def contact_view_detail(requeat, slug):
    # return HttpResponse(slug)
    contact = Contact.objects.get(slug=slug)
    return render(requeat, "contact/contact_view_detail.html", {"contact": contact})


def contact_create_list(request):
    if request.method == "POST":
        form = model_forms.CreateContact(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact/contact_thank_you.html")
    else:
        form = model_forms.CreateContact()
    return render(request, "contact/contact_create_list.html", {"form": form})


# def contact_thank_you(request):
#     return render(request, "contact/contact_thank_you.html")
