from django.conf.urls import url
from django.contrib import admin

from homepage import views as homepage_views
from karyawan import views as karyawan_views
from kehadiran import views as kehadiran_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', karyawan_views.profil),
    url(r'^login/', homepage_views.login_view),
    url(r'^logout/', homepage_views.logout_view),
    url(r'^daftar_hadir/', kehadiran_views.daftar_hadir),
]
