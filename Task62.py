# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 13:29:48 2021

@author: Fetibek Aliev
"""

class Massage:
    
    def __init__(self, sender,  text):
        self.sender = sender
        self.text = text
        
    def __str__(self):
        return "Message [sender = " + str(self.sender + " , text = " + str(self.text) + "]")
        
class MessageBox:
    
    def __init__(self):
        self.messages = []
    
    def add_message(self, message):
        self.messages.append(message)
    
    def get_last_massage(self):
        if len(self.messages) == 0:
            return None
        else:
           message = self.massages[len(self.messages)]
           return message
    def __str__(self):
        return str(self.message)
                                

message_box_1 = MessageBox()

massage1 = Massage("Alex", "Salom")
massage2 = Massage("Anton", "Salom Fetuha")

message_box_1.add_message(massage1)
message_box_1.add_message(massage2)

print(massage1)
print(massage2)

print(message_box_1)

