from django.urls import path
from .views import TheaterAvailabilityView, CustomUnavailabilityView, SlotView
from . import views
from .views import TheaterCreateView, ScreenCreateView, MovieCreateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Movie Booking System API",
        default_version='v1',
        description="API documentation for the Movie Booking System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('theater/create/', TheaterCreateView.as_view(), name='create-theater'),
    path('screen/create/', ScreenCreateView.as_view(), name='create-screen'),
    path('movie/create/', MovieCreateView.as_view(), name='create-movie'),
    path('theatre/<int:id>/availability/', TheaterAvailabilityView.as_view()),
    path('theatre/<int:id>/custom-unavailability/', CustomUnavailabilityView.as_view()),
    path('theatre/<int:id>/slots/', SlotView.as_view()),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


