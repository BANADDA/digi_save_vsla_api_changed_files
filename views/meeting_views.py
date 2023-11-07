from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Meeting
from digi_save_vsla_api.serializers import MeetingSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def meeting_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')
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
            socialFundContributions = data.get('socialFundContributions')
            sharePurchases = data.get('sharePurchases')
            totalLoanFund = data.get('totalLoanFund')
            totalSocialFund = data.get('totalSocialFund')

            # Get the related instances based on their IDs
            group = GroupForm.objects.get(id=group_id)
            cycle = CycleMeeting.objects.get(id=cycle_id)

            meeting = Meeting(
                group_id=group,
                cycle_id=cycle,
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
                socialFundContributions=socialFundContributions,
                sharePurchases=sharePurchases,
                totalLoanFund=totalLoanFund,
                totalSocialFund=totalSocialFund,
            )
            meeting.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Meeting created successfully',
            })

        if request.method == 'GET':
            meetings = Meeting.objects.all()
            meeting_data = []
            for meeting in meetings:
                meeting_data.append({
                    'group_id': meeting.group_id.id,
                    'cycle_id': meeting.cycle_id.id,
                    'date': meeting.date,
                    'time': meeting.time,
                    'endTime': meeting.endTime,
                    'location': meeting.location,
                    'facilitator': meeting.facilitator,
                    'meetingPurpose': meeting.meetingPurpose,
                    'latitude': meeting.latitude,
                    'longitude': meeting.longitude,
                    'address': meeting.address,
                    'objectives': meeting.objectives,
                    'attendanceData': meeting.attendanceData,
                    'representativeData': meeting.representativeData,
                    'proposals': meeting.proposals,
                    'socialFundContributions': meeting.socialFundContributions,
                    'sharePurchases': meeting.sharePurchases,
                    'totalLoanFund': meeting.totalLoanFund,
                    'totalSocialFund': meeting.totalSocialFund,
                })
            return JsonResponse({
                'status': 'success',
                'meetings': meeting_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def meeting_detail(request, pk):
    try:
        meeting = Meeting.objects.get(pk=pk)
    except Meeting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MeetingSerializer(meeting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MeetingSerializer(meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)