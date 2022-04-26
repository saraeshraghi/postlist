from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ranking/<int:pk>', views.RankingView.as_view(), name='ranking')
    # path('api_token/', auth_token.obtain_auth_token)
]
