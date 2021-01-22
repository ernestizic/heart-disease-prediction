from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # For using static files
from django.conf.urls.static import static  # For using static files
from django.conf import settings  # For using media files
from apphome import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctors/', include('doctors.urls')),
    path('accounts/', include('accounts.urls')),
    path('apphome/', include('apphome.urls')),
    path('', home_views.index, name="home"),

]

# static files
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# username = admin
# password = passhnd2
