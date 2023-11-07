from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import MemberShares
from digi_save_vsla_api.serializers import MemberSharesSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def member_shares_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            logged_in_users_id = data.get('logged_in_users_id')
            date = data.get('date')
            sharePurchases = data.get('sharePurchases')
            meeting_id = data.get('meetingId')
            users_id = data.get('users_id')
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')

            # Get the related instances based on their IDs
            meeting = Meeting.objects.get(id=meeting_id)
            users = Users.objects.get(id=users_id)
            group = GroupForm.objects.get(id=group_id)
            cycle_id = CycleMeeting.objects.get(id=cycle_id)

            member_shares = MemberShares(
                logged_in_users_id=logged_in_users_id,
                date=date,
                sharePurchases=sharePurchases,
                meeting=meeting,
                users=users,
                group_id=group,
                cycle_id=cycle_id,
            )
            member_shares.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Member shares created successfully',
            })

        if request.method == 'GET':
            member_shares = MemberShares.objects.all()
            member_shares_data = []
            for member_share in member_shares:
                member_shares_data.append({
                    'logged_in_users_id': member_share.logged_in_users_id,
                    'date': member_share.date,
                    'sharePurchases': member_share.sharePurchases,
                    'meetingId': member_share.meeting.id,
                    'users_id': member_share.users.id,
                    'group_id': member_share.group_id.id,
                    'cycle_id': member_share.cycle_id.id,
                })
            return JsonResponse({
                'status': 'success',
                'member_shares': member_shares_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def member_shares_detail(request, pk):
    try:
        member_shares = MemberShares.objects.get(pk=pk)
    except MemberShares.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSharesSerializer(member_shares)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MemberSharesSerializer(member_shares, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member_shares.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)