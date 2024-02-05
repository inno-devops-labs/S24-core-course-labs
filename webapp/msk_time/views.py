from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from datetime import datetime
import pytz


class MoscowTimeView(View):
    def get(self, request, *args, **kwargs):
        moscow_tz = pytz.timezone('Europe/Moscow')

        moscow_time = datetime.now(moscow_tz)

        formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S %Z')

        return JsonResponse({'moscow_time': formatted_time})