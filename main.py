"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, request
import twilio.twiml
import re
import currency, weather, translate

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
 
@app.route("/", methods=['GET', 'POST'])
def texty():
	"""Respond to incoming calls with a simple text message."""
 
	#from_number = request.values.get('From', None)
	from_body = request.values.get('Body', None)
	body_string = str(from_body)
	actual_content = re.split('\s*@',body_string)

	message = "unchanged"
	if len(actual_content) > 1:
		if actual_content[1] == "translate":
			lang_from = actual_content[2]
			lang_to = actual_content[3]
			text = actual_content[4]
			message = translate.filler(lang_from, lang_to, text)
			#message = lang_from + " " + lang_to + " " + text
		elif actual_content[1] == "currency":
			conversion_rate = currency.getConversionRate(actual_content[2], actual_content[3])
			converted_amount = float(conversion_rate) * float(actual_content[4])
			message = format(converted_amount, '.2f')
		elif actual_content[1] == "temperature":
			city = re.split(',\s*',actual_content[3])
			message = weather.getWeather(city[0])
		elif actual_content[1] == "stock":
			message = "stock"
		else:
			message = "plah"
	else:
		message = "blah"

	resp = twilio.twiml.Response()
	resp.message(str(message))
	return str(resp)

@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
	"""Return a custom 500 error."""
	return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == "__main__":
    app.run()