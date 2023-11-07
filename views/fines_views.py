from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import CycleMeeting, Fines, GroupForm, GroupMembers, Meeting, SavingsAccount
from digi_save_vsla_api.serializers import FinesSerializer

@api_view(['GET', 'POST'])
def fines_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            member_id = data.get('member_id')
            amount = data.get('amount')
            reason = data.get('reason')
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')
            meeting_id = data.get('meeting_id')
            savings_account_id = data.get('savings_account_id')

            # Get the related instances based on their IDs
            member = GroupMembers.objects.get(id=member_id)
            group = GroupForm.objects.get(id=group_id)
            cycle = CycleMeeting.objects.get(id=cycle_id)
            meeting = Meeting.objects.get(id=meeting_id)
            savings_account = SavingsAccount.objects.get(id=savings_account_id)

            fine = Fines(
                memberId=member,
                amount=amount,
                reason=reason,
                groupId=group,
                cycleId=cycle,
                meetingId=meeting,
                savingsAccountId=savings_account,
            )
            fine.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Fine created successfully',
            })

        if request.method == 'GET':
            fines = Fines.objects.all()
            fine_data = []
            for fine in fines:
                fine_data.append({
                    'member_id': fine.memberId.id,
                    'amount': fine.amount,
                    'reason': fine.reason,
                    'group_id': fine.groupId.id,
                    'cycle_id': fine.cycleId.id,
                    'meeting_id': fine.meetingId.id,
                    'savings_account_id': fine.savingsAccountId.id,
                })
            return JsonResponse({
                'status': 'success',
                'fines': fine_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def fines_detail(request, pk):
    try:
        fines = Fines.objects.get(pk=pk)
    except Fines.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FinesSerializer(fines)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FinesSerializer(fines, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fines.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)