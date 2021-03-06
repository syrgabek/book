from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
                   path('admin/', admin.site.urls),
                   path('', include(('book.urls', 'book'), namespace='book')),
                   path('', include('book.urls')),
                   path('', include('scrapy.urls')),
               ] + static(settings.STATIC_URL, documet_root=settings.STATIC_ROOT)
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
               )
