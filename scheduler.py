from collections import deque


class Process:
    def __init__(self, pid, name, total_time, priority):
        self.pid = pid
        self.name = name
        self.remaining_time = total_time  # how many times else it needs
        self.priority = priority
        self.wait_time = 0

    def maybe_promote(self, max_wait=3):
        self.wait_time += 1
        if self.wait_time >= max_wait and self.priority > 1:
            self.priority -= 1  # повышаем приоритет
            print(f"[AGING] Повышен приоритет процесса {self.name} до {self.priority}")
            self.wait_time = 0  # сбрасываем ожидание

    def run(self, quantum):
        time_used = min(self.remaining_time, quantum)
        self.remaining_time -= time_used
        self.wait_time = 0
        print(f"[RUNNING] {self.name} (PID {self.pid}) → {time_used} ед. времени, осталось: {self.remaining_time}, PRIORITY: {self.priority}")
        return self.remaining_time <= 0

    def __repr__(self):
        return f"<Process {self.name} (PID {self.pid}) — осталось {self.remaining_time} ед. времени, PRIORITY: {self.priority}>"


class RoundRobinScheduler:
    def __init__(self, quantum):
        self.queue = deque()
        self.pid_counter = 1
        self.quantum = quantum

    def add_process(self, name, total_time, priority):
        process = Process(self.pid_counter, name, total_time, priority)
        self.queue.append(process)
        print(f"[ADDED] {process}")
        self.pid_counter += 1

    def run(self):
        finished_processes = []
        print("\n[STARTING SCHEDULER]\n")
        cycle = 1
        while self.queue:
            print(f"{'-' * 20} ЦИКЛ {cycle} {'-' * 20}")
            print("Текущая очередь:")
            for process in self.queue:
                process.maybe_promote(max_wait=3)
                print(process)

            self.queue = deque(sorted(self.queue, key=lambda p: p.priority)) #######
            process = self.queue.popleft()
            finished = process.run(self.quantum)
            if not finished:
                self.queue.append(process)
            else:
                print(f"[FINISHED] {process.name} (PID {process.pid}) завершён\n")
                finished_processes.append(process)
            cycle += 1
        print("\nЗавершённые процессы:")
        for proc in finished_processes:
            print(f" {proc.name} (PID {proc.pid})")
        print("[ALL TASKS COMPLETE]")


scheduler = RoundRobinScheduler(quantum=9)
scheduler.add_process("System Update", 4, priority=1)
scheduler.add_process("Music Player", 5, priority=3)
scheduler.add_process("Browser", 6, priority=2)
scheduler.add_process("Slow Background App", 7, priority=5)


scheduler.run()
