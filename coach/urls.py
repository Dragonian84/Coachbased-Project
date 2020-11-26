from django.urls import path
from .import views
# from .models import 

urlpatterns = [  
    path('',views.dashboard),
    path('profile/',views.profile),
    path('upcoming/',views.upcoming),
    path('history/',views.history),
    path('availability/',views.availability),
    # path('afterlogin/',views.afterlogin),
    # path('afterrevert/',views.afterrevert),
]