from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .models import Phone, CommentPhone
from phone.forms import PhoneForm, CommentFrom
from django.http import HttpResponse


# предварительный просмотр
def phone_list_view(request):
    phone_objects = Phone.objects.all()
    return render(request, "phone_list.html", {'phone_objects': phone_objects})


# детальный просмотр
def phone_detail_view(request, id):
    phone_detail = get_object_or_404(Phone, id=id)
    return render(request, "phone_detail.html", {"phone_detail": phone_detail})


# добавление машины
def create_phone_view(request):
    method = request.method
    if method == "POST":
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Смартфон успешно добавлена</h2>")
    else:
        form = PhoneForm()
    return render(request, 'create_phone.html', {"form": form})


# Обновление Смартфона
def update_object_view(request, id):
    phone_object = get_object_or_404(Phone, id=id)
    if request.method == "POST":
        form = PhoneForm(instance=phone_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Смартфон успешно обновлена</h2>")
    else:
        form = PhoneForm(instance=phone_object)
        return render(request, 'update_phone.html', {"form": form,
                                                     "object": phone_object
                                                     })

# удаление смартфона
def delete_object_view(request, id):
    phone_object = get_object_or_404(Phone, id=id)
    phone_object.delete()
    return HttpResponse("<h2>Смартфон успешно удалена из базы данных</h2>")



# Оставит Комментарии
class PhoneCommentView(CreateView):
    template_name = 'phone_comment.html'
    form_class = CommentFrom
    queryset = CommentPhone.objects.all()
    success_url = '/phone_list/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get("id")

    def form_valid(self, form):
        print(form.clean)
        return super(PhoneCommentView, self).form_valid(form=form)