from django.urls import path
from test_two.bincomapp import views

urlpatterns = [
    path('index/', views.bincompage, name='page'),
    path('total-votes/', views.totalScore, name="total_votes"),
    path('add_polling_unit_result/', views.add_polling_unit_result, name='add_polling_unit_result'),
]