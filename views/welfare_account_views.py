from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import WelfareAccount
from digi_save_vsla_api.serializers import WelfareAccountSerializer

@api_view(['GET', 'POST'])
def welfare_account_list(request):
    if request.method == 'GET':
        welfare_accounts = WelfareAccount.objects.all()
        serializer = WelfareAccountSerializer(welfare_accounts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WelfareAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def welfare_account_detail(request, pk):
    try:
        welfare_account = WelfareAccount.objects.get(pk=pk)
    except WelfareAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WelfareAccountSerializer(welfare_account)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WelfareAccountSerializer(welfare_account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        welfare_account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)