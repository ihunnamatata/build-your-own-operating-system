# 🧠 Build Your Own Operating System (Simulated Kernel)

This project simulates a basic operating system kernel using Python. It introduces core OS concepts such as memory management, process scheduling, and system state — all within a round-robin executor.

---

## 📌 Features

- Launch named processes with memory requirements
- Track system memory and process states
- Prevent new processes from launching if memory is full
- Simulate round-robin scheduling

---

## 🧠 Why It Matters in Healthcare Simulation

In a live clinical AI setting, your system may need to:
- Run a simulation model (e.g. FEM brain perfusion)
- Activate a monitoring AI (e.g. oxygen alert)
- Log vitals and inference outcomes in real time

Your OS (or mini-OS) needs to:
- Manage memory between models
- Schedule jobs fairly
- Isolate failed states

---

## 🚀 How to Use

```bash
cd src/
python main.py
```

Output will show:
- Which processes were launched
- Which were blocked
- The schedule order
- Final system memory state

---

## 📁 Structure

- `src/main.py`: Simulated kernel logic
- `assets/`: Add architecture diagrams or screenshots
- `NOTES.md`: Clinical parallels, ideas, or system reflections

---

## 👩🏾‍⚕️ Author

**Ihunna Amugo**  
DDS Candidate | MHA | MS | REHS | PhD(c) Computational Engineering  
GitHub: [@ihunnamatata](https://github.com/ihunnamatata)
