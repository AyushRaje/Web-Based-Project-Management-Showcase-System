from django.urls import path
from authentication import views

urlpatterns = [
    path('ping',views.ping,name='ping'),
    path('csrf',views.get_csrf,name='get_csrf'),
    path('create_org',views.create_org,name='create_org'),
    path('generate_referral',views.generate_referral,name='generate_referral'),
    # path('generate_api_key',views.generate_api_key,name='generate_api_key')
]
