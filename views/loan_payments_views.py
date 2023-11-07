from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import *
from digi_save_vsla_api.serializers import LoanPaymentsSerializer

@api_view(['GET', 'POST'])
def loan_payments_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            member_id = data.get('member_id')
            group_id = data.get('groupId')
            loan_id = data.get('loan_id')
            payment_amount = data.get('payment_amount')
            payment_date = data.get('payment_date')

            # Get the related instances based on their IDs
            member = GroupMembers.objects.get(id=member_id)
            group = GroupForm.objects.get(id=group_id)
            loan = Loans.objects.get(id=loan_id)

            payment = LoanPayments(
                member=member,
                group=group,
                loan=loan,
                payment_amount=payment_amount,
                payment_date=payment_date,
            )
            payment.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Loan payment created successfully',
            })

        if request.method == 'GET':
            payments = LoanPayments.objects.all()
            payment_data = []
            for payment in payments:
                payment_data.append({
                    'member_id': payment.member.id,
                    'groupId': payment.group.id,
                    'loan_id': payment.loan.id,
                    'payment_amount': payment.payment_amount,
                    'payment_date': payment.payment_date,
                })
            return JsonResponse({
                'status': 'success',
                'loan_payments': payment_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def loan_payments_detail(request, pk):
    try:
        loan_payment = LoanPayments.objects.get(pk=pk)
    except LoanPayments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanPaymentsSerializer(loan_payment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoanPaymentsSerializer(loan_payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loan_payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)