from django.contrib import admin
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),  # Wagtail admin interface
    path('documents/', include(wagtaildocs_urls)),
    path('', include(wagtail_urls)),  # Wagtail front-end routing
]

