from twilio.rest import TwilioRestClient
import time

#Your twilio number
TWILIO_PHONE_NUMBER = ""

#Put mass call number(s) here
DIAL_NUMBERS = ["",]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  ""

#your twilio info
client = TwilioRestClient("", "")


def dial_numbers(numbers_list):
    for number in numbers_list:
        print("Calling the following phone number:  " + number)

        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")
    
def program_start():
    keepcalling = input("Would you like to place indefinite calls?   >")
    if keepcalling.lower() == "yes":
        program_loop()
    else:
        print("Say 'yes' when ready")
        program_start()
     
def program_loop():
    loop_dial()        
    time.sleep(10)
    run_again()

def loop_dial():
    dial_numbers(DIAL_NUMBERS)

def run_again():
    program_loop()

program_start()

