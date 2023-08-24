from django.urls import path
from .views import SorovApiView

urlpatterns = [
     path('', SorovApiView.as_view()),
]