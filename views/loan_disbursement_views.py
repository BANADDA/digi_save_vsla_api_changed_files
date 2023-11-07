from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import CycleMeeting, GroupForm, GroupMembers, LoanDisbursement, Loans
from digi_save_vsla_api.serializers import LoanDisbursementSerializer

@api_view(['GET', 'POST'])
def loan_disbursement_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            member_id = data.get('member_id')
            group_id = data.get('groupId')
            cycle_id = data.get('cycleId')
            loan_id = data.get('loan_id')
            disbursement_amount = data.get('disbursement_amount')
            disbursement_date = data.get('disbursement_date')

            # Get the related instances based on their IDs
            member = GroupMembers.objects.get(id=member_id)
            group = GroupForm.objects.get(id=group_id)
            cycle = CycleMeeting.objects.get(id=cycle_id)
            loan = Loans.objects.get(id=loan_id)

            disbursement = LoanDisbursement(
                member=member,
                group=group,
                cycleId=cycle,
                loan=loan,
                disbursement_amount=disbursement_amount,
                disbursement_date=disbursement_date,
            )
            disbursement.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Loan disbursement created successfully',
            })

        if request.method == 'GET':
            disbursements = LoanDisbursement.objects.all()
            disbursement_data = []
            for disbursement in disbursements:
                disbursement_data.append({
                    'member_id': disbursement.member.id,
                    'groupId': disbursement.group.id,
                    'cycleId': disbursement.cycleId.id,
                    'loan_id': disbursement.loan.id,
                    'disbursement_amount': disbursement.disbursement_amount,
                    'disbursement_date': disbursement.disbursement_date,
                })
            return JsonResponse({
                'status': 'success',
                'loan_disbursements': disbursement_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def loan_disbursement_detail(request, pk):
    try:
        loan_disbursement = LoanDisbursement.objects.get(pk=pk)
    except LoanDisbursement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanDisbursementSerializer(loan_disbursement)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoanDisbursementSerializer(loan_disbursement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loan_disbursement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)