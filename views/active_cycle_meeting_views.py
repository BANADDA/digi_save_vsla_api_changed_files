from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import ActiveCycleMeeting, CycleMeeting, GroupProfile
from digi_save_vsla_api.serializers import ActiveCycleMeetingSerializer

@api_view(['GET', 'POST'])
def active_cycle_meeting_list(request):
    print("Received data:", request.data)
    data = request.data
    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            cycleMeetingID = data.get('cycleMeetingID')

            # Get the GroupProfile instance based on the group_id
            group_profile = GroupProfile.objects.get(id=group_id)
            cycleMeetingID = CycleMeeting.objects.get(id=cycleMeetingID)

            constitution = ActiveCycleMeeting(
                group_id=group_profile,
                cycleMeetingID=cycleMeetingID,
            )
            constitution.save()

            return JsonResponse({
                'status': 'success',
                'message': 'ActiveCycleMeeting created successfully',
            })

        if request.method == 'GET':
            constitutions = ActiveCycleMeeting.objects.all()
            constitution_data = []
            for constitution in constitutions:
                constitution_data.append({
                    'group_id': constitution.group_id,
                    'cycleMeetingID': constitution.cycleMeetingID,
                })
            return JsonResponse({
                'status': 'success',
                'constitutions': constitution_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def active_cycle_meeting_detail(request, pk):
    try:
        active_cycle_meeting = ActiveCycleMeeting.objects.get(pk=pk)
    except ActiveCycleMeeting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActiveCycleMeetingSerializer(active_cycle_meeting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ActiveCycleMeetingSerializer(active_cycle_meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        active_cycle_meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
