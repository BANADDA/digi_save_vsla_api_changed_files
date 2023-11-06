from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Users
from digi_save_vsla_api.serializers import UsersSerializer

@api_view(['GET', 'POST'])
def users_list(request):
    data = request.data
    print("Received data:", data.get('fname'), data.get('lname'))
    try:
        if request.method == 'POST':
            
            print("Received data:", data)
            unique_code = data.get('unique_code')
            fname = data.get('fname')
            lname = data.get('lname')
            email = data.get('email')
            phone = data.get('phone')
            sex = data.get('sex')
            country = data.get('country')
            date_of_birth = data.get('date_of_birth')
            image = data.get('image')
            district = data.get('district')
            subCounty = data.get('subCounty')
            village = data.get('village')
            number_of_dependents = data.get('number_of_dependents')
            family_information = data.get('family_information')
            next_of_kin_name = data.get('next_of_kin_name')
            next_of_kin_has_phone_number = data.get('next_of_kin_has_phone_number')
            next_of_kin_phone_number = data.get('next_of_kin_phone_number')
            pwd_type = data.get('pwd_type')
            sync_flag = data.get('sync_flag')

            group_profile = Users(
                unique_code=unique_code,
                fname=fname,
                lname=lname,
                email=email,
                phone=phone,
                sex=sex,
                country=country,
                date_of_birth=date_of_birth,
                image=image,
                district=district,
                subCounty=subCounty,
                village=village,
                number_of_dependents=number_of_dependents,
                family_information=family_information,
                next_of_kin_name=next_of_kin_name,
                next_of_kin_has_phone_number=next_of_kin_has_phone_number,
                next_of_kin_phone_number=next_of_kin_phone_number,
                pwd_type=pwd_type,
                sync_flag=sync_flag,
            )
            group_profile.save()

            return JsonResponse({
                'status': 'success',
                'message': 'User profile created successfully',
            })

        if request.method == 'GET':
            user_profiles = Users.objects.all()
            user_profile_data = ()
            for user_profile in user_profiles:
                user_profile_data.append({
                    'id': user_profile.id,
                    'unique_code': user_profile.unique_code,
                    'fname': user_profile.fname,
                    'lname': user_profile.lname,
                    'email': user_profile.email,
                    'phone': user_profile.phone,
                    'sex': user_profile.sex,
                    'country': user_profile.country,
                    'date_of_birth': user_profile.date_of_birth,
                    'image': user_profile.image,
                    'district': user_profile.district,
                    'subCounty': user_profile.subCounty,
                    'village': user_profile.village,
                    'number_of_dependents': user_profile.number_of_dependents,
                    'family_information': user_profile.family_information,
                    'next_of_kin_name': user_profile.next_of_kin_name,
                    'next_of_kin_has_phone_number': user_profile.next_of_kin_has_phone_number,
                    'next_of_kin_phone_number': user_profile.next_of_kin_phone_number,
                    'pwd_type': user_profile.pwd_type,
                    'sync_flag': user_profile.sync_flag,
                })
            return JsonResponse({
                'status': 'success',
                'user_profiles': user_profile_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
