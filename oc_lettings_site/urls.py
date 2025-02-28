from django.contrib import admin
from django.urls import include, path
from oc_lettings_site import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]

handler404 = 'oc_lettings_site.views.error_404'
handler500 = 'oc_lettings_site.views.error_500'
