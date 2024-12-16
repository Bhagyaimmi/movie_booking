from django.urls import path
from .views import TheaterAvailabilityView, CustomUnavailabilityView, SlotView
from . import views
from .views import TheaterCreateView, ScreenCreateView, MovieCreateView
urlpatterns = [
    path('theater/create/', TheaterCreateView.as_view(), name='create-theater'),
    path('screen/create/', ScreenCreateView.as_view(), name='create-screen'),
    path('movie/create/', MovieCreateView.as_view(), name='create-movie'),
    path('theatre/<int:id>/availability/', TheaterAvailabilityView.as_view()),
    path('theatre/<int:id>/custom-unavailability/', CustomUnavailabilityView.as_view()),
    path('theatre/<int:id>/slots/', SlotView.as_view()),
]
