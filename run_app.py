from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-517280283250-517151581972-522704850773-3a74027a8ec447414f150fd3f99b7fed', #app verification token
							'xoxb-517280283250-516736066865-320llLmqJ9AhAgwWNoYKu1uE', # bot verification token
							'8UaqjeCDtHZPv3wD8WYDoMcH', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
