from authentication.models import ReferralCode,Organization
import random
def generate_referral_code():
    try:
        prefix = "AAR"
        random_digits = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        referral_code = prefix + random_digits
        ref_obj = ReferralCode.objects.get_or_create(code=referral_code) 
        ref_obj.referral_count +=1
        ref_obj.save()
    except Exception as e:
        print("Exception in generate referral code :"+str(e))
    
    return referral_code

def create_organization(name,city,type,referral):
    status = "Success"
    try:
        org_obj = Organization.objects.create(name=name)
        org_obj.city = city
        org_obj.type = type
        ref_obj = ReferralCode.objects.get(code=referral)
        ref_obj.referral_count+=1
        ref_obj.save()
        org_obj.referral = ref_obj
        org_obj.save()
        org_id = org_obj.pk
        
        
    except Exception as e:
        status = "Exception in create organization :"+str(e)
        org_id = ""
        print(status)   
    return status,org_id
    