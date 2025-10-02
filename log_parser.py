import os
from utils import log_message

def parse_logs(log_file):
    log_message("📑 Parsing system logs...")

    if not os.path.exists(log_file):
        log_message(f"⚠️ Log file {log_file} not found")
        return

    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    errors = [line for line in lines if "ERROR" in line]
    warnings = [line for line in lines if "WARNING" in line]

    log_message(f"🔍 Found {len(errors)} errors and {len(warnings)} warnings")
    if errors:
        log_message("❌ Errors detected in logs")
    if warnings:
        log_message("⚠️ Warnings detected in logs")

    log_message("✅ Log parsing completed")
