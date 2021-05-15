from django.urls                import path, include
from .                          import views
from rest_framework             import routers
from snkrs                      import views

router = routers.DefaultRouter()
router.register(r'account', views.AccountViewSet)
router.register(r'snkr', views.SnkrViewSet)

urlpatterns = [
    path('', views.snkrs, name='snkrs'),
    path('api/', include(router.urls)),
]