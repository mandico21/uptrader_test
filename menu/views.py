from django.shortcuts import render
from django.views import View

from menu.models import Menu


class MenuView(View):

    def get(self, request, **kwargs):
        return render(request, 'menu/base.html', {'menu': Menu.objects.all()})
