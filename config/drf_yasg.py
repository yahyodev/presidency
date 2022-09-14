from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="English Lessons API",
        default_version='v1',
        description="This is documentation for English Lessons",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="y.abdunazarov@uicgroup.org"),
        license=openapi.License(name="None"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
