from answer.models import AnswerModel
from answer.serializer import AnswerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView, status


class ViewAllAnswers(APIView):
    def get(self, request) -> Response:
        answers = AnswerModel.objects.all().values()
        return Response(answers)


class GetAnswer(APIView):
    def get(self, request, id) -> Response():
        answer_exist: bool = AnswerModel.objects.filter(id=id).exists()
        if answer_exist:
            answer: AnswerModel = AnswerModel.objects.filter(id=id).values()
            return Response(answer, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)


class CreateAnswer(APIView):
    def post(self, request) -> Response:
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteAnswer(APIView):
    def post(self, request) -> Response:
        ans_id: str = request.data["id"]
        answer_exist: bool = AnswerModel.objects.filter(id=ans_id).exists()
        if answer_exist:
            AnswerModel.objects.filter(id=ans_id).delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)


class UpdateAnswer(APIView):
    def post(self, request, id) -> Response:
        answer_exist: bool = AnswerModel.objects.filter(id=id).exists()
        if answer_exist:
            answer: AnswerModel = AnswerModel.objects.get(id=id)
            serializer = AnswerSerializer(answer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_400_BAD_REQUEST)
