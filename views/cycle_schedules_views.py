# views/cycle_schedules_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import CycleSchedules, GroupProfile
from digi_save_vsla_api.serializers import CycleSchedulesSerializer

@api_view(['GET', 'POST'])
def cycle_schedules_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            
            print("Received data:", data)
            group_id = data.get('group_id')
            meeting_duration = data.get('meeting_duration')
            number_of_meetings = data.get('number_of_meetings')
            meeting_frequency = data.get('meeting_frequency')
            day_of_week = data.get('day_of_week')
            start_date = data.get('start_date')
            share_out_date = data.get('share_out_date')
            sync_flag = data.get('sync_flag')

            #  # Get the GroupProfile instance based on the group_id
            group_profile = GroupProfile.objects.get(id=group_id)
            # print('Group profile object: ', group_profile)


            cycle_schedules = CycleSchedules(
                group_id=group_profile,
                meeting_duration=meeting_duration,
                number_of_meetings=number_of_meetings,
                meeting_frequency=meeting_frequency,
                day_of_week=day_of_week,
                start_date=start_date,
                share_out_date=share_out_date,
                sync_flag=sync_flag,
            )
            cycle_schedules.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Cycle Schedle created successfully',
            })

        if request.method == 'GET':
            cycleSchedules_ = CycleSchedules.objects.all()
            CycleSchedules_data = []
            for cycle_schedules in cycleSchedules_:
                CycleSchedules_data.append({
                    'group_id': cycle_schedules.group_id.id,
                    'meeting_duration': cycle_schedules.meeting_duration,
                    'number_of_meetings': cycle_schedules.number_of_meetings,
                    'meeting_frequency': cycle_schedules.meeting_frequency,
                    'day_of_week': cycle_schedules.day_of_week,
                    'start_date': cycle_schedules.start_date,
                    'share_out_date': cycle_schedules.share_out_date,
                    'sync_flag': cycle_schedules.sync_flag,
                })
            return JsonResponse({
                'status': 'success',
                'CycleSchedules': CycleSchedules_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def cycle_schedules_detail(request, pk):
    try:
        cycle_schedule = CycleSchedules.objects.get(pk=pk)
    except CycleSchedules.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CycleSchedulesSerializer(cycle_schedule)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CycleSchedulesSerializer(cycle_schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cycle_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
