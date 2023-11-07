from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import GroupFees, GroupForm, GroupMembers
from digi_save_vsla_api.serializers import GroupFeesSerializer

@api_view(['GET', 'POST'])
def group_fees_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            member_id = data.get('member_id')
            group_id = data.get('group_id')
            registration_fee = data.get('registration_fee')

            # Get the related instances based on their IDs
            member = GroupMembers.objects.get(id=member_id)
            group = GroupForm.objects.get(id=group_id)

            fee = GroupFees(
                member=member,
                group_id=group,
                registration_fee=registration_fee,
            )
            fee.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Fee created successfully',
            })

        if request.method == 'GET':
            fees = GroupFees.objects.all()
            fee_data = []
            for fee in fees:
                fee_data.append({
                    'member_id': fee.member.id,
                    'group_id': fee.group_id.id,
                    'registration_fee': fee.registration_fee,
                })
            return JsonResponse({
                'status': 'success',
                'fees': fee_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def group_fees_detail(request, pk):
    try:
        group_fees = GroupFees.objects.get(pk=pk)
    except GroupFees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupFeesSerializer(group_fees)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupFeesSerializer(group_fees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_fees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)