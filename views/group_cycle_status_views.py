from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import CycleMeeting, GroupCycleStatus, GroupProfile
from digi_save_vsla_api.serializers import GroupCycleStatusSerializer

@api_view(['GET', 'POST'])
def group_cycle_status_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')
            is_cycle_started = data.get('is_cycle_started')

            # Get the related instances based on their IDs
            group = GroupProfile.objects.get(id=group_id)
            cycle = CycleMeeting.objects.get(id=cycle_id)

            cycle_status = GroupCycleStatus(
                group=group,
                cycleId=cycle,
                is_cycle_started=is_cycle_started,
            )
            cycle_status.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Cycle status created successfully',
            })

        if request.method == 'GET':
            cycle_statuses = GroupCycleStatus.objects.all()
            cycle_status_data = []
            for cycle_status in cycle_statuses:
                cycle_status_data.append({
                    'group_id': cycle_status.group.id,
                    'cycleId': cycle_status.cycleId.id,
                    'is_cycle_started': cycle_status.is_cycle_started,
                })
            return JsonResponse({
                'status': 'success',
                'cycle_statuses': cycle_status_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)
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