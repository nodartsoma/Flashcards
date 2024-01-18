from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Flashcard
from .serializers import FlashcardSerializer


class CardListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlashcardSerializer

    def get(self, request):
        flashcards = request.user.cards.all()
        serializer = self.serializer_class(instance=flashcards, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class CardSingletonView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlashcardSerializer

    def get(self, request, pk):
        flashcard = get_object_or_404(Flashcard, pk=pk)
        serializer = self.serializer_class(instance=flashcard)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        flashcard = get_object_or_404(Flashcard, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=flashcard, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        flashcard = get_object_or_404(Flashcard, pk=pk)
        flashcard.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

