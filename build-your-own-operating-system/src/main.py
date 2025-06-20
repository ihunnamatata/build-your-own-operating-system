"""
Build Your Own Operating System – Simulated Kernel (Python)
Author: Ihunna Amugo | Build-Your-Own-X Series

🧠 Goal:
Simulate a minimalist OS kernel loop that:
- Launches and tracks fake processes
- Simulates memory usage per app
- Schedules jobs in a round-robin style

🩺 Real-World Parallel:
A surgical digital twin system may run:
- A perfusion simulator (Python/FEM)
- An AI classifier (PyTorch)
- A logger (file output)

This capstone teaches how those components might be scheduled, memory-isolated, and executed in real-time.

"""

import time
import random

class Process:
    def __init__(self, pid, name, memory_required):
        self.pid = pid
        self.name = name
        self.memory = memory_required
        self.state = "READY"

    def run(self):
        print(f"[RUNNING] {self.name} (PID {self.pid}) | Memory: {self.memory}MB")
        time.sleep(0.5)  # simulate work
        self.state = "TERMINATED"

class KernelSimulator:
    def __init__(self, total_memory=512):
        self.process_table = []
        self.next_pid = 1
        self.total_memory = total_memory
        self.used_memory = 0

    def launch(self, name, memory):
        if self.used_memory + memory > self.total_memory:
            print(f"❌ Not enough memory to launch {name} ({memory}MB)")
            return
        proc = Process(self.next_pid, name, memory)
        self.process_table.append(proc)
        self.used_memory += memory
        self.next_pid += 1
        print(f"✅ Launched {name} (PID {proc.pid}) | Memory: {memory}MB")

    def schedule(self):
        print("\n[📋 Scheduler] Round-robin execution beginning:")
        for proc in self.process_table:
            if proc.state == "READY":
                proc.run()
                self.used_memory -= proc.memory

    def status(self):
        print("\n[📊 System Status]")
        for proc in self.process_table:
            print(f"PID {proc.pid} | {proc.name} | State: {proc.state}")
        print(f"Memory: {self.used_memory}/{self.total_memory}MB used")

if __name__ == "__main__":
    os = KernelSimulator()

    # Simulate launching apps (e.g., ML, FEM, logger)
    os.launch("AI_Triage_Model", 120)
    os.launch("PerfusionSimulator", 200)
    os.launch("Logger", 64)
    os.launch("BackupProcess", 180)  # should exceed memory

    os.status()
    os.schedule()
    os.status()
