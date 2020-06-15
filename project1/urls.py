from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path('login',views.login),
    path('loginto',views.loginto),
    path('logout',views.logout),
    path('admin',views.admin_panel),
    path('seniority',views.seniority),
    path('collect',views.collect),
    path('notification',views.notification),
    path('circular',views.circular),
    path('add_seniority',views.add_seniority),
    path('add_notification',views.add_notification),
    path('add_qb',views.add_qb),
    path('add_sl',views.add_sl),
    path('add_questionbank',views.add_questionbank),
    path('attachment/<str:files>',views.attachment),
    path('qb',views.qb),
    # path('action1',views.action1),
    # path('register',views.register),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
