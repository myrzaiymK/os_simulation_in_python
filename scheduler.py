from collections import deque


class Process:
    def __init__(self, pid, name, total_time):
        self.pid = pid
        self.name = name
        self.remaining_time = total_time  # how many times else it needs

    def run(self, quantum):
        time_used = min(self.remaining_time, quantum)
        self.remaining_time -= time_used
        print(f"RUNNING: {self.name} PID: {self.pid} → {time_used} ед. времени, осталось: {self.remaining_time} ")
        return self.remaining_time <= 0

    def __repr__(self):
        return f"<Process {self.name} (PID {self.pid}) — осталось {self.remaining_time} ед. времени>"


class RoundRobinScheduler:
    def __init__(self, quantum):
        self.queue = deque()
        self.pid_counter = 1
        self.quantum = quantum

    def add_process(self, name, total_time):
        process = Process(self.pid_counter, name, total_time)
        self.queue.append(process)
        print(f"[ADDED] {process}")
        self.pid_counter += 1

    def run(self):
        print("\n[STARTING SCHEDULER]\n")
        while self.queue:
            process = self.queue.popleft()
            finished = process.run(self.quantum)
            if not finished:
                self.queue.append(process)
            else:
                print(f"[FINISHED] {process.name} (PID {process.pid}) завершён\n")
            print("[ALL TASKS COMPLETE]")


scheduler = RoundRobinScheduler(quantum=9)
scheduler.add_process("Text Editor", 5)
scheduler.add_process("Browser", 8)
scheduler.add_process("Music Player", 3)

scheduler.run()
