class ChatRoom(object):
    def displayMessage(self, user, message):
        print("[{} says]: {}".format(user, message))
 
class User(object):
    def __init__(self, name):
        self.name = name
        self.chatRoom = ChatRoom()
 
    def sendMessage(self, message):
        self.chatRoom.displayMessage(self, message)
 
    def __str__(self):
        return self.name
 
jorge = User('Jorge')
oliver = User('Oliver')
kevin = User('Kevin')
 
jorge.sendMessage("¡Hola equipo! Reunión hoy a las 3 p.m.")
oliver.sendMessage("¡Entendido!")
kevin.sendMessage("Esta bien.")
