import random

from rest_framework import generics, permissions

from .models import Transaction
from .serializers import TransactionSerializer


class MakePaymentView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        payment_status = random.choice(['SUCCESS', 'FAILED'])

        serializer.save(
            user=self.request.user,
            status=payment_status
        )


class TransactionHistoryView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user
        ).order_by('-created_at')
