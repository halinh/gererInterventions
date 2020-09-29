from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from interventions.models import Intervention
from interventions.serializers import InterventionSerializer

# Create your views here.
class InterventionListView(APIView):
    def get(self, request):
        interventions = Intervention.objects.all()
        serializer = InterventionSerializer(interventions, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = InterventionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class InterventionDetailView(APIView):
    def get(self,request,pk):
        intervention=get_object_or_404(Intervention, pk=pk)
        serializer = InterventionSerializer(intervention)
        return Response(serializer.data)

    def put(self,request,pk):
        intervention=get_object_or_404(Intervention, pk=pk)
        serializer = InterventionSerializer(intervention,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        intervention=get_object_or_404(Intervention, pk=pk)
        intervention.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)