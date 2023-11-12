from util.image_hash_manager import ImageHashManager
from util.state_manager import StateManager


DESTINATION_FOLDER = 'out/'
STEP = 2
SUPPORTED_EXTENSIONS = ("png", "jpg")

def should_start(status_manager: StateManager) -> bool:
    return status_manager.should_start(STEP) and any(ext in status_manager.get_state() for ext in SUPPORTED_EXTENSIONS)

def print_equal(images: list[str]) -> None:
    print(f"This images are equal: {images}")

def main() -> None:
    status_manager = StateManager()
    status = status_manager.get_state()

    if not should_start(status_manager):
        exit(0)

    found_images_equal = False

    for extension in SUPPORTED_EXTENSIONS:
        if extension not in status:
            continue

        hashed_images = ImageHashManager.hash_list(status[extension])
        hashed_images = ImageHashManager.get_equals_images(hashed_images)
        
        for _, conflict_image in hashed_images.items():
            found_images_equal = True
            print_equal(conflict_image)
    
    if found_images_equal:
        exit(1)

if __name__ == "__main__":
    main()