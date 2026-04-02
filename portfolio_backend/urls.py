from django.contrib import admin
from django.urls import path, include
from contact.views import portfolio   

urlpatterns = [
    path('', portfolio), 
    path('admin/', admin.site.urls),
    path('api/contact/', include('contact.urls')),
    path('api/projects/', include('projects.urls')),
]