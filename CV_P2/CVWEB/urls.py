from .views import contact
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name="mysc"

urlpatterns = [

    path("",contact,name="cv"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
