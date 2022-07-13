from django.urls import include, path

urlpatterns = [
    path('v1/', include('virtual_bank.urls')),
]
