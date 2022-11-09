
from django.urls import path

from squaring.views import SquaringView, HelloWorldView

urlpatterns = [
    path('<int:number>', SquaringView.as_view(), name='home'),
    path('/', HelloWorldView.as_view()),
]
