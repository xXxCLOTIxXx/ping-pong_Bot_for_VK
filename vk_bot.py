# -*- coding: utf-8 -*-


#made by Xsarz (Telegram: https://t.me/DXsarz)
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


TOKEN ='your token'
GROUP_ID ='group id'
def main():
	vk_session = vk_api.VkApi(token=TOKEN)
	session_API = vk_session.get_api()
	longpoll = VkBotLongPoll(vk_session, GROUP_ID)
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			ct =  event.message.text.lower()
			content = str(ct).lower().split(" ")
			user_id = event.message.from_id
			peer_id = event.message.peer_id
			user_first_name = session_API.users.get(user_ids = (user_id))[0]['first_name']
			user_last_name = session_API.users.get(user_ids = (user_id))[0]['last_name']
			print(f'\n\n\nКто написал: {user_first_name} {user_last_name}\nЧто написал: {ct}')
			if content[0][0] == '/':
				if content[0][1:] == 'ping':
					session_API.messages.send(peer_id=peer_id, message='Pong!', random_id=0)
				elif content[0][1:] == 'pong':
					session_API.messages.send(peer_id=peer_id, message='Ping!', random_id=0)

if __name__ == '__main__':
	main()