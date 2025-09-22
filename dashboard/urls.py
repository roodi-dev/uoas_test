from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.manager_login, name='dashboard_login'),
    path('logout/', views.manager_logout, name='dashboard_logout'),
    path('', views.dashboard_home, name='dashboard_home'),
    path('products/', views.product_list, name='dashboard_product_list'),
    path('products/add/', views.product_add, name='dashboard_product_add'),
    path('products/<int:pk>/edit/', views.product_edit, name='dashboard_product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='dashboard_product_delete'),

    # Slide management
    path('slides/', views.slide_list, name='dashboard_slide_list'),
    path('slides/add/', views.slide_add, name='dashboard_slide_add'),
    path('slides/<int:pk>/edit/', views.slide_edit, name='dashboard_slide_edit'),
    path('slides/<int:pk>/delete/', views.slide_delete, name='dashboard_slide_delete'),

    # QuotationRequest management
    path('quotation-requests/', views.quotationrequest_list, name='dashboard_quotationrequest_list'),
    path('quotation-requests/<int:pk>/', views.quotationrequest_detail, name='dashboard_quotationrequest_detail'),
    path('quotation-requests/<int:pk>/delete/', views.quotationrequest_delete, name='dashboard_quotationrequest_delete'),

    # Team management
    path('team/', views.team_list, name='dashboard_team_list'),
    path('team/add/', views.team_add, name='dashboard_team_add'),
    path('team/<int:pk>/edit/', views.team_edit, name='dashboard_team_edit'),
    path('team/<int:pk>/delete/', views.team_delete, name='dashboard_team_delete'),
]
