from django.shortcuts import render
from .models import get_random_text
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .forms import TemplateForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from django.views.generic import TemplateView, FormView


class MyFormView(FormView):
    template_name = 'app/template_form.html'  # Шаблон, который будет рендерится
    form_class = TemplateForm  # Класс формы который будет валидироваться
    success_url = '/'  # Ссылка для перехода при удачной валидации

    def form_valid(self, form):
        return JsonResponse(form.cleaned_data)


class MyTemplView(TemplateView):
    template_name = 'app/template_form.html'

    def post(self, request, *args, **kwargs):
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            my_text = form.cleaned_data.get("my_text")  # Получили очищенные данные
            my_email = form.cleaned_data.get("my_email")
            my_password = form.cleaned_data.get("my_password")
            my_birthday = form.cleaned_data.get("my_birthday")
            my_age = form.cleaned_data.get("my_age")
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")
            my_accept = form.cleaned_data.get("my_accept")
            return JsonResponse(form.cleaned_data)

        context = self.get_context_data(**kwargs)  # Получаем контекст, если он есть
        context["form"] = form  # Записываем в контекст форму
        return self.render_to_response(context)  # Возвращаем вызов метода render_to_response


class TemplView(View):
    def get(self, request):
        return render(request, 'app/template_form.html')

    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            my_text = form.cleaned_data.get("my_text")  # Получили очищенные данные
            my_email = form.cleaned_data.get("my_email")
            my_password = form.cleaned_data.get("my_password")
            my_birthday = form.cleaned_data.get("my_birthday")
            my_age = form.cleaned_data.get("my_age")
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")
            my_accept = form.cleaned_data.get("my_accept")
            return JsonResponse(form.cleaned_data)

        return render(request, 'app/template_form.html', context={"form": form})

def template_view(request):
    if request.method == "GET":
        return render(request, 'app/template_form.html')

    if request.method == "POST":
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            my_text = form.cleaned_data.get("my_text")  # Получили очищенные данные
            my_email = form.cleaned_data.get("my_email")
            my_password = form.cleaned_data.get("my_password")
            my_birthday = form.cleaned_data.get("my_birthday")
            my_age = form.cleaned_data.get("my_age")
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")
            my_accept = form.cleaned_data.get("my_accept")
            return JsonResponse(form.cleaned_data)

        return render(request, 'app/template_form.html', context={"form": form})


def login_view(request):
    if request.method == "GET":
        return render(request, 'app/login.html')

    # if request.method == "POST":
    #     data = request.POST
    #     user = authenticate(username=data["username"], password=data["password"])
    #     if user:
    #         login(request, user)
    #         return redirect("app:user_profile")
    #     return render(request, "app/login.html", context={"error": "Неверные данные"})

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("app:user_profile")
        return render(request, "app/login.html", context={"form": form})


def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")


def register_view(request):
    if request.method == "GET":
        return render(request, 'app/register.html')

    # if request.method == "POST":
    #     return render(request, 'app/register.html')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Возвращает сохраненного пользователя из данных формы
            login(request, user)
            return redirect("app:user_profile")

        return render(request, 'app/register.html', context={"form": form})


def reset_view(request):
    if request.method == "GET":
        return render(request, 'app/reset.html')

    if request.method == "POST":
        return render(request, 'app/register.html')


def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("app:user_profile")
        return render(request, 'app/index.html')


def user_detail_view(request):
    if request.method == "GET":
        return render(request, 'app/user_details.html')

def get_text_json(request):
    if request.method == "GET":
        return JsonResponse({"text": get_random_text()},
                            json_dumps_params={"ensure_ascii": False})

