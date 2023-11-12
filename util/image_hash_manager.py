from PIL import Image
import imagehash

class ImageHashManager():

    @staticmethod
    def hash(image_path: str) -> imagehash.ImageHash:
        image = Image.open(image_path)
        return imagehash.phash(image)
    
    @staticmethod
    def hash_list(images_path: list[str]) -> dict[imagehash.ImageHash, list[str]]:
        images_hash = {}

        for image_path in images_path:
            image_hash = ImageHashManager.hash(image_path)
            images_hash.setdefault(image_hash, []).append(image_path)

        return images_hash
    
    @staticmethod
    def get_equals_images(images: dict[imagehash.ImageHash, list[str]]) -> dict[imagehash.ImageHash, list[str]]:
        conflict_images = {key: value for key, value in images.items() if ImageHashManager.has_conflict(value)}
        return conflict_images
    
    @staticmethod
    def has_conflict(conflict_images: list[str]) -> bool:
        return len(conflict_images) > 1