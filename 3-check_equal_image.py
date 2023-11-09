from util.image_hash_manager import ImageHashManager
from util.state_manager import StateManager


DESTINATION_FOLDER = 'out/'
STEP = 2

def should_i_start(status_manager:StateManager):
    if not status_manager.should_i_start(STEP):
        return False

    if "png" not in status_manager.get_state() and "jpg" not in status_manager.get_state():
        return False

    return True

def print_equal(images: list[str]):
    print(f"This images are equal: {images}")

def main():
    status_manager = StateManager()
    status = status_manager.get_state()

    if not should_i_start(status_manager):
        exit(0)

    extensions = ("png", "jpg")
    found_images_equal = False

    for extension in extensions:
        if extension not in status:
            continue

        hashed_images = ImageHashManager.get_equals_images(status[extension])
        
        for conflict_image in hashed_images.values():
            found_images_equal = True
            print_equal(conflict_image)
    
    if found_images_equal:
        exit(1)

if __name__ == "__main__":
    main()