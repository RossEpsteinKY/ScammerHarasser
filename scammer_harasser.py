from twilio.rest import TwilioRestClient
import time

#Your twilio number
YOUR_NUMBER = ""

#Put mass call number(s) here
CHOSEN_NUMBERS = ["",]

# URL location of TwiML instructions for how to handle the phone call
XML_URL = \
  ""

#your twilio info
client = TwilioRestClient("", "")


def call_number(numbers):
    for number in numbers:
        print("Calling the following phone number:  " + number)

        client.calls.create(to=number, from_=YOUR_NUMBER,
                            url=XML_URL, method="GET")



    
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
    call_number(CHOSEN_NUMBERS)

def run_again():
    program_loop()
            

program_start()

