from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import SocialFundApplications
from digi_save_vsla_api.serializers import SocialFundApplicationsSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def social_fund_applications_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')
            meeting_id = data.get('meeting_id')
            submission_date = data.get('submission_date')
            applicant = data.get('applicant')
            group_member_id = data.get('group_member_id')
            amount_needed = data.get('amount_needed')
            social_purpose = data.get('social_purpose')
            repayment_date = data.get('repayment_date')

            # Get the related instances based on their IDs
            group = GroupForm.objects.get(id=group_id)
            cycle = CycleMeeting.objects.get(id=cycle_id)
            meeting = Meeting.objects.get(id=meeting_id)
            group_member = GroupMembers.objects.get(id=group_member_id)

            social_fund_application = SocialFundApplications(
                group_id=group,
                cycle_id=cycle,
                meeting_id=meeting,
                submission_date=submission_date,
                applicant=applicant,
                group_member=group_member,
                amount_needed=amount_needed,
                social_purpose=social_purpose,
                repayment_date=repayment_date,
            )
            social_fund_application.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Social Fund application created successfully',
            })

        if request.method == 'GET':
            social_fund_applications = SocialFundApplications.objects.all()
            social_fund_data = []
            for social_fund_application in social_fund_applications:
                social_fund_data.append({
                    'group_id': social_fund_application.group_id.id,
                    'cycle_id': social_fund_application.cycle_id.id,
                    'meeting_id': social_fund_application.meeting_id.id,
                    'submission_date': social_fund_application.submission_date,
                    'applicant': social_fund_application.applicant,
                    'group_member_id': social_fund_application.group_member.id,
                    'amount_needed': social_fund_application.amount_needed,
                    'social_purpose': social_fund_application.social_purpose,
                    'repayment_date': social_fund_application.repayment_date,
                })
            return JsonResponse({
                'status': 'success',
                'social_fund_applications': social_fund_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def social_fund_applications_detail(request, pk):
    try:
        social_fund_application = SocialFundApplications.objects.get(pk=pk)
    except SocialFundApplications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialFundApplicationsSerializer(social_fund_application)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SocialFundApplicationsSerializer(social_fund_application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        social_fund_application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)