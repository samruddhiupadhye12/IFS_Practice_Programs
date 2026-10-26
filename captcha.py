import string, random

def generate_captcha():
    return ''.join(random.choices( string.ascii_letters + string.digits, k=5))

captcha = generate_captcha()
print("Captcha : ",captcha)
input_captcha = input("Enter captcha : ")

if captcha == input_captcha:
    print("Valid Captcha.!")
else:
    print("Invalid Captcha.!")