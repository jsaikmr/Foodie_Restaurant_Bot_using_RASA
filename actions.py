import pandas as pd

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.events import AllSlotsReset
from rasa_core.events import Restarted

import zomatopy
import json
import smtplib
import sys

global_search_result = ''

class ActionSearchRestaurants(Action):
	def name(self):
		return "action_search_restaurant"

	def get_restaurants_by_budget(self, restaurants_list, budget):

		try:
			lst_name = []
			lst_address = []
			lst_budget = []
			lst_rating = []

			for rest in restaurants_list:
				lst_name.append(rest['restaurant']['name'])
				lst_address.append(rest['restaurant']['location']['address'])
				lst_budget.append(rest['restaurant']['average_cost_for_two'])
				lst_rating.append(rest['restaurant']['user_rating']['aggregate_rating'])

			restaurant_df = pd.DataFrame(columns=['name','address','budget','rating'])
			restaurant_df['name'] = lst_name
			restaurant_df['address'] = lst_address
			restaurant_df['budget'] = lst_budget
			restaurant_df['rating'] = lst_rating

			if budget < 300:
				restaurant_df = restaurant_df.loc[(restaurant_df['budget'] < 300)]
			elif budget >= 300 and budget <= 700:
				restaurant_df = restaurant_df.loc[(restaurant_df['budget'] >= 300) & (restaurant_df['budget'] <= 700)]
			else:
				restaurant_df = restaurant_df.loc[(restaurant_df['budget'] > 700)]

			restaurant_df = restaurant_df.sort_values(['rating'], ascending=False).reset_index()

			if len(restaurant_df) <= 0:
				return ''

			global global_search_result
			global_search_result = ''

			output = 'Showing you top rated restaurants:\n'
			for i, row in restaurant_df.head(10).iterrows():
				if i < 5:
					output = output + '{0}. {1} in {2} has been rated {3}'.format(i+1, row['name'], row['address'], row['rating']) + '\n'

				global_search_result = global_search_result + '{0}. {1} in {2} has been rated {3}'.format(i+1, row['name'], row['address'], row['rating']) + '\n'

			return output
		except:
			return ''


	def run(self, dispatcher, tracker, domain):
		try:
			loc = tracker.get_slot('location')
			cuisine = tracker.get_slot('cuisine')
			budget = int(tracker.get_slot('budget'))

			config={ "user_key":"<Zomato API Key>"}
			zomato = zomatopy.initialize_app(config)
			location_detail=zomato.get_location(loc, 1)

			ld_json = json.loads(location_detail)
			lat = ld_json["location_suggestions"][0]["latitude"]
			lon = ld_json["location_suggestions"][0]["longitude"]

			cuisines_dict= {'chinese':25,'mexican':73,'italian':55,'american':1,'south indian':85,'north indian':50}
			results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100)

			res_json = json.loads(results)
			response=""

			[AllSlotsReset()]

			if res_json['results_found'] == 0:
				response= "no result"
				dispatcher.utter_message(response)
				return [SlotSet('is_result_found',False)]
			else:
				response = self.get_restaurants_by_budget(res_json['restaurants'], budget)

				if response == '':
					response= "no result"
					dispatcher.utter_message(response)
					return [SlotSet('is_result_found',False)]
				else:
					dispatcher.utter_message(response)
					return [SlotSet('is_result_found',True)]
		except:
			response= "no result"
			dispatcher.utter_message(response)
			return [SlotSet('is_result_found',False)]


class ActionSlotReset(Action):
	def name(self):
		return 'action_slot_reset'

	def run(self, dispatcher, tracker, domain):
		return[AllSlotsReset()]

class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		tier1_city_list = [ 'ahmedabad','bangalore','chennai','delhi','hyderabad','kolkata','mumbai','pune' ]
		tier2_city_list = [ 'agra','ajmer','aligarh','allahabad','amravati','amritsar','asansol','aurangabad','bareilly','belgaum','bhavnagar','bhiwandi',
							'bhopal','bhubaneswar','bikaner','bokaro steel city','chandigarh','coimbatore','cuttack','dehradun','dhanbad','durg-bhilai nagar',
							'durgapur','erode','faridabad','firozabad','ghaziabad','gorakhpur','gulbarga','guntur','gurgaon','guwahati','gwalior',
							'hubli-dharwad','indore','jabalpur','jaipur','jalandhar','jammu','jamnagar','jamshedpur','jhansi','jodhpur','kannur','kanpur',
							'kakinada','kochi','kottayam','kolhapur','kollam','kota','kozhikode','kurnool','lucknow','ludhiana','madurai','malappuram',
							'mathura','goa','mangalore','meerut','moradabad','mysore','nagpur','nanded','nashik','nellore','noida','palakkad','patna',
							'pondicherry','raipur','rajkot','rajahmundry','ranchi','rourkela','salem','sangli','siliguri','solapur','srinagar','sultanpur',
							'surat','thiruvananthapuram','thrissur','tiruchirappalli','tirunelveli','tiruppur','ujjain','vijayapura','vadodara','varanasi',
							'vasai-virar city','vijayawada','visakhapatnam','warangal']

		try:

			loc = str(tracker.get_slot('location')).lower()

			if loc in tier1_city_list or loc in tier2_city_list:
				return [SlotSet('valid_location',"true")]
			else:
				return [SlotSet('valid_location',"false")]

		except:
			return [SlotSet('valid_location',"false")]


class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):

		try:
			global global_search_result

			recipient_email = tracker.get_slot('email')

			gmail_user = '<Email Id>'
			gmail_password = '<Password>'

			sender_addr = "gmail_user"
			to_addr = [str(recipient_email)]
			subject = 'Restaurant details from RestaurantBot'
			body_msg = """\
Hello, \n\n Thank you for using the Resturant-Bot by AkiPunSaiGan. Below are top rated restaurant results of your recent search.

%s

Bon Appitet. Enjoy your food and have a wonderful day.

Regards
Foodie Restaurant Bot Team
""" % ('\n'+ global_search_result)

# 			print(body_msg)
			message = 'Subject: {}\n\n{}'.format(subject, body_msg)
			try:
				server = smtplib.SMTP('smtp.gmail.com', 587)
				server.starttls()
				server.login(gmail_user, gmail_password)
				server.sendmail(sender_addr, to_addr, message)
				server.close()

				print('Email sent!')
			except:
				print('Something went wrong...')

		except:
			print('Something went wrong...')

		return[AllSlotsReset()]
