# svs_processor/processor.py

import os
import subprocess
from .metadata_extractor import MetadataExtractor
from .image_data_extractor import ImageDataExtractor
from .thumbnail_extractor import ThumbnailExtractor
from .png_converter import PNGConverter

class SVSProcessor:
    """
    A class to process SVS files. This class provides methods to extract metadata,
    image data, thumbnails, and convert the SVS file to PNG format.

    Attributes:
        svs_file_path (str): The path to the SVS file to process.
        output_dir (str): The directory where output files will be saved.
        thumbnail_size (tuple): The size of the thumbnail to extract.
        level (int): The level of resolution to extract from the SVS file.
    """
    def __init__(self, wsi_filename, output_dir, thumbnail_size=(200, 200), level=0, wsi_url=None):
        """Initializes the SVSProcessor with paths, thumbnail size, and image level."""
        self.images_dir = 'images'  # Folder where SVS files will be stored
        self.svs_file_path = os.path.join(self.images_dir, wsi_filename)
        self.output_dir = output_dir
        self.thumbnail_size = thumbnail_size
        self.level = level
        self.wsi_url = wsi_url

        # Ensure output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)  # Create the directory if it doesn't exist

        # Ensure PNG folder exists
        self.png_folder = os.path.join(self.output_dir, 'png')
        if not os.path.exists(self.png_folder):
            os.makedirs(self.png_folder)

        # Ensure the images folder exists and download the SVS file if necessary
        self.download_svs_file()

    def download_svs_file(self):
        """Download the SVS file if it's not already present in the images folder."""
        if not os.path.exists(self.images_dir):
            os.makedirs(self.images_dir)  # Ensure the 'images' folder exists

        if not os.path.isfile(self.svs_file_path):
            if self.wsi_url:
                print(f"Downloading SVS file from {self.wsi_url} into {self.images_dir}...")
                try:
                    # Use curl to download the file and save it in the images/ folder
                    subprocess.run(['curl', '-o', self.svs_file_path, self.wsi_url], check=True)
                    print(f"Downloaded {self.svs_file_path}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to download SVS file: {e}")
            else:
                print(f"No URL provided to download the SVS file.")

    def process(self):
        """Runs all steps of SVS file processing."""
        # Extract metadata
        metadata_extractor = MetadataExtractor(self.svs_file_path, self.output_dir)
        metadata_extractor.extract()

        # Extract image data
        image_data_extractor = ImageDataExtractor(self.svs_file_path, self.output_dir)
        image_data_extractor.extract()

        # Extract thumbnail
        thumbnail_extractor = ThumbnailExtractor(self.svs_file_path, self.output_dir, self.thumbnail_size)
        thumbnail_extractor.extract()

        # Convert to PNG for all levels dynamically
        png_converter = PNGConverter(self.svs_file_path, self.png_folder)
        png_converter.convert_all_levels()
