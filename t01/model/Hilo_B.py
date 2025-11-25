import threading

class Hilo_B(threading.Thread):
    def run(self):
        for _ in range(30):
            print("YES")