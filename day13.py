import pywhatkit as kit
import datetime
def send_message(phone,message):
    print(f"sending message{message}")
    kit.sendwhatmsg(phone,message,datetime.datetime.now().hour,datetime.datetime.now().minute+1)

reciepients={'+234 816 030 4930':'hi',
             '+234 913 037 1860':'hello'}
for phone,message in reciepients.items():
    send_message(phone,message)