from utils import log_message

def collect_data():
    log_message("📡 Collecting Data...")

    data_files = ["data1.txt", "data2.txt", "data3.txt"]

    for i, file in enumerate(data_files, 1):
        with open(file, "w", encoding="utf-8") as f:
            f.write(f"Sample data {i}\n")

        log_message(f"✅ {file} created")

    log_message("📂 Data collection completed")
    return data_files
