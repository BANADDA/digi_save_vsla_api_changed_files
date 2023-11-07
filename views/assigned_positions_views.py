# views/assigned_positions_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import AssignedPositions, GroupMembers, GroupProfile, Positions
from digi_save_vsla_api.serializers import AssignedPositionsSerializer

@api_view(['GET', 'POST'])
def assigned_positions_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            position_id = data.get('position_id')
            member_id = data.get('member_id')
            group_id = data.get('group_id')

            # Get the related instances based on their IDs
            member = GroupMembers.objects.get(id=member_id)
            group = GroupProfile.objects.get(id=group_id)

            assigned_position = AssignedPositions(
                position_id=position_id,
                member_id=member,
                group_id=group,
            )
            assigned_position.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Assigned position created successfully',
            })

        if request.method == 'GET':
            assigned_positions = AssignedPositions.objects.all()
            assigned_positions_data = []
            for assigned_position in assigned_positions:
                assigned_positions_data.append({
                    'position_id': assigned_position.position_id,
                    'member_id': assigned_position.member_id.id,
                    'group_id': assigned_position.group_id.id,
                })
            return JsonResponse({
                'status': 'success',
                'assigned_positions': assigned_positions_data,
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

