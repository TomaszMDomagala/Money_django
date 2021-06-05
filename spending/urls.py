from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'spendings', views.SpendingViewSet)

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('api/', include(router.urls)),
    path('<uuid:uuid>', views.SpendingDetailView.as_view(), name='spending_detail'),
    path('add', views.CreateSpendingView.as_view(), name='new_spending'),
    path('<uuid:uuid>/update', views.SpendingUpdateView.as_view(), name='update_spending'),
    path('<uuid:uuid>/delete', views.SpendingDeleteView.as_view(), name='delete_spending'),
    path('about', views.SpendingAboutView, name='about_spending')
]
