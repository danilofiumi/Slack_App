def blks(in_dt,out_dt):
    blocks={
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "This is a plain text section block.",
				"emoji": True
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "datepicker",
					"initial_date": in_dt,
					"placeholder": {
						"type": "plain_text",
						"text": "Select a date",
						"emoji": True
					},
					"action_id": "actionId-0"
				},
				{
					"type": "datepicker",
					"initial_date":out_dt ,
					"placeholder": {
						"type": "plain_text",
						"text": "Select a date",
						"emoji": True
					},
					"action_id": "actionId-1"
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Click Me",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				}
			]
		}
	]
}
    return blocks