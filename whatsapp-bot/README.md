###Creating a WhatsApp chatbot
 via https://www.twilio.com/
first you need to create account in twilio
###### go to whatsapp <a href="https://www.twilio.com/console/sms/whatsapp/learn"> Try WhatsApp</a>
###### then you will find the message bellow:
Invite your friends to your Sandbox. Ask them to send 
a WhatsApp message to +1 415 523 8886 with code 
<b>join</b> two-phrases

and <b>WHEN A MESSAGE COMES IN</b> in this textbox add the link of your api call 
make sure your api link begin with https, if it is not please install ngrok and copy the ngrok url 
not localhost if you run it on your pc not on ssh

go to your mobile device and save twilio number +1 415 523 8886 for sandbox test
and after that open your whatsapp and send to twilio number
the following code:
<b>join</b> two-phrases

<b>Note: </b>the words two-phrases they are dummy words I wrote them here
.They will be in other words in your account


To Run Project
--------------
1. write the command python app.py 
2. then launch the ngrok 
3. copy the ngrok generated https link
4. go to whatsapp <a href="https://www.twilio.com/console/sms/whatsapp/learn"> Try WhatsApp</a>
5. in <b>WHEN A MESSAGE COMES IN</b> textbox add the ngrok link for bot api
6. save and Enjoy send and receive message 

