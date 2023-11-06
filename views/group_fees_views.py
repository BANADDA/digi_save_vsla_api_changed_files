from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import GroupFees
from digi_save_vsla_api.serializers import GroupFeesSerializer

@api_view(['GET', 'POST'])
def group_fees_list(request):
    if request.method == 'GET':
        group_fees = GroupFees.objects.all()
        serializer = GroupFeesSerializer(group_fees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroupFeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def group_fees_detail(request, pk):
    try:
        group_fees = GroupFees.objects.get(pk=pk)
    except GroupFees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupFeesSerializer(group_fees)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupFeesSerializer(group_fees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_fees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)