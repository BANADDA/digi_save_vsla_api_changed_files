from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import CycleStartMeeting
from digi_save_vsla_api.serializers import CycleStartMeetingSerializer

@api_view(['GET', 'POST'])
def cycle_start_meeting_list(request):
    if request.method == 'GET':
        cycle_start_meetings = CycleStartMeeting.objects.all()
        serializer = CycleStartMeetingSerializer(cycle_start_meetings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CycleStartMeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cycle_start_meeting_detail(request, pk):
    try:
        cycle_start_meeting = CycleStartMeeting.objects.get(pk=pk)
    except CycleStartMeeting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CycleStartMeetingSerializer(cycle_start_meeting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CycleStartMeetingSerializer(cycle_start_meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cycle_start_meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)