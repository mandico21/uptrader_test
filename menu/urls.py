from django.urls import path

from menu.views import MenuView

urlpatterns = [
    path('', MenuView.as_view(), name='item'),
    path('<slug:slug>/<slug:menu_slug>/', MenuView.as_view(), name='menu_item'),
    path('<slug:slug>/', MenuView.as_view(), name='menu'),
]
