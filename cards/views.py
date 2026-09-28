from rest_framework import generics, permissions
from .models import Card
from .serializers import CardSerializer


class AddCardView(generics.CreateAPIView):
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        card_number = self.request.data.get('card_number')

        last_four = card_number[-4:]
        masked_card = f"**** **** **** {last_four}"

        serializer.save(
            user=self.request.user,
            masked_card=masked_card,
            last_four_digits=last_four
        )
class ViewCardsView(generics.ListAPIView):
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)


class DeleteCardView(generics.DestroyAPIView):
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)