# views/savings_account_views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import SavingsAccount
from digi_save_vsla_api.serializers import SavingsAccountSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def savings_account_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            logged_in_users_id = data.get('logged_in_users_id')
            date = data.get('date')
            purpose = data.get('purpose')
            amount = data.get('amount')
            group_id = data.get('group_id')

            # Get the related instances based on their IDs
            group = GroupForm.objects.get(id=group_id)
            logged_in_users_id = Users.objects.get(id=logged_in_users_id)

            savings_account = SavingsAccount(
                logged_in_users_id=logged_in_users_id,
                date=date,
                purpose=purpose,
                amount=amount,
                group=group
            )
            savings_account.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Savings account created successfully',
            })

        if request.method == 'GET':
            savings_accounts = SavingsAccount.objects.all()
            savings_account_data = []
            for savings_account in savings_accounts:
                savings_account_data.append({
                    'logged_in_users_id': savings_account.logged_in_users_id.id,
                    'date': savings_account.date,
                    'purpose': savings_account.purpose,
                    'amount': savings_account.amount,
                    'group_id': savings_account.group.id,
                })
            return JsonResponse({
                'status': 'success',
                'savings_accounts': savings_account_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def savings_account_detail(request, pk):
    try:
        savings_account = SavingsAccount.objects.get(pk=pk)
    except SavingsAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SavingsAccountSerializer(savings_account)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SavingsAccountSerializer(savings_account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        savings_account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
