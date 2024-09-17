from django.shortcuts import render, get_object_or_404

from .models import Phone


def phone_list_view(request):
    phone_objects = Phone.objects.all()
    return render(request, "phone_list.html", {'phone_objects': phone_objects})

def phone_detail_view(request, id):
    phone_detail = get_object_or_404(Phone, id=id)
    return render(request, "phone_detail.html", {"phone_detail": phone_detail})