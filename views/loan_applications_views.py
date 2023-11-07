from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import CycleMeeting, GroupForm, GroupMembers, LoanApplications, Meeting
from digi_save_vsla_api.serializers import LoanApplicationsSerializer

@api_view(['GET', 'POST'])
def loan_applications_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')
            meeting_id = data.get('meetingId')
            submission_date = data.get('submission_date')
            loan_applicant = data.get('loan_applicant')
            group_member_id = data.get('group_member_id')
            amount_needed = data.get('amount_needed')
            loan_purpose = data.get('loan_purpose')
            repayment_date = data.get('repayment_date')

            # Get the related instances based on their IDs
            group = GroupForm.objects.get(id=group_id)
            cycle = CycleMeeting.objects.get(id=cycle_id)
            meeting = Meeting.objects.get(id=meeting_id)
            group_member = GroupMembers.objects.get(id=group_member_id)

            loan_application = LoanApplications(
                group_id=group,
                cycle_id=cycle,
                meeting_id=meeting,
                submission_date=submission_date,
                loan_applicant=loan_applicant,
                group_member=group_member,
                amount_needed=amount_needed,
                loan_purpose=loan_purpose,
                repayment_date=repayment_date,
            )
            loan_application.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Loan application created successfully',
            })

        if request.method == 'GET':
            loan_applications = LoanApplications.objects.all()
            loan_application_data = []
            for loan_application in loan_applications:
                loan_application_data.append({
                    'group_id': loan_application.group_id.id,
                    'cycle_id': loan_application.cycle_id.id,
                    'meetingId': loan_application.meeting_id.id,
                    'submission_date': loan_application.submission_date,
                    'loan_applicant': loan_application.loan_applicant,
                    'group_member_id': loan_application.group_member.id,
                    'amount_needed': loan_application.amount_needed,
                    'loan_purpose': loan_application.loan_purpose,
                    'repayment_date': loan_application.repayment_date,
                })
            return JsonResponse({
                'status': 'success',
                'loan_applications': loan_application_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)
@api_view(['GET', 'PUT', 'DELETE'])
def loan_applications_detail(request, pk):
    try:
        loan_application = LoanApplications.objects.get(pk=pk)
    except LoanApplications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanApplicationsSerializer(loan_application)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoanApplicationsSerializer(loan_application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loan_application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)