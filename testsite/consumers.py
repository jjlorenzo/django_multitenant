from django_multitenant_sockets.decorators import has_permission_and_org
import logging
import json

logger = logging.getLogger(__name__)

def connect(message):
  logger.debug('connect')

def disconnect(message):
  logger.debug('disconnect')

#@has_permission_and_org('chat_interact')
def receive(message):
  logger.debug('receive: {}'.format(vars(message)))
  message.reply_channel.send({'text': message.content['text']})
  #check authorization based on message.type and message.user.org_pk()

#@has_permission_and_org('chat_interact')
def send(message):
  pass