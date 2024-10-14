# SVS Image Processor

## Overview

This project provides a modular Python solution for processing SVS (Scanned Virtual Slide) files. It includes functionality to download an SVS file, extract metadata, generate image data, create thumbnails, and convert the SVS file into PNG images at different downsampling levels. All outputs are saved in specified folders for easy access.

## Features

- Download SVS file from a specified URL.
- Extract and save metadata in CSV format.
- Extract image level data (dimensions and downsampling levels) in CSV format.
- Generate a thumbnail from the SVS file and save pixel data in CSV format.
- Dynamically generate PNG images for each downsampling level and save them in a `png/` folder.
- All file paths and outputs are managed through organized folder structures.

## Folder Structure

```plaintext
project_directory/
│
├── images/
│   └── <downloaded_svs_file>.svs  # The SVS file will be downloaded here.
│
├── output_directory/
│   ├── metadata.csv      # Metadata extracted from the SVS file
│   ├── image_data.csv    # Image level data (dimensions and downsampling factors)
│   ├── thumbnail.csv     # Thumbnail pixel data extracted from the SVS file
│   └── png/
│       ├── <svs_filename>_level_0.png  # PNG image at level 0
│       ├── <svs_filename>_level_1.png  # PNG image at level 1
│       └── ...                          # More PNGs for other levels
```

## Environment Setup

`git clone git@github.com:ElucidataInc/svs_processor.git`
`cd svs-processor`


## Create and activate virtual environment

`python -m venv venv`
`source venv/bin/activate`

## Install python dependencies

`pip install openslide-python`
`pip install Pillow`

### Note: You may need to install OpenSlide itself depending on your operating system. 
For Ubuntu:
`sudo apt-get install openslide-tools`

For macOS:
`brew install openslide`

### Run script

`python3 main.py`
