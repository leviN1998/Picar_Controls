import pygame
import sys
import socket

pygame.init()
pygame.display.set_caption("Test")
window = pygame.display.set_mode((100, 100))

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.26"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


class Direction:
    forward: bool
    backward: bool
    left: bool
    right: bool

    def __init__(self):
        self.forward = False
        self.backward = False
        self.left = False
        self.right = False

    def get_string(self):
        out = ""
        if self.forward:
            out += "1"
        else:
            out += "0"
        if self.backward:
            out += "1"
        else:
            out += "0"
        if self.left:
            out += "1"
        else:
            out += "0"
        if self.right:
            out += "1"
        else:
            out += "0"
        return out


while True:
    pygame.time.Clock().tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dir = Direction()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w]:
        dir.forward = True
    if pressed_keys[pygame.K_s]:
        dir.backward = True
    if pressed_keys[pygame.K_a]:
        dir.left = True
    if pressed_keys[pygame.K_d]:
        dir.right = True

    send(dir.get_string())
    window.fill((0, 0, 0))
    pygame.display.update()




