from answer.views import (CreateAnswer, DeleteAnswer, GetAnswer, UpdateAnswer,
                          ViewAllAnswers)
from django.urls import path

urlpatterns = [
    path("answers", ViewAllAnswers.as_view(), name="all_ans"),
    path("answer/<uuid:id>", GetAnswer.as_view(), name="get_ans"),
    path("create-answer", CreateAnswer.as_view(), name="create_ans"),
    path("delete-answer", DeleteAnswer.as_view(), name="del_ans"),
    path("update-answer", UpdateAnswer.as_view(), name="update_ans"),
]
