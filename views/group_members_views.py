# views/group_members_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import GroupMembers, GroupProfile, Users
from digi_save_vsla_api.serializers import GroupMembersSerializer

@api_view(['GET', 'POST'])
def group_members_list(request):
    data = request.data
    print("Received data:", data)
    try:
        if request.method == 'POST':
            
            print("Received data:", data)
            group_id = data.get('group_id')
            user_id = data.get('user_id')
            sync_flag = data.get('sync_flag')

            #  # Get the GroupProfile instance based on the group_id
            group_id = GroupProfile.objects.get(id=group_id)
            user_id = Users.objects.get(id=user_id)


            group_members = GroupMembers(
                group_id=group_id,
                user_id=user_id,
                sync_flag=sync_flag,
            )
            group_members.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Group members added successfully',
            })

        if request.method == 'GET':
            groupMembers = GroupMembers.objects.all()
            print('Group members: ', groupMembers)
            group_member_data = []
            for group_member in groupMembers:
                group_member_data.append({
                    'group_id': group_member.group_id.id,
                    'user_id': group_member.user_id.id,
                    'sync_flag': group_member.sync_flag,
                })
            return JsonResponse({
                'status': 'success',
                'groupMembers': group_member_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def group_members_detail(request, pk):
    try:
        group_member = GroupMembers.objects.get(pk=pk)
    except GroupMembers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupMembersSerializer(group_member)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupMembersSerializer(group_member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
