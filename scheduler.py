class Process:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name


class Scheduler:
    def __init__(self):
        self.queue = []

    def add_process(self, process):
        self.queue.append(process)

    def run(self):
        while self.queue:
            proc = self.queue.pop(0)
            print(f"Running process: {proc.name} (PID {proc.pid})")


scheduler = Scheduler()
scheduler.add_process(Process(1, "Chrome"))
scheduler.add_process(Process(2, "Text Editor"))
scheduler.run()
