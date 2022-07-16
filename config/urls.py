"""This module sets the url paths for each app in the project
"""

from django.urls import include, path

urlpatterns = [
    path('v1/', include('virtual_bank.urls')),
]
