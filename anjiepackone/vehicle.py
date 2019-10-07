import logging

class Vehicle:
    def __init__(self, type):
        self.type = type

    def drive(self):
        logging.info('Driving')

    def horn(self):
        logging.info('Honking')