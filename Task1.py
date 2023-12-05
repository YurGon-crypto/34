import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for _ in range(self.rounds):
            self.counter += 1


counter_thread1 = Counter()
counter_thread2 = Counter()

counter_thread1.start()
counter_thread2.start()


counter_thread1.join()
counter_thread2.join()


result = counter_thread1.counter + counter_thread2.counter
print(f"Final Counter Value: {result}")

