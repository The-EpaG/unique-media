from PIL import Image
import io

from util.state_manager import StateManager


DESTINATION_FOLDER = 'out/'
STEP = 2
SCALE = 128, 128

def should_i_start(status_manager:StateManager):
    if not status_manager.should_i_start(STEP):
        return False

    if "png" not in status_manager.get_state() or "jpg" not in status_manager.get_state():
        return False

    return True

def scale_image(image_path):
    img = Image.open(image_path)
    img.thumbnail(SCALE, Image.Resampling.LANCZOS)
    
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return img_byte_arr

def not_equal(image1, image2):
    print(f"This images are equal: {image1} and {image2}")

def main():
    status_manager = StateManager()
    status = status_manager.get_state()

    if not should_i_start(status_manager):
        exit(0)

    extensions = ("png", "jpg")
    found_images_equal = False

    for extension in extensions:

        unique_image = {
            "path": [],
            "image": []
        }

        for image in status[extension]:
            scaled_image = scale_image(image)

            if scaled_image not in unique_image["image"]:
                unique_image["path"].append(image)
                unique_image["image"].append(scaled_image)
                continue

            not_equal(image, unique_image["path"].pop(unique_image["image"].index(scaled_image)))
            found_images_equal = True
    
    if found_images_equal:
        exit(1)

if __name__ == "__main__":
    main()