from django.core import serializers
from question.models import QuestionModel
from question.serializer import QuestionSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Get_Question(APIView):
    def get(self, request, id) -> Response:
        question_id = id
        question_exist: bool = QuestionModel.objects.filter(id=question_id).exists()
        if question_exist:
            question: QuestionModel = QuestionModel.objects.filter(
                id=question_id
            ).values()
            # question_json = serializers.serialize("json", question)
            return Response(question)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class List_Question(APIView):
    def get(self, request) -> Response:
        questions: QuestionModel = QuestionModel.objects.all().values()
        return Response(questions)


class Create_Question(APIView):
    """
    For creating question.
    """

    def post(self, request) -> Response:
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class Update_Question(APIView):
    """
    For updating question with an id.
    """

    def post(self, request) -> Response:
        question_id = request.data["id"]
        question_exist: bool = QuestionModel.objects.filter(id=question_id).exists()
        if question_exist:
            question: QuestionModel = QuestionModel.objects.get(id=question_id)
            serializer = QuestionSerializer(question, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class Delete_Question(APIView):
    def post(self, request) -> Response:
        question_id: str = request.data["id"]
        question_exist: bool = QuestionModel.objects.filter(id=question_id).exists()
        if question_exist:
            question: QuestionModel = QuestionModel.objects.get(id=question_id)
            question.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
