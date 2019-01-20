## Story 001
* greet
    - utter_greet

	
## Story 002
* goodbye
    - utter_goodbye

	
## Story 003
* thankyou
	- utter_thankyou	



## Story 003_1
* restaurant_search
	- utter_ask_location


## Null entity
## Story 004 - full positive flow starting from null entity and opt email
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 004_1 - full positive flow starting from null entity and opt email with email address
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 005 - full positive starting from null entity and opt no email
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* deny
	- utter_thankyou



## Story 005_1 - full positive starting from null entity and opt no email with no result
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye




## Story 006 - starting from null entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 006_1 - starting from null entity and location not valid in first attempt but valid in the second attempt with email address
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou

	

## Story 006_1 - starting from null entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye


	
	
## Story 007 - starting from null entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	
	
	
## Single entity
## Story 008 - full positive flow starting with location and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 008_1 - full positive flow starting with location and opt email with email address
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 009 - full positive flow starting with location and opt no email
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* deny
	- utter_thankyou



## Story 009_1 - full positive flow starting with location and opt no email with no result
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye

	

## Story 010 - starting with location entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 010_1 - starting with location entity and location not valid in first attempt but valid in the second attempt with email address
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou

	
	
## Story 010_1 - starting with location entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye



	
## Story 011 - starting with location entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	



## Story 012 - full positive flow starting with cuisine and opt email
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location	
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 012_1 - full positive flow starting with cuisine and opt email with email address
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location	
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 013 - full positive flow starting with cuisine and opt no email
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* deny
	- utter_thankyou



## Story 013_1 - full positive flow starting with cuisine and opt no email with no results
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye




## Story 014 - starting with cuisine entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 014_1 - starting with cuisine entity and location not valid in first attempt but valid in the second attempt with email address
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 014_1 - starting with cuisine entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye


	
	
## Story 015 - starting with cuisine entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	




## Story 016 - full positive flow starting with budget and opt email
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou




## Story 016_1 - full positive flow starting with budget and opt email with email address
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 017 - full positive flow starting with budget and opt no email
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* deny
	- utter_thankyou



## Story 017_1 - full positive flow starting with budget and opt no email with no results
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye




## Story 018 - starting with budget entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 018_1 - starting with budget entity and location not valid in first attempt but valid in the second attempt with email address
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou
	


	
## Story 018_1 - starting with budget entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye


	
	
## Story 019 - starting with budget entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	



## Story 020 - full positive flow starting with email and opt email
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 020_1 - full positive flow starting with email and opt email with no results
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye



## Story 021 - starting with email entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou

	
	
## Story 022 - starting with email entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	
	
	

## Double entity
## Story 023 - full positive flow starting with location and cuisine and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 023_1 - full positive flow starting with location and cuisine and opt email with email address
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou

	

## Story 024 - full positive flow starting with location and cuisine and opt no email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* deny
	- utter_thankyou



## Story 024_1 - full positive flow starting with location and cuisine and opt no email with no results
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye



## Story 025 - starting with location and cuisine entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 025_1 - starting with location and cuisine entity and location not valid in first attempt but valid in the second attempt with email address
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 025_2 - starting with location and cuisine entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye



	
## Story 026 - starting with location and cuisine entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine": "chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	





## Story 027 - full positive flow starting with location and budget and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 027_1 - full positive flow starting with location and budget and opt email with email address
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 028 - full positive flow starting with location and budget and opt no email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* deny
	- utter_thankyou



## Story 028_1 - full positive flow starting with location and budget and opt no email with no results
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye




## Story 029 - starting with location and budget entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 029_1 - starting with location and budget entity and location not valid in first attempt but valid in the second attempt with email address
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 029_2 - starting with location and budget entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye


	
	
## Story 030 - starting with location and budget entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	




## Story 031 - full positive flow starting with location and email and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","email":"abc@xyz.com"}
	- slot{"location": "delhi"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou




## Story 032 - starting with location and email entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","email":"abc@xyz.com"}
	- slot{"location": "delhi"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou

	

## Story 032_1 - starting with location and email entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"location":"delhi","email":"abc@xyz.com"}
	- slot{"location": "delhi"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye



	
## Story 033 - starting with location and email entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","email":"abc@xyz.com"}
	- slot{"location": "delhi"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	




## Story 034 - full positive flow starting with cuisine and budget and opt email
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou




## Story 034_1 - full positive flow starting with cuisine and budget and opt email with email address
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou

	

## Story 035 - full positive flow starting with cuisine and budget and opt no email
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* deny
	- utter_thankyou



## Story 035_1 - full positive flow starting with cuisine and budget and opt no email with no results
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye




## Story 036 - starting with cuisine and budget entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou

	

## Story 036_1 - starting with cuisine and budget entity and location not valid in first attempt but valid in the second attempt with email address
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou




## Story 036_1 - starting with cuisine and budget entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye

	
	

## Story 037 - starting with cuisine and budget entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	





## Story 038 - full positive flow starting with email and budget and opt email
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","budget":"300"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou




## Story 039 - starting with email and budget entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","budget":"300"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 039_1 - starting with email and budget entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","budget":"300"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}	
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye


	
	
## Story 040 - starting with email and budget entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","budget":"300"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	




## Story 041 - full positive flow starting with email and cuisine and opt email
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","cuisine":"chinese"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"cuisine":"chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget":"300"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou




## Story 042 - starting with email and cuisine entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","cuisine":"chinese"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"cuisine":"chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget":"300"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 042_1 - starting with email and cuisine entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","cuisine":"chinese"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"cuisine":"chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget":"300"}	
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye


	
	
## Story 043 - starting with email and cuisine entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","cuisine":"chinese"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"cuisine":"chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	



## Triple entities
## Story 044 - full positive flow starting with location, cuisine and budget and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 044_1 - full positive flow starting with location, cuisine and budget and opt email with email address
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 045 - full positive flow starting with location, cuisine and budget and opt no email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* deny
	- utter_thankyou



## Story 045_1 - full positive flow starting with location, cuisine and budget and opt no email with no results
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye




## Story 046 - starting with location, cuisine and budget entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 046_1 - starting with location, cuisine and budget entity and location not valid in first attempt but valid in the second attempt with email address
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- utter_ask_email_needed
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_thankyou

	

## Story 046_1 - starting with location, cuisine and budget entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye


	
	
## Story 047 - starting with location, cuisine and budget entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	




## Story 048 - full positive flow starting with location, cuisine and email and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget":"300"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou




## Story 049 - starting with location, cuisine and email entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget":"300"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou



## Story 049_1 - starting with location, cuisine and email entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget":"300"}	
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye


	
	
## Story 050 - starting with location, cuisine and email entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	





## Story 051 - full positive flow starting with location, budget and email and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou




## Story 052 - starting with location, budget and email entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou

	

## Story 052_1 - starting with location, budget and email entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}	
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye



	
## Story 053 - starting with location, budget and email entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	




## Story 054 - full positive flow starting with cuisine, budget and email and opt email
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou




## Story 055 - starting with cuisine, budget and email entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou

	

## Story 055_1 - starting with cuisine, budget and email entity and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye



	
## Story 056 - starting with cuisine, budget and email entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	



## Four entities
## Story 057 - full positive flow starting with all entities and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"location": "delhi"}	
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou




## Story 058 - starting with all entities and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"location": "delhi"}
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- slot{"is_result_found": 1}
	- action_send_email
	- utter_email_status
	- utter_thankyou

	


## Story 058_1 - starting with all entities and location not valid in first attempt but valid in the second attempt with no results
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"location": "delhi"}
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- slot{"is_result_found": 0}
	- utter_goodbye


	
	
## Story 059 - starting with all entities and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"location": "delhi"}	
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye

	
