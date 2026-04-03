Computer Troubleshooting CLI

Description

This project is a command-line tool that helps diagnose common computer problems and suggests possible solutions.

The tool can detect issues such as:
- Network problems
- System freezing
- Overheating
- Blue screen errors
- Slow operating system

It is built using Python, Typer, and uv.



Installation

Clone the repository:

git https://github.com/CrisAxe/backend-i.git

Install dependencies:

uv sync


Run the CLI:

python cli.py menu


Example 

=== Computer Troubleshooting Menu ===
1. Network
2. Freeze
3. Heating
4. Bluescreen
5. OS Slow
Select a problem by number: 3

Problem: heating
Solution: Clean your computer fan and ensure proper ventilation.


or

python cli.py wizard


Exemple

🧙 System Troubleshooting Wizard

Does your computer freeze frequently? [y/N]: y 
Do you see a blue screen error? [y/N]: ñ
Error: invalid input
Do you see a blue screen error? [y/N]: n
╭──────────────────────────────────────────────────── 📋 Detected Problems ────────────────────────────────────────────────────╮
│                                                                                                                              │
│                                                                                                                              │
│ ---                                                                                                                          │
│ Network: False                                                                                                               │
│ Freeze: True                                                                                                                 │
│ Overheating: False                                                                                                           │
│ Bluescreen: False                                                                                                            │
│ Os Slow: False                                                                                                               │
│                                                                                                                              │
│ ---                                                                                                                          │
│                                                                                                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🔧 Recommended Solutions:

Problem: freeze
Analyzing freeze... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   0% -:--:--• Close heavy applications
Analyzing freeze... ━━━━━━━━━━━━━╺━━━━━━━━━━━━━━━━━━━━━━━━━━  33% -:--:--• Check RAM usage in Task Manager
Analyzing freeze... ━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━━━━━━━━  67% 0:00:01• Restart the computer
Analyzing freeze... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:01

📊 System Metrics:
         System Status
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Metric              ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ CPU Usage           │ 9.8%  │
│ RAM Usage           │ 51.3% │
│ Disk Usage          │ 57.6% │
│ Internet Connection │ OK    │
└─────────────────────┴───────┘