from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # This data variable will contain refresh and access tokens
        data = super().validate(attrs)
        # You can add more User model's attributes like username,email etc.
        # in the data dictionary like this.
        data['user_name'] = self.user.username
        data['user_id'] = self.user.id
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    # serializer_class = CustomTokenObtainPairSerializer
    serializer_class = CustomTokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['name'] = user.username
        # token['email'] = user.email

        return token


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
