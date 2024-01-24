from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('add', add, name='add'),
    path('update/<int:id>', edit, name='update'),
    path('delete/<int:id>', delete, name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

