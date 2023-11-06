from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Fines
from digi_save_vsla_api.serializers import FinesSerializer

@api_view(['GET', 'POST'])
def fines_list(request):
    if request.method == 'GET':
        fines = Fines.objects.all()
        serializer = FinesSerializer(fines, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def fines_detail(request, pk):
    try:
        fines = Fines.objects.get(pk=pk)
    except Fines.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FinesSerializer(fines)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FinesSerializer(fines, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fines.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)