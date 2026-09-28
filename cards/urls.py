from django.urls import path
from .views import AddCardView, ViewCardsView, DeleteCardView

urlpatterns = [
    path('add-card/', AddCardView.as_view(), name='add-card'),
    path('view-cards/', ViewCardsView.as_view(), name='view-cards'),
    path('delete-card/<int:pk>/', DeleteCardView.as_view(), name='delete-card'),
]