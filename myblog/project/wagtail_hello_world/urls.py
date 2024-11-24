from django.contrib import admin
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

urlpatterns = [
    # Django admin path
    path('django-admin/', admin.site.urls),

    # Wagtail admin path
    path('admin/', include(wagtailadmin_urls)),

    # Wagtail document serving
    path('documents/', include(wagtaildocs_urls)),

    # Wagtail frontend pages (default catch-all)
    path('', include(wagtail_urls)),
]
