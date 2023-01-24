from password_strength import PasswordStats

def get_entopy(password):
    stats=PasswordStats(password)
    if(stats.entropy_bits<45):
        state="weak"
    elif(stats.entropy_bits<80):
        state="medium"
    elif(stats.entropy_bits<=110):
        state="strong"
    else:
        state="very strong"
    return int(stats.entropy_bits),state