# from utils import log_message

# def annotate_data(files):
#     log_message("📝 Starting annotation...")

#     for file in files:
#         annotated_file = f"annotated_{file}"
#         with open(file, "r", encoding="utf-8") as f:
#             content = f.read()

#         with open(annotated_file, "w", encoding="utf-8") as f:
#             f.write(content.strip() + " | annotated ✅\n")

#         log_message(f"✏️ Annotated {file} -> {annotated_file}")

#     log_message("📌 Annotation process completed")

from PIL import Image, ImageDraw
from utils import log_message

def annotate_image():
    log_message("📝 Starting image annotation...")

    # Create a blank image
    img = Image.new("RGB", (400, 300), color="white")
    draw = ImageDraw.Draw(img)

    # 🚗 Simulated bounding box for Car
    draw.rectangle([50, 50, 150, 150], outline="red", width=3)
    draw.text((50, 40), "Car", fill="red")

    # 🏍️ Simulated bounding box for Bike
    draw.rectangle([200, 100, 280, 200], outline="blue", width=3)
    draw.text((200, 90), "Bike", fill="blue")

    # Save and show
    img.save("annotated_output.png")
    img.show()

    log_message("✅ Image annotated and saved as 'annotated_output.png'")
