from django.urls                import path, include
from .                          import views
from rest_framework             import routers
from rubik                      import views

router = routers.DefaultRouter()
router.register(r'times', views.TimesViewSet)

urlpatterns = [
    path('', views.RubikViews.as_view(), name='rubiks'),
    path('api/', include(router.urls)),
]
