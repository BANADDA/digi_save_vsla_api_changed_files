from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import WelfareAccount
from digi_save_vsla_api.serializers import WelfareAccountSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def welfare_account_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            logged_in_users_id = data.get('logged_in_users_id')
            amount = data.get('amount')
            group_id = data.get('group_id')
            meeting_id = data.get('meeting_id')
            cycle_id = data.get('cycle_id')

            # Get the related instances based on their IDs
            group = GroupForm.objects.get(id=group_id)
            logged_in_users_id = Users.objects.get(id=logged_in_users_id)
            meeting = Meeting.objects.get(id=meeting_id)
            cycle = CycleMeeting.objects.get(id=cycle_id)

            welfare_account = WelfareAccount(
                logged_in_users_id=logged_in_users_id,
                amount=amount,
                group=group,
                meeting_id=meeting,
                cycle_id=cycle,
            )
            welfare_account.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Welfare account created successfully',
            })

        if request.method == 'GET':
            welfare_accounts = WelfareAccount.objects.all()
            welfare_account_data = []
            for welfare_account in welfare_accounts:
                welfare_account_data.append({
                    'logged_in_users_id': welfare_account.logged_in_users_id.id,
                    'amount': welfare_account.amount,
                    'group_id': welfare_account.group_id.id,
                    'meeting_id': welfare_account.meeting_id.id,
                    'cycle_id': welfare_account.cycle_id.id,
                })
            return JsonResponse({
                'status': 'success',
                'welfare_accounts': welfare_account_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

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