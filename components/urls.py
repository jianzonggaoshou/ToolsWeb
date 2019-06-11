from django.urls import path

from components.views import ComponentsList


urlpatterns = [
    path('components', view=ComponentsList.as_view()),
]
