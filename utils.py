from datetime import datetime

def log_message(message: str):
    """Log messages with timestamp (UTF-8 safe)."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
