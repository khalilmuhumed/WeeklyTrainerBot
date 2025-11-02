# 🤖 Weekly Trainer Bot

A simple RPA (Robotic Process Automation) project built with **Robocorp / Sema4.ai** that automates the weekly sending of training schedules to a list of recipients.

This project was developed as part of Laurea University of Applied Sciences coursework.

---

## 🎯 Purpose

The bot automates a common manual task:
- Reads a list of recipients from an Excel file (`recipients.xlsx`)
- Checks that the weekly training schedule PDF exists
- Simulates sending the email (no real email is sent)
- Logs all actions and results to a file (`output/log.txt`)

The goal is to demonstrate **data handling**, **automation flow**, and **logging** using **Robot Framework + Robocorp Tasks**.

---

## 📂 Project Structure

WeeklyTrainerBot/
tasks.robot # Main robot logic
conda.yaml # Environment configuration
robot.yaml # Robot definition (entry point)
README.md # Project documentation
.gitignore # Ignored files
data/
recipients.xlsx # List of email recipients
training_schedule.pdf # Weekly training plan
output/ # Generated logs and reports
---

## ⚙️ Requirements

- **VS Code**
- **Robocorp Code / Sema4.ai extension**
- **Python 3.10+**
- Internet connection (for first-time environment setup only)

---

## 🚀 How to Run the Robot (Locally)

### Option 1: Inside VS Code
1. Open the folder `WeeklyTrainerBot` in VS Code  
2. Use Command Palette → `Sema4.ai: Switch to Local Development`  
3. Then run: `Sema4.ai: Run Task Package`

### Option 2: From the Terminal
Run this command:
```bash
~/.vscode/extensions/robocorp.robocorp-code-1.22.3-darwin-x64/bin/rcc run -r robot.yaml -t "Weekly Trainer Bot"
🧠 Key Features
No personal accounts or emails required

Simulates the process of sending weekly updates

Logs every step to output/log.txt

Checks for missing files and notifies if human action is needed

📊 Example Output
🚀 Starting WeeklyTrainerBot for week 44
📄 Recipients loaded: ['test1@example.com', 'test2@example.com', 'test3@example.com']
📎 PDF found for week 44: data/training_schedule.pdf
✉️ Simulating email sending...
✅ Completed successfully for week 44
🧩 Technologies Used
Robot Framework

RPA Framework (rpaframework)

Robocorp Tasks

Python 3.10

VS Code with Sema4.ai extension

👤 Author
Khalil Muhumed
Laurea University of Applied Sciences
Business Information Technology (BIT) — 2025
