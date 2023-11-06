from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from digi_save_vsla_api.auth import PhoneCodeBackend

@csrf_exempt
def login_with_phone_code(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        code = request.POST.get('code')
        print('phone:', phone)
        print('code: ', code)
        user = PhoneCodeBackend().authenticate(request, phone=phone, code=code)
        print('User:', user)
        if user is not None:
            # Generate or retrieve the user's token
            # token, created = Token.objects.get_or_create(user=user)
            response_data = {
                'success': True,
                'user': {
                    'id': user.id,
                    'fname': user.fname,
                    'lname': user.lname,
                    'email': user.email,
                    'phone': user.phone,
                    'sex': user.sex,
                    'country': user.country,
                    'date_of_birth': user.date_of_birth,
                    'image': user.image,
                    'district': user.district,
                    'subCounty': user.subCounty,
                    'village': user.village,
                    'number_of_dependents': user.number_of_dependents,
                    'family_information': user.family_information,
                    'next_of_kin_name': user.next_of_kin_name,
                    'next_of_kin_has_phone_number': user.next_of_kin_has_phone_number,
                    'next_of_kin_phone_number': user.next_of_kin_phone_number,
                    'pwd_type': user.pwd_type,
                },
            }
            return JsonResponse(response_data)
        else:
            response_data = {
                'success': False,
                'message': 'Invalid phone number or unique code',
            }
            return JsonResponse(response_data)