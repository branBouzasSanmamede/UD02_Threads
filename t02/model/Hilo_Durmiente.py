import threading, time

class Hilo_Durmiente(threading.Thread):
    def run(self):
        time.sleep(2)