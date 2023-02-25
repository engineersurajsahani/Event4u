from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home,register_view,login_view,logout_view,dashboard,events,event_data,volunteer,participant,audience,payment,report,generatereport,generate_pass,generate_qr
urlpatterns = [
    path('',home,name='home'),
    path('dashboard/',dashboard,name='dashboard'),
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('events/',events,name='events'),
    path('event_data/<int:pid>',event_data,name='event_data'),
    path('volunteer/',volunteer,name='volunteer'),
    path('participant/',participant,name='participant'),
    path('audience/',audience,name='audience'),
    path('payment/',payment,name='payment'),
    path('report/',report,name='report'),
    path('generatereport/<int:pid>/',generatereport,name='generatereport'),
    path('qr/', generate_qr, name='generate-qr'),
    path('event/<int:event_id>/generate-pass/', generate_pass, name='generate-pass'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
