from django.urls import path
from .views import ApiListView


urlpatterns = [
    path('list/', ApiListView.as_view()),
]
