from authentication.models import Organization,ApiKey,ReferralCode
import jwt
import secrets
from decouple import config
from cryptography.fernet import Fernet
import base64
import hashlib
def create_api_key(org_name,referral):
    status = "Success"
    api_key = ""
    try:
        org_obj = Organization.objects.get(name=org_name)
        ref_obj = ReferralCode.objects.get(code=referral)
        if org_obj and ref_obj:
            print(org_obj.referral)
            print(ref_obj)
            api_key = secrets.token_hex(15)
            secret_key = config('API_GENERATION_KEY')
            repeated_key = (secret_key* (len(api_key) // len(api_key) + 1))[:len(secret_key)]

            # Applingy XOR operation character by character
            encoded_key = ''.join(chr(ord(char) ^ ord(key_char)) for char, key_char in zip(api_key, repeated_key))
            api_obj = ApiKey.objects.create(key=encoded_key)
            api_obj.organization = org_obj
            api_obj.save()
        else:
            status = "Invalid org or referral"
    except Exception as e:
        status = "Exception in generating API Key:"+str(e)
        api_key = ""
        print(status)
    return status,api_key                    