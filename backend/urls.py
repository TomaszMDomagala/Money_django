from django.contrib             import admin
from django.urls                import path, include
from django.views.generic       import RedirectView
from django.conf                import settings
from django.conf.urls.static    import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spending/', include('spending.urls')),
    path('snkrs/', include('snkrs.urls')),
    path('', RedirectView.as_view(url='spending/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)