from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showmain, name="showmain"),
    path('<str:id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/',views.create, name="create"),
    path('search/',views.search, name="search"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)