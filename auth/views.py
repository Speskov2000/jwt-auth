from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class AboutView(APIView):
    """
    Представление для отправки api и проверки функционала аутентификации
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'key': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsa quibusdam, hic non dolor facere nulla quidem aut excepturi rem, dolores quos laboriosam earum necessitatibus facilis commodi repellendus sit nobis sequi.'})
