from PIL import Image
import os
from util.const import DESTINATION_FOLDER

from util.state_manager import StateManager

STEP = 1

def should_i_start(status_manager:StateManager):
    if not status_manager.should_i_start(STEP):
        return False

    if "png" not in status_manager.get_state():
        return False

    return True

def get_file_name(file_path):
    return os.path.basename(file_path)

def get_output_file_name(file_path):
    return os.path.join(DESTINATION_FOLDER, file_path)

def convert_png_to_jpg(png_path):
    img = Image.open(png_path)

    if img.mode == "RGBA":
        return None

    jpg_path = get_file_name(png_path)
    jpg_path = jpg_path.replace(".png", ".jpg")
    jpg_path = get_output_file_name(jpg_path)
    img.save(jpg_path, "JPEG")
    
    os.remove(png_path)
    return jpg_path

def main():
    status_manager = StateManager()
    status = status_manager.get_state()

    if not should_i_start(status_manager):
        exit(0)

    converted_file = []

    # Convert PNG to JPG
    for png_path in status["png"]:
        jpg_path = convert_png_to_jpg(png_path)

        if jpg_path is None:
            continue

        converted_file.append((png_path, jpg_path))

    # Update status
    for png_path, jpg_path in converted_file:
        if "jpg" not in status:
            status["jpg"] = []

        status["jpg"].append(jpg_path)

        status["png"].remove(png_path)
    
    # If png is empty, remove it
    if len(status["png"]) == 0:
        status.remove("png")

    # Save status
    status_manager.set_state(status)

if __name__ == "__main__":
    main()