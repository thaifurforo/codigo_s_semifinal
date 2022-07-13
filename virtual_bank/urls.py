from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from virtual_bank.views import AccountViewSet, CustomerViewSet, TransactionViewSet, AccountsByCustomerView, TransactionsByAccountView

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'account', AccountViewSet)
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('customer/<int:pk>/accounts/', AccountsByCustomerView.as_view()),
    path('account/<int:pk>/transactions/', TransactionsByAccountView.as_view())
]
