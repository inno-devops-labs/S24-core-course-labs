from django.urls import path
from .views import MoscowTimeView

urlpatterns = [
    path('', MoscowTimeView.as_view(), name='moscow_time'),
]