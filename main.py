# import sys
# import io
# from collect_data import collect_data
# from log_parser import parse_logs
# from annotate import annotate_data
# from utils import log_message

# # ✅ Force stdout to UTF-8
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# def main():
#     log_message("🚀 Starting Zensar AI Data Pipeline Simulation")

#     # Step 1: Collect Data
#     collected_files = collect_data()

#     # Step 2: Parse System Logs
#     parse_logs("system.log")

#     # Step 3: Annotate Data
#     annotate_data(collected_files)

#     log_message("✅ Simulation Finished Successfully")

# if __name__ == "__main__":
#     main()

import sys
import io
from collect_data import collect_data
from log_parser import parse_logs
from annotate import annotate_image   # ✅ updated import
from utils import log_message

# ✅ Force stdout to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def main():
    log_message("🚀 Starting AI Data Pipeline Simulation")

    # Step 1: Collect Data
    collected_files = collect_data()

    # Step 2: Parse System Logs
    parse_logs("system.log")

    # Step 3: Annotate Image (instead of text files)
    annotate_image()

    log_message("✅ Simulation Finished Successfully")

if __name__ == "__main__":
    main()
