# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import Reservation
import Restaurant
import unicodedata



app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms():
	reservInfo = " "
    # Start our response

	resp = MessagingResponse()

	#user input
	message_body = request.form['Body']
	
	count = 0
	name = " "
	time = " "

	file = open("Reservations.txt", "a")

	#check for # of spaces, if two words assume data correct
	for i in range(len(message_body)-1):
   		if message_body[i] == " ":
   			count = count + 1

   	#Parse the user response to a name and time
   	if count == 1:
   		for i in range(len(message_body)-1):
   			if message_body[i] == " ": #first space
   				name = message_body[0:i]
   				time = message_body[i+1:len(message_body)]
   				print name
   				print time
   		#if time is not a number, request user to enter a valid number
   		if is_number(time) == False: 
   			resp.message('Please input time as a valid number.')
   			return str(resp)


		#If reservation time is not booked, create a reservation
		res = Reservation.Reservation(name, time)
		rest = Restaurant.Restaurant()
		if rest.add_reservation(res.get_time()) == True:
			resp.message('Your reservation is confirmed. Thank you!')
			file.write(res.get_name())
			file.write(" ")
			file.write(str(res.get_time()))

			file.close()
			return str(resp)    
		#Request user select another time
		else:
			resp.message('This time is booked. Select another time.')
			return str(resp)
			#run alternate_reservation method to give user options
			# temp_times = resp.message(rest.alternate_reservation(res.get_time()))
			# for t in temp_times:


			# resp.message('This time is taken. Please pick another')
			# return str(resp)
		
	else:
		#tell them to send the correct information
		print "checkpoint 1"
		resp.message('Welcome to Entree! Send us your last name and the time.')
		return str(resp)



def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
	return False



if __name__ == "__main__":
    app.run(debug=True)
