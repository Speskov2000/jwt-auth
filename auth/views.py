from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class AboutView(APIView):
    """
    Представление для отправки api и проверки функционала аутентификации
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        text = (
            "Lorem ipsum dolor sit amet consectetur, adipisicing elit. "
            "Ipsa quibusdam, hic non dolor facere nulla quidem aut "
            "excepturi rem,dolores quos laboriosam earum necessitatibus "
            "facilis commodirepellendus sit nobis sequi."
        )

        return Response({'key': text})
