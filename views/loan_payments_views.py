from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import LoanPayments
from digi_save_vsla_api.serializers import LoanPaymentsSerializer

@api_view(['GET', 'POST'])
def loan_payments_list(request):
    if request.method == 'GET':
        loan_payments = LoanPayments.objects.all()
        serializer = LoanPaymentsSerializer(loan_payments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoanPaymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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