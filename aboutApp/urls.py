from django.urls import path
from . import views

app_name = 'aboutApp'

urlpatterns = [
    path('survey/', views.survey, name='survey'),  # 企业概况
    path('honor/', views.honor, name='honor'),     # 荣誉资质
]