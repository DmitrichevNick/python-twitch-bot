from datetime import datetime
import asyncio
from socket import timeout
import time
from twitchio import Channel

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
    
    def listen_input(self, chat:Channel):
        print('listen_input')
        message = ''
        loop = asyncio.new_event_loop()
        while self.listen:
            message = input()
            words = message.split(' ')
            if words[0].lower() == "put":
                if len(self.messages) > 0 and message[(len("put")+1):] == self.messages[-1]:
                    continue
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
                if len(self.messages) == 0:
                    continue
                
                tasks = []
                for message in self.messages:
                    tasks.append(loop.create_task(chat.send(message)))
                    tasks.append(loop.create_task(self.asyncSleep(1)))
                loop.run_until_complete(asyncio.wait(tasks))
                loop.run_until_complete(loop.create_task(self.clear()))
            elif words[0].lower() == 'sys:exit':
                loop.close()
                quit()
            
    async def clear(self):
        self.messages = []
        
    async def asyncSleep(self, time_s):
        time.sleep(time_s)
        
    def get_messages(self):
        return self.messages
