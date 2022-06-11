from datetime import datetime
import asyncio

class MessageCollector():
    def __init__(self):
        print('create')
        self.create_time = datetime.now().strftime("%H:%M:%S")

    def start(self):
        print('start')
        self.start_time = datetime.now().strftime("%H:%M:%S")
        self.messages = []
        self.listen = True
    
    def stop(self):
        print('stop')
        self.listen = False
    
    def listen_input(self, chat):
        print('listen_input')
        message = ''
        while self.listen:
            message = input()
            words = message.split(' ')
            if words[0].lower() == "put":
                self.messages.append(message[(len("put")+1):])
                print(str(len(self.messages))+" messages")
            elif words[0].lower() == "end":
                self.listen = False
            elif words[0].lower() == 'clear':
                print('clear')
                self.messages = []
            elif words[0].lower() == 'get':
                print('get')
                return self.get_messages()
            elif words[0].lower() == 'pop':
                loop = asyncio.new_event_loop()
                tasks = [loop.create_task(chat.send(message)) for message in self.messages]
                loop.run_until_complete(asyncio.wait(tasks))
                self.messages = []
            
    def clear(self):
        self.messages = []
        
    def get_messages(self):
        return self.messages