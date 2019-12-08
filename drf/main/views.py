from django.shortcuts import render, get_object_or_404
from .models import Person, House

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from .serializers import PersonSerializer, HouseSerializer

from rest_framework.permissions import IsAuthenticated

# FUNCTION-BASED VIEW
# @api_view(['GET', 'POST'])
# def fbv(request):
#     print(request.user)
#     if request.method == 'GET':
#         return Response(data={'message': 'FBV GET'}, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         return Response(data=request.data, status=status.HTTP_200_OK)
#     else:
#         return Response(data="Something does not seem to be working.")

# CLASS-BASED VIEW
# class cbv(APIView):
#     def get(self, request):
#         print(request.user)    
#         return Response(data={'message': 'CBV GET'}, status=status.HTTP_200_OK)

#     def post(self, request):
#         print(request.user)
#         return Response(data=request.data, status=status.HTTP_200_OK)

# CLASS-BASED VIEW WITH SERIALIZED MODELS
# class mainapi(APIView):
#     def get_all_objects(self):
#         try:
#             return Person.objects.all()
#         except Person.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND

#     def get_object(self, pid):
#         try:
#             return Person.objects.get(id=pid)
#         except Person.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND

#     def get(self, request, format=None):
#         queryset = self.get_all_objects()
#         serializer = PersonSerializer(queryset, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = PersonSerializer(data=request.data)
#         try:
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             print(e)
#             return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request):
#         pid = request.data['id']
#         queryset = self.get_object(pid)
#         queryset.delete()
#         return Response(data={'message': 'MAINAPI DELETED '+pid}, status=status.HTTP_410_GONE)

#     def put(self, request):
#         pid = request.data['id']
#         queryset = self.get_object(pid)
#         serializer = PersonSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# CLASS-BASED GENERIC VIEW WITH SERIALIZED MODELS
# class mainapi_person_generic(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# CLASS-BASED VIEWSET
class mainapi_person_viewset(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    permission_classes = [IsAuthenticated]

class mainapi_house_viewset(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    queryset = House.objects.all()
    permission_classes = [IsAuthenticated]