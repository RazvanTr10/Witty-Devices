from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_and_conditions/', views.terms_and_conditions,
         name='terms_and_conditions'),
    path('refunds_and_returns', views.refunds_and_returns,
         name='refunds_and_returns'),
]
