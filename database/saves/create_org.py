from authentication.models import ReferralCode,Organization
import random
async def generate_referral_code():
    ref_obj = ""
    try:
        prefix = "AAR"
        random_digits = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        referral_code = prefix + random_digits
        ref_obj = await ReferralCode.objects.acreate(code=referral_code) 
        ref_obj.referral_count +=1
        await ref_obj.asave()
    except Exception as e:
        print("Exception in generate referral code :"+str(e))
    
    return referral_code

async def create_organization(name,city,type,referral):
    status = "Success"
    try:
        org_obj = await Organization.objects.acreate(name=name)
        org_obj.city = city
        org_obj.type = type
        ref_obj = await ReferralCode.objects.aget(code=referral)
        ref_obj.referral_count+=1
        await ref_obj.asave()
        org_obj.referral = ref_obj
        await org_obj.asave()
        org_id = org_obj.pk
        
        
    except Exception as e:
        status = "Exception in create organization :"+str(e)
        org_id = ""
        print(status)   
    return status,org_id
    