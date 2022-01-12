from django.conf.urls import url
from .views import  contact,cont,CVPAGE,download
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
app_name="mysc"

urlpatterns = [
    path("cv",CVPAGE.as_view(), name='cv'),
    path("",download,name="home"),
    path("contact", contact, name="contact"),
    path("cont", cont, name="cont"),
    url(r"^download/(?P<path>.*)$",serve,{'document_root':settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
