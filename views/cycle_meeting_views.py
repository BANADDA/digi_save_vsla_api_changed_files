from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import CycleMeeting, GroupForm, GroupProfile
from digi_save_vsla_api.serializers import CycleMeetingSerializer

@api_view(['GET', 'POST'])
def cycle_meeting_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            date = data.get('date')
            time = data.get('time')
            endTime = data.get('endTime')
            location = data.get('location')
            facilitator = data.get('facilitator')
            meetingPurpose = data.get('meetingPurpose')
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            address = data.get('address')
            objectives = data.get('objectives')
            attendanceData = data.get('attendanceData')
            representativeData = data.get('representativeData')
            proposals = data.get('proposals')
            totalLoanFund = data.get('totalLoanFund')
            totalSocialFund = data.get('totalSocialFund')
            socialFundContributions = data.get('socialFundContributions')
            sharePurchases = data.get('sharePurchases')
            group_id = data.get('group_id')

            # Get the related group instance based on its ID
            group = GroupForm.objects.get(id=group_id)

            cycle_meeting = CycleMeeting(
                date=date,
                time=time,
                endTime=endTime,
                location=location,
                facilitator=facilitator,
                meetingPurpose=meetingPurpose,
                latitude=latitude,
                longitude=longitude,
                address=address,
                objectives=objectives,
                attendanceData=attendanceData,
                representativeData=representativeData,
                proposals=proposals,
                totalLoanFund=totalLoanFund,
                totalSocialFund=totalSocialFund,
                socialFundContributions=socialFundContributions,
                sharePurchases=sharePurchases,
                group_id=group,
            )
            cycle_meeting.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Cycle meeting created successfully',
            })

        if request.method == 'GET':
            cycle_meetings = CycleMeeting.objects.all()
            cycle_meeting_data = []
            for cycle_meeting in cycle_meetings:
                cycle_meeting_data.append({
                    'date': cycle_meeting.date,
                    'time': cycle_meeting.time,
                    'endTime': cycle_meeting.endTime,
                    'location': cycle_meeting.location,
                    'facilitator': cycle_meeting.facilitator,
                    'meetingPurpose': cycle_meeting.meetingPurpose,
                    'latitude': cycle_meeting.latitude,
                    'longitude': cycle_meeting.longitude,
                    'address': cycle_meeting.address,
                    'objectives': cycle_meeting.objectives,
                    'attendanceData': cycle_meeting.attendanceData,
                    'representativeData': cycle_meeting.representativeData,
                    'proposals': cycle_meeting.proposals,
                    'totalLoanFund': cycle_meeting.totalLoanFund,
                    'totalSocialFund': cycle_meeting.totalSocialFund,
                    'socialFundContributions': cycle_meeting.socialFundContributions,
                    'sharePurchases': cycle_meeting.sharePurchases,
                    'group_id': cycle_meeting.group_id.id,
                })
            return JsonResponse({
                'status': 'success',
                'cycle_meetings': cycle_meeting_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def cycle_meeting_detail(request, pk):
    try:
        cycle_meeting = CycleMeeting.objects.get(pk=pk)
    except CycleMeeting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CycleMeetingSerializer(cycle_meeting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CycleMeetingSerializer(cycle_meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cycle_meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)