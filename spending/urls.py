from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<uuid:uuid>', views.SpendingDetailView.as_view(), name='spending_detail'),
    path('add', views.CreateSpendingView.as_view(), name='new_spending'),
    path('<uuid:uuid>/update', views.SpendingUpdateView.as_view(), name='update_spending'),
    path('<uuid:uuid>/delete', views.SpendingDeleteView.as_view(), name='delete_spending'),
    path('about/', views.SpendingAboutView, name='about_spending')
]