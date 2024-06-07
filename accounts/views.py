from rest_framework import generics
from .models import MyUser
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
