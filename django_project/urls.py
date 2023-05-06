from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
import debug_toolbar
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    #path("accounts/", include("allauth.urls")),
    #re_path(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path("", include("pages.urls")),
    path("__debug__/", include(debug_toolbar.urls))
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
