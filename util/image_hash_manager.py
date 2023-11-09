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

            if image_hash in images_hash.keys():
                images_hash[image_hash].append(image_path)
            else:
                images_hash[image_hash] = [image_path]
        return images_hash
    
    @staticmethod
    def get_equals_images(images: dict[imagehash.ImageHash, str]) -> dict[imagehash.ImageHash, list[str]]:
        conflict_images = ImageHashManager.hash_list(images)
        images_hash = list(conflict_images.keys())
        images_paths = list(conflict_images.values())

        for image_hash, image_paths in zip(images_hash, images_paths):
            if not ImageHashManager.has_conflict(image_paths):
                conflict_images.pop(image_hash)
        return conflict_images

        # for image_hash, image_paths in conflict_images.items():
        #     if not ImageHashManager.has_conflict(image_paths):
        #         conflict_images.pop(image_hash)
        # return conflict_images
    
    @staticmethod
    def has_conflict(conflict_images: list[str]) -> bool:
        return len(conflict_images) > 1