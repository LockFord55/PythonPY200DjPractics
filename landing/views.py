from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from landing.forms import TemplateForm


# Create your views here.

# class LandFormView(FormView):
#     template_name = 'landing/index.html'
#     form_class = TemplateFormLand
#     success_url = '/'
#
#     def form_valid(self, form):
#         return JsonResponse(form.cleaned_data)

class TemplateView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Получение IP
        else:
            ip = request.META.get('REMOTE_ADDR')  # Получение IP

        user_agent = request.META.get('HTTP_USER_AGENT')

        if form.is_valid():  # Проверили, что данные все валидные
            dict_form = dict(form.cleaned_data)
            dict_form["ip"] = ip
            dict_form["user_agent"] = user_agent
            return JsonResponse(dict_form)

        return render(request, 'landing/index.html', context={"form": form})