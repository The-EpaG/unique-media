import os
from moviepy.editor import VideoFileClip
import shutil
from util.const import DESTINATION_FOLDER, SOURCE_FOLDER

from util.state_manager import StateManager

STEP = 0

def should_i_start(status_manager:StateManager):
    return status_manager.should_i_start(STEP, should_exist=False)

def mkdir_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def mp4_to_webm(input_file, output_file):
    video = VideoFileClip(input_file)
    output_file = output_file.replace('.mp4', '.webm')
    video.write_videofile(output_file, codec="libvpx", audio_codec="libvorbis")
    return output_file

def main():
    status_manager = StateManager()
    status = status_manager.get_state()

    if not should_i_start(status_manager):
        exit(0)

    for root, dirs, files in os.walk(SOURCE_FOLDER):
        for file_name in files:
            # Get the file extension
            extension = file_name.split('.')[-1].lower()

            input_file = os.path.join(root, file_name)
            output_file = os.path.join(DESTINATION_FOLDER, file_name)

            # if the file is a video file convert it to webm
            if extension == 'mp4':
                output_file_webm = mp4_to_webm(input_file, output_file)
                extension = 'webm'  # Aggiorna l'estensione al nuovo formato
                status.setdefault('webm', []).append(output_file_webm)
            else:
                shutil.copy(input_file, output_file)
                status.setdefault(extension, []).append(output_file)

    # Save status
    status_manager.set_state(status)

if __name__ == '__main__':
    main()