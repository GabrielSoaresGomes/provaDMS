from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('aluguel.urls')),  # URL principal, que irá ser mostrada ao iniciar o site.
    path('admin/', admin.site.urls),

]
