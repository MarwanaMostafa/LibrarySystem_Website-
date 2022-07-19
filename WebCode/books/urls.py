from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.borrowing, name='book'),
    path('', views.books, name='books'),
    path('extendPeriod/<int:pk>/', views.extendPeriod, name='extendPeriod'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]