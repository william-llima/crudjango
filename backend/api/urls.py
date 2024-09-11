from django.contrib import admin
from django.urls import path,include
from api.views import *


urlpatterns = [
    path('register', CreatePessoaView.as_view(), name='registerpessoa' ),
    path('search', PessoaListView.as_view(), name='pessoa-list'),
     path('pessoas/<int:pk>/update/', PessoaUpdateView.as_view(), name='pessoa-update'),
     path('pessoas/<int:pk>/delete/', PessoaDeleteView.as_view(), name='pessoa-delete'),
      path('pessoas/peso', PesoIdealView.as_view(), name='pessoa-peso'),
]
