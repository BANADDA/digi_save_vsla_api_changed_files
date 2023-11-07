# views/positions_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Positions
from digi_save_vsla_api.serializers import PositionsSerializer

@api_view(['GET', 'POST'])
def positions_list(request):
    data = request.data
    print("Received data:", data)
    try:
        if request.method == 'POST':
            
            print("Received data:", data)
            name = data.get('name')
            sync_flag = data.get('sync_flag')

            group_members = Positions(
                name=name,
                sync_flag=sync_flag,
            )
            group_members.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Positions created successfully',
            })

        if request.method == 'GET':
            groupMembers = Positions.objects.all()
            group_member_data = []
            for group_member in groupMembers:
                group_member_data.append({
                    'name': group_member.name,
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
def positions_detail(request, pk):
    try:
        position = Positions.objects.get(pk=pk)
    except Positions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PositionsSerializer(position)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PositionsSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
