# Foodie Restaurant Bot using RASA

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities.

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience.

### Prerequisites:
Following are the versions of the packages used in the development environment

* Python Version		-  3.6.4
* Rasa_nlu Version 	- 0.12.3
* Rasa_core Version 	- 0.10.1

**Note:**
* Zomato apis can be generated using [https://developers.zomato.com/documentation#/](https://developers.zomato.com/documentation#/)

* Application demo can be viewed in Youtube using [https://youtu.be/d4BwwHnYVQY](https://youtu.be/d4BwwHnYVQY)


### Installing Rasa nlu:

$pip install rasa_nlu

### Install Rasa Core

* $git clone https://github.com/RasaHQ/rasa_core.git
* $cd rasa_core
* $pip install -r requirements.txt
* $pip install -e .

### To find version of rasa_core and rasa_nlu installed
* $python --version
* $python -c "import rasa_nlu; print(rasa_nlu.__version__);"
* $python -c "import rasa_core; print(rasa_core.__version__);"

### Steps to train the nlu data & train the core conversational flow using command line
1. cd path

2. Train the NLU

- $python .\nlu_model.py

3.Train Core

- $python .\train_init.py


**Run Dialogue management**


**Step 1: Run the action server**

```
	python -m rasa_core_sdk.endpoint --actions actions
```

**Step 2: Run the RASA Core**

```
	python -m rasa_core.run --nlu models/nlu/default/restaurantnlu --core models/dialogue --endpoints endpoints.yml
```

**Slack Integration**

```
python -m rasa_core.run -d models/dialogue -u models/nlu/default/restaurantnlu --endpoints endpoints.yml --port 5002 --connector slack --credentials slack_credentials.yml
```

**To train the nlu data & train the core conversational flow using python code**

1. cd path 
2. $python .\nlu_model.py
3. $python .\train_init.py


**To verify the bot command line**

$python .\dialogue_management_model.py


### Train dialogue flow online and add the strories

$python .\train_online.py

Generated stories can be exported to a path and then added to stories.md. Retrain the model and check dialogue flow.


## Deployment to slack

Run the bot on local sever and integrate with slack.

Using ngrok (https://ngrok.com/download) as a webhook deploy the bot on slack(https://slack.com/). Create a bot in slack and integrate the credentials in run_app.py program.

$python .\run_app.py  

Bot can be accessed from slack. 
 

## Framework and Libraries used.

* Rasa
* Keras Framework
* Tensorflow
* Slack
