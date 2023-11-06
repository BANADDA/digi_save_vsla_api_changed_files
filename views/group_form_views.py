# views/group_form_views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import GroupForm
from digi_save_vsla_api.serializers import GroupFormSerializer

@api_view(['GET', 'POST'])
def group_form_list(request):
    if request.method == 'GET':
        group_forms = GroupForm.objects.all()
        serializer = GroupFormSerializer(group_forms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroupFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def group_form_detail(request, pk):
    try:
        group_form = GroupForm.objects.get(pk=pk)
    except GroupForm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupFormSerializer(group_form)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupFormSerializer(group_form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
