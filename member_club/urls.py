from django.urls import include, path

urlpatterns = [
    path('', include('page.urls')),
]
