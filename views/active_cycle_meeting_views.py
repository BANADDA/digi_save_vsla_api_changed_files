from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import ActiveCycleMeeting
from digi_save_vsla_api.serializers import ActiveCycleMeetingSerializer

@api_view(['GET', 'POST'])
def active_cycle_meeting_list(request):
    if request.method == 'GET':
        active_cycle_meetings = ActiveCycleMeeting.objects.all()
        serializer = ActiveCycleMeetingSerializer(active_cycle_meetings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ActiveCycleMeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
