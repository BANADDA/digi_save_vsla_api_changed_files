from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Loans
from digi_save_vsla_api.serializers import LoansSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def loans_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            member_id = data.get('member_id')
            loan_applicant = data.get('loan_applicant')
            group_id = data.get('groupId')
            loan_purpose = data.get('loan_purpose')
            loan_amount = data.get('loan_amount')
            interest_rate = data.get('interest_rate')
            start_date = data.get('start_date')
            end_date = data.get('end_date')
            status = data.get('status')

            # Get the related instances based on their IDs
            member = GroupMembers.objects.get(id=member_id)
            group = GroupForm.objects.get(id=group_id)

            loan = Loans(
                member=member,
                loan_applicant=loan_applicant,
                group=group,
                loan_purpose=loan_purpose,
                loan_amount=loan_amount,
                interest_rate=interest_rate,
                start_date=start_date,
                end_date=end_date,
                status=status,
            )
            loan.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Loan created successfully',
            })

        if request.method == 'GET':
            loans = Loans.objects.all()
            loan_data = []
            for loan in loans:
                loan_data.append({
                    'member_id': loan.member.id,
                    'loan_applicant': loan.loan_applicant,
                    'groupId': loan.group.id,
                    'loan_purpose': loan.loan_purpose,
                    'loan_amount': loan.loan_amount,
                    'interest_rate': loan.interest_rate,
                    'start_date': loan.start_date,
                    'end_date': loan.end_date,
                    'status': loan.status,
                })
            return JsonResponse({
                'status': 'success',
                'loans': loan_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def loans_detail(request, pk):
    try:
        loans = Loans.objects.get(pk=pk)
    except Loans.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoansSerializer(loans)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoansSerializer(loans, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loans.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
