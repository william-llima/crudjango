from django.shortcuts import render
from .models import *
from rest_framework import generics,filters
from rest_framework.permissions import AllowAny
from .serializers import * 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError



class PesoIdealView(generics.GenericAPIView):
        permission_classes = [AllowAny]
        def post(self,request,*args,**kwargs):
            data = request.data
            calculo = ''
            print(data)
            if(data['sexo']=='M'):
                calculo = ( 72.7 * float(data['altura']) )-58
            else:
                calculo = ( 62.1 * float(data['altura']) )-44.7
            return Response(f'{calculo:.2f}',status=status.HTTP_200_OK)

class CreatePessoaView(generics.CreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSearilizer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
    
        try:
            
            response = super().create(request, *args, **kwargs)
            return response
        except ValidationError as e:
          
            print("Erro de validação:", e.detail)  
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

class PessoaListView(generics.ListAPIView):
    serializer_class = PessoaSearilizer
    def get_queryset(self):
        queryset = Pessoa.objects.all()
        cpf = self.request.query_params.get('search', None)
        
        
        if cpf:
            queryset = queryset.filter(cpf=cpf)
        return queryset


class PessoaUpdateView(generics.UpdateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSearilizer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
        
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            print("Erro de validação:", e.detail)  
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        
class PessoaDeleteView(generics.DestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSearilizer
