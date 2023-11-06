# views/assigned_positions_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import AssignedPositions, GroupMembers, GroupProfile, Positions
from digi_save_vsla_api.serializers import AssignedPositionsSerializer

@api_view(['GET', 'POST'])
def assigned_positions_list(request):
    data = request.data
    print("Received data:", data)
    try:
        if request.method == 'POST':
            
            print("Received data:", data)
            position_id = data.get('position_id')
            group_id = data.get('group_id')
            member_id = data.get('member_id')
            sync_flag = data.get('sync_flag')

            #  # Get the GroupProfile instance based on the position_id
            group_id = GroupProfile.objects.get(id=group_id)
            position_id = Positions.objects.get(id=position_id)
            member_id = GroupMembers.objects.get(id=member_id)


            group_members = AssignedPositions(
                position_id=position_id,
                member_id=member_id,
                sync_flag=sync_flag,
            )
            group_members.save()

            return JsonResponse({
                'status': 'success',
                'message': 'AssignedPositions created successfully',
            })

        if request.method == 'GET':
            groupMembers = AssignedPositions.objects.all()
            group_member_data = ()
            for group_member in groupMembers:
                group_member_data.append({
                    'position_id': group_member.position_id,
                    'member_id': group_member.member_id,
                    'sync_flag': group_member.sync_flag,
                })
            return JsonResponse({
                'status': 'success',
                'CycleSchedules': group_member_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)
@api_view(['GET', 'PUT', 'DELETE'])
def assigned_positions_detail(request, pk):
    try:
        assigned_position = AssignedPositions.objects.get(pk=pk)
    except AssignedPositions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AssignedPositionsSerializer(assigned_position)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AssignedPositionsSerializer(assigned_position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        assigned_position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

