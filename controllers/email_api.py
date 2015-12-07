# -*- coding: utf-8 -*-
import json

#API Features
def check_email():
	"""
	This call checks if the email is already in database, confirmed or primary and then returns the results.
	"""
	data = json.loads(request.body.read())
	emails = data["email"]
	email_list = []
	response = {}
	for email in emails:
		email_list.append(str(email))

	existing_emails = db(db.user_email.email_address.belongs(email_list)).select()

	for item in email_list:
		for email in existing_emails:
			if item == email.email_address and email.confirmed == 1:
				query = db(db.user_email.user_id == email.user_id).select(orderby = ~db.user_email.login_time)
				for entry in query:
					if entry.primary_key == 1:
						response[item] = entry.email_address
						break
					else:
						response[item] = entry.email_address
			elif item == email.email_address and email.confirmed == 0:
				response[item] = None
	else:
		response[item] = None
			
	return dict (email = response)