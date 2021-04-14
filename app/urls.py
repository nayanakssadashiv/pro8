from django.urls import path
from app import views
app_name="app"
urlpatterns = [
    path("if_demo/",views.if_demo,name="if"),
    path("else_demo/",views.else_demo,name="else"),
    path("for_demo/",views.for_demo,name="for"),
]
