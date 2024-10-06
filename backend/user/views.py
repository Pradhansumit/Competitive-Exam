from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializer import UserSerializer


class Create_User(APIView):
    def post(self, request) -> Response:
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class Login_View(APIView):
    def post(self, request):
        try:
            if request.method == "POST":
                user_name = request.data["user_name"]
                password = request.data["password"]

                user = authenticate(request, username=user_name, password=password)

                if user is not None:
                    login(request, user)
                    return Response(
                        {"message": "Login successful"}, status=status.HTTP_200_OK
                    )
            return Response(status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class Logout_View(APIView):
    def get(self, request) -> Response:
        logout(request)
        return Response({"message": "Logout successful"}, status.HTTP_200_OK)
