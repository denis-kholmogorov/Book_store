from django.urls import path

from .views import HomePageView, AboutPagesView

urlpatterns = [
    path('about/', AboutPagesView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home')

]