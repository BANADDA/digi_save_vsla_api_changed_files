from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import ReversedTransactions
from digi_save_vsla_api.serializers import ReversedTransactionsSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def reversed_transactions_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            savings_account_id = data.get('savings_account_id')
            logged_in_users_id = data.get('logged_in_users_id')
            reversed_amount = data.get('reversed_amount')
            date = data.get('date')
            purpose = data.get('purpose')
            reversed_data = data.get('reversed_data')

            # Get the related instances based on their IDs
            group = GroupProfile.objects.get(id=group_id)
            savings_account = SavingsAccount.objects.get(id=savings_account_id)
            logged_in_users = Users.objects.get(id=logged_in_users_id)

            reversed_transaction = ReversedTransactions(
                group=group,
                savings_account=savings_account,
                logged_in_users=logged_in_users,
                reversed_amount=reversed_amount,
                date=date,
                purpose=purpose,
                reversed_data=reversed_data,
            )
            reversed_transaction.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Reversed transaction created successfully',
            })

        if request.method == 'GET':
            reversed_transactions = ReversedTransactions.objects.all()
            reversed_transaction_data = []
            for reversed_transaction in reversed_transactions:
                reversed_transaction_data.append({
                    'group_id': reversed_transaction.group.id,
                    'savings_account_id': reversed_transaction.savings_account.id,
                    'logged_in_users_id': reversed_transaction.logged_in_users.id,
                    'reversed_amount': reversed_transaction.reversed_amount,
                    'date': reversed_transaction.date,
                    'purpose': reversed_transaction.purpose,
                    'reversed_data': reversed_transaction.reversed_data,
                })
            return JsonResponse({
                'status': 'success',
                'reversed_transactions': reversed_transaction_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

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