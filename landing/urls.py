from django.urls import path
from landing.views import TemplateView

app_name = 'landing'

urlpatterns = [
    path('', TemplateView.as_view(), name='template')
]
