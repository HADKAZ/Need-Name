import socket, json

class Communications:
	def __init__(self, host : tuple):
		self.host = host
		self.link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.link.connect(host)
		self.requests = ["new_user", "get_user", "get_map", "pixel_modification"]
		
	def ask(self, data : dict):
		if "id" in data and "request" in data and "payload" in data:
			if data["request"] in self.requests:
				self.link.send(self.translation_to(data))
				ans = self.link.recv(1000000) # 1 Mo max
				return self.translation_from(ans)
				
	def translation_from(self, message : bytes, encoding : str = 'utf-8'):
		"""Traduit un messages en bytes vers une forme python"""
		message = message.decode(encoding)
		return json.loads(message)

	def translation_to(self, message, encoding : str = 'utf-8'):
		message = json.dumps(message)
		return message.encode(encoding)
				
if __name__ == "__main__":
	Com = Communications(("192.168.1.236", 43298))
	while True:
		req = input()
		req = json.loads(req)
		ans = Com.ask(req)
		print(ans)