from django.urls import path
from question.views import (Create_Question, Delete_Question, Get_Question,
                            List_Question, Update_Question)

urlpatterns = [
    path("question/<uuid:id>", Get_Question.as_view(), name="get_question"),
    path("questions", List_Question.as_view(), name="list_question"),
    path("create-question", Create_Question.as_view(), name="create-question"),
    path("update-question", Update_Question.as_view(), name="update-question"),
    path("delete-question", Delete_Question.as_view(), name="delete-question"),
]
