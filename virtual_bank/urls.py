"""This module sets the url paths for each ViewSet in the API, the admin site and
the main path
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from virtual_bank.views import (
    AccountViewSet,
    CustomerViewSet,
    TransactionViewSet,
    AccountsByCustomerView,
    TransactionsByAccountView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Virtual Bank API",
        default_version='v1',
        description="Virtual Bank REST API that makes possible to insert, update, consult "
        "and exclude the customers data (natural or juridical person) in the database; "
        "to create, update and consult the bank accounts data (including the current balance); "
        "and to insert, exclude and consult, including for specific periods, the transactions "
        "made by the accounts. It's also possible to consult all the accounts from one same "
        "customer, and all the transactions from one same account. ",
        contact=openapi.Contact(email="thainaralf@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[]
)

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'account', AccountViewSet)
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('customer/<int:pk>/accounts/', AccountsByCustomerView.as_view()),
    path('account/<int:pk>/transactions/', TransactionsByAccountView.as_view()),
    path('swagger.json/', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
