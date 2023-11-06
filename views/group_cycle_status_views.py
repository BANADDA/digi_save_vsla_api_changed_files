from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import GroupCycleStatus
from digi_save_vsla_api.serializers import GroupCycleStatusSerializer

@api_view(['GET', 'POST'])
def group_cycle_status_list(request):
    if request.method == 'GET':
        group_cycle_status = GroupCycleStatus.objects.all()
        serializer = GroupCycleStatusSerializer(group_cycle_status, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroupCycleStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def group_cycle_status_detail(request, pk):
    try:
        group_cycle_status = GroupCycleStatus.objects.get(pk=pk)
    except GroupCycleStatus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupCycleStatusSerializer(group_cycle_status)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupCycleStatusSerializer(group_cycle_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_cycle_status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)