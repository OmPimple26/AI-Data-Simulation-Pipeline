# AI-Data-Simulation-Pipeline

🚀 AI Data Simulation Pipeline: Simulates a mini AI workflow with data collection📂, log parsing📝, and image annotation🖼️. Generates sample files, detects errors/warnings⚠️❌, and creates annotated images✅. Perfect demo for AI pipelines!

--- 

## 🌟 Features

- **Data Collection📂:** Generates sample text files (`data1.txt`, `data2.txt`, `data3.txt`) simulating raw input.  
- **Log Parsing📝:** Reads `system.log` to detect **errors❌** and **warnings⚠️**.  
- **Image Annotation🖼️:** Creates `annotated_output.png` with bounding boxes for objects like cars 🚗 and bikes 🏍️.  
- **Timestamped Logging⏰:** All console messages include timestamps and are UTF-8 safe.

---

## 🛠️ Tech Stack

- Python 3.x  
- Pillow (PIL) for image annotation  
- Standard Python libraries: `os`, `io`, `datetime`, `sys`

---

## 🗂️ Project Structure

main.py # Entry point of the pipeline
collect_data.py # Simulates data collection
log_parser.py # Parses system logs for errors/warnings
annotate.py # Simulates annotation (image)
utils.py # Helper functions for logging
system.log # Sample system log
.gitignore # Ignore unnecessary files
LICENSE # License
README.md # Project description

---

## ⚡ How to Run

1. Install dependencies:
```
pip install pillow
```

2. Run the pipeline:
```
python main.py
```

3. Check the console logs, text files, and annotated_output.png.

---

## 🎯 Outcome

Sample text files representing collected data

Annotated image showing bounding boxes

Console logs with timestamps, errors❌, and warnings⚠️

---

## 🎓 Purpose

A beginner-friendly demo of an AI data pipeline:

Collect raw data

Monitor system logs

Annotate datasets for AI training
Ideal for learning or showcasing in interviews 🚀.