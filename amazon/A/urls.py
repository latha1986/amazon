from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('prod/<int:category_id>/', views.prod, name='prod'),
    path('display_image/<int:id>/', views.display_image, name='display_image'),
    path('account/',views.account,name="account"),
    path('cart/',views.cart,name="cart"),
]