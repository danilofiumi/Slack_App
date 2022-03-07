import slack
from flask import Flask, request,Response ,make_response
from slackeventsapi import SlackEventAdapter
from dotenv import load_dotenv
import os
from pathlib import Path
from classmrkdwn import WelcomeMessage, send_welcome_message
from esempiomkdwn import mex
import json
from datetime import datetime
from blocco_scelta_date import blks


env_path=Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
	os.environ['SLACK_SIGNING_SECRET'], '/slack/event', app)

client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

in_dt=datetime.today().strftime('%Y-%m-%d')
out_dt=datetime.today().strftime('%Y-%m-%d')
in_date = in_dt
to_date = out_dt

blocks=blks(in_dt,out_dt)


@app.route('/time-off', methods=['POST'])
def message_count():
	data= request.form
	print(data)
	user_id=data.get('user_id')
	channel_id = data.get('channel_id')
	client.chat_postMessage(channel=channel_id,**blocks)
	return Response(), 200



@app.route("/slack/message_actions", methods=["POST"])
def message_actions():

	# Parse the request payload
	form_json = json.loads(request.form["payload"])
	print(form_json)
	# Check to see what the user's selection was and update the message
	global in_date
	global to_date
	global out_dt
	global in_dt

	if form_json["actions"][0]["type"] =='datepicker':
		selected_date=form_json["actions"][0]["selected_date"]
		print(selected_date)
		action_id = form_json["actions"][0]["action_id"]
		print(action_id)
		# initialize the date for new iteration


		if action_id == "actionId-0":
			in_date=selected_date

			# update if move forward
			in_dt=selected_date
			if (in_dt > out_dt):
				out_dt = selected_date
				to_date = selected_date
				blocks1=blks(in_dt,out_dt)


				client.chat_update(channel=form_json["channel"]["id"], ts=form_json["container"]["message_ts"], **blocks1)
		elif action_id == "actionId-1":
			to_date=selected_date


	elif form_json["actions"][0]["value"] == "click_me_123":
		# button = form_json["actions"][0]["value"]
		# if button == "click_me_123":
			message_text = ":white_check_mark: Request processed! Wait the answer"
			global main_channel
			global main_ts

			main_channel=form_json["channel"]["id"]
			main_ts=form_json["container"]["message_ts"]
			client.chat_update(channel=form_json["channel"]["id"], ts=form_json["container"]["message_ts"],text=message_text, blocks=[])

			f = open("demofile2.txt", "w")
			f.write("data di inizio = "+ in_date + ", data di fine = "+ to_date)
			f.close()

			# send to manager
			yes_or_no={
		"blocks": [
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Yes",
						"emoji": True
					},
					"value": "yes",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "No",
						"emoji": True
					},
					"value": "no",
					"action_id": "actionId-1"
				}
			]
		}
	]
}
			client.chat_postMessage(channel="D01HVCQHZ8C", **yes_or_no)
	else:
		answer=form_json["actions"][0]["value"]
		print(answer)
		if answer =="yes":
			client.chat_postMessage(channel=main_channel,
								   text=":heavy_check_mark: your time-off request from "
										+ in_date + " to " + to_date +" has been approved!", blocks=[])
		else:
			client.chat_postMessage(channel=main_channel,
							   text=":heavy_multiplication_x: your request for time off from "
									+ in_date + " to " + to_date + " has been denied!", blocks=[])
		client.chat_update(channel=form_json["channel"]["id"], ts=form_json["container"]["message_ts"],
						   text="Done", blocks=[])
		# reinitialize the date for new iteration
		in_date = datetime.today().strftime('%Y-%m-%d')
		to_date = datetime.today().strftime('%Y-%m-%d')

	return make_response("", 200)


if __name__ == "__main__":
	app.run(debug=True)
