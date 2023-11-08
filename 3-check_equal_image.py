from PIL import Image
import io

import imagehash

from util.state_manager import StateManager


DESTINATION_FOLDER = 'out/'
STEP = 2

def should_i_start(status_manager:StateManager):
    if not status_manager.should_i_start(STEP):
        return False

    if "png" not in status_manager.get_state() or "jpg" not in status_manager.get_state():
        return False

    return True

def phash(image_path):
    img = Image.open(image_path)
    return imagehash.phash(img)

def print_equal(image1, image2):
    print(f"This images are equal: {image1} and {image2}")

def main():
    status_manager = StateManager()
    status = status_manager.get_state()

    if not should_i_start(status_manager):
        exit(0)

    extensions = ("png", "jpg")
    found_images_equal = False

    for extension in extensions:

        unique_image = {}

        for image in status[extension]:
            hashed_image = phash(image)

            if hashed_image not in unique_image.keys():
                unique_image[hashed_image] = (image)
                continue

            print_equal(image, unique_image[hashed_image])
            found_images_equal = True
    
    if found_images_equal:
        exit(1)

if __name__ == "__main__":
    main()