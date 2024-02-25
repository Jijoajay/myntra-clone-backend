import random
from twilio.rest import Client
from django.conf import settings

TWILIO_USERNAME = "lcatejas120@gmail.com"
TWILIO_PASSWORD = "Jijo@123#Jijo@123#"
TWILIO_ACCOUNT_SID = "AC865c605dc24100a2b54ba9e1b3ca200b"
TWILIO_ACCOUNT_TOKEN = "f4bca41991c4a379336212c27d22a20f"
TWILIO_PHONE_NUMBER = "+16593992305"
def generate_otp():
    return str(random.randint(1000, 9999))

def send_otp_via_sms(phone_number, otp):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_TOKEN)
    message = client.messages.create(
        from_ = TWILIO_PHONE_NUMBER,
        to= "+91"+phone_number,
        body="Your OTP is: %s"%otp
    )
    return message.sid
        
