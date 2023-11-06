# views/savings_account_views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import SavingsAccount
from digi_save_vsla_api.serializers import SavingsAccountSerializer

@api_view(['GET', 'POST'])
def savings_account_list(request):
    if request.method == 'GET':
        savings_accounts = SavingsAccount.objects.all()
        serializer = SavingsAccountSerializer(savings_accounts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SavingsAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
