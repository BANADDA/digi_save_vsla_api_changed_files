from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import ReversedTransactions
from digi_save_vsla_api.serializers import ReversedTransactionsSerializer

@api_view(['GET', 'POST'])
def reversed_transactions_list(request):
    if request.method == 'GET':
        reversed_transactions = ReversedTransactions.objects.all()
        serializer = ReversedTransactionsSerializer(reversed_transactions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReversedTransactionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def reversed_transactions_detail(request, pk):
    try:
        reversed_transaction = ReversedTransactions.objects.get(pk=pk)
    except ReversedTransactions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReversedTransactionsSerializer(reversed_transaction)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReversedTransactionsSerializer(reversed_transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reversed_transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)