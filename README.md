# Unique Media

Unique Media is a Python3-based project designed to convert various media file types (such as png and mp4) into more size-efficient formats like jpg and webm. Additionally, the project aims to identify and remove duplicate files within a specified set.

## Project Structure

The project comprises a collection of Python3 scripts that are executable via a bash script.

### Usage

1. Ensure Python3 is installed.

2. Execute the provided bash script to initiate the file conversion and duplicate check process.

```bash
./convert_media.sh
```

## Instructions

1. Place the media files (png, mp4) in the designated input folder ( _in/_ ).
2. Run the bash script to start the conversion and duplicate check.
3. Find the processed files in the output directory ( _out/_ ).

## Requirements

- Python 3.10
- Bash

## Note

The script will convert png files to jpg and mp4 files to webm, aiming to minimize file size. Duplicate files will be checked and removed to ensure a collection of unique media content.
