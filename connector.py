import bluetooth
import pygame


name = 'BT04-A'
target_device = '98:DA:20:03:B0:4B'


class Connector:
    def __init__(self):
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.sock.connect((target_device, 1))
        self.sock.settimeout(2)
        self.write()

    def connect(self):
        self.sock.close()
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.sock.connect((target_device, 1))
        self.sock.settimeout(2)

    def send(self, message: str):
        self.sock.send(message)

    def write(self):
        message = self.sock.recv(1024)
        return message

    def connected(self):
        try:
            self.send('z')
            message = self.sock.recv(1024)
            return True
        except Exception:
            return False

    def close(self):
        self.sock.close()
