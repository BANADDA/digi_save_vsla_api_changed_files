from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import LoanDisbursement
from digi_save_vsla_api.serializers import LoanDisbursementSerializer

@api_view(['GET', 'POST'])
def loan_disbursement_list(request):
    if request.method == 'GET':
        loan_disbursements = LoanDisbursement.objects.all()
        serializer = LoanDisbursementSerializer(loan_disbursements, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoanDisbursementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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