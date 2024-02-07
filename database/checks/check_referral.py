from authentication.models import ReferralCode

def check_referral_code(referral):
    status = "Success"
    check =False
    try:
        referral_obj = ReferralCode.objects.filter(code=referral).values_list()
        if len(referral_obj):
            check = True
        else:
            check = False
    except Exception as e:
        status = "Exception in checking referral code :"+str(e)         
        print(status)
        check = False
    return check,status    
        