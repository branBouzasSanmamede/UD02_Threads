import threading

class Hilo_A(threading.Thread):
    def run(self):
        for _ in range(30):
            print("NO")