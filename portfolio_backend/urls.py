from django.contrib import admin
from django.urls import path, include
from contact.views import index   

urlpatterns = [
    path('', index), 
    path('admin/', admin.site.urls),
    path('api/contact/', include('contact.urls')),
    path('api/projects/', include('projects.urls')),
]