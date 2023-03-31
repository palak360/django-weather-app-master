from rest_api.models import Record
from rest_api.serializers import RecordSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


"""
    List all weather details, or create a new weather info
"""
class WeatherList(APIView):
    
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def get(self, request, format=None):
        snippets = Record.objects.all()
        serializer = RecordSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

"""
    Retrieve, update or delete a weather instance.
"""
class WeatherDetail(APIView):
    def get_object(self, pk):
        try:
            return Record.objects.get(pk=pk)
        except Record.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        weather = self.get_object(pk)
        serializer = RecordSerializer(weather)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        weather = self.get_object(pk)
        serializer = RecordSerializer(weather, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        weather = self.get_object(pk)
        weather.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)