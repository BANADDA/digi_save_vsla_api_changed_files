from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Shares
from digi_save_vsla_api.serializers import SharesSerializer

@api_view(['GET', 'POST'])
def shares_list(request):
    if request.method == 'GET':
        shares = Shares.objects.all()
        serializer = SharesSerializer(shares, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SharesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def shares_detail(request, pk):
    try:
        shares = Shares.objects.get(pk=pk)
    except Shares.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SharesSerializer(shares)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SharesSerializer(shares, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        shares.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)