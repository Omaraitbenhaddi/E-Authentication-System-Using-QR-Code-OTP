from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = ''
admin.site.site_title = ''
admin.site.index_title = ''

urlpatterns = [



    re_path(r'^admin/', admin.site.urls),
    re_path(r'api/', include('accounts.urls', namespace='account')),



   
]

