import logging
from .metadata_extractor import MetadataExtractor
from .image_data_extractor import ImageDataExtractor
from .thumbnail_extractor import ThumbnailExtractor
from .png_converter import PNGConverter

class SVSProcessor:
    def __init__(self, svs_file_path, png_output_dir, metadata_output_dir, thumbnail_size=(200, 200), level=0, svs_id=1):
        self.svs_file_path = svs_file_path
        self.png_output_dir = png_output_dir
        self.metadata_output_dir = metadata_output_dir
        self.thumbnail_size = thumbnail_size
        self.level = level
        self.svs_id = svs_id

        # Now storing these extractors as attributes for external access after processing
        self.metadata_extractor = None
        self.image_data_extractor = None
        self.thumbnail_extractor = None

    def process_metadata_only(self):
        """Process only the metadata (without generating PNG images)."""
        logging.info(f"Starting metadata processing for {self.svs_file_path}")

        try:
            # Initialize and process metadata, image data, and thumbnails
            self.metadata_extractor = MetadataExtractor(self.svs_file_path, self.metadata_output_dir, self.svs_id)
            self.metadata_extractor.extract()

            self.image_data_extractor = ImageDataExtractor(self.svs_file_path, self.metadata_output_dir, self.svs_id)
            self.image_data_extractor.extract()

            self.thumbnail_extractor = ThumbnailExtractor(self.svs_file_path, self.metadata_output_dir, self.thumbnail_size, self.svs_id)
            self.thumbnail_extractor.extract()

            logging.info(f"Metadata processed successfully for {self.svs_file_path}")
        except Exception as e:
            logging.error(f"Error processing metadata for {self.svs_file_path}: {e}")

    def generate_pngs(self):
        """Generate PNG images for the SVS file."""
        logging.info(f"Starting PNG generation for {self.svs_file_path}")

        try:
            # Generate PNG files for the SVS file in file-specific subfolder
            png_converter = PNGConverter(self.svs_file_path, self.png_output_dir)
            png_converter.convert_all_levels()

            logging.info(f"Successfully generated PNGs for {self.svs_file_path}")
        except Exception as e:
            logging.error(f"Error generating PNGs for {self.svs_file_path}: {e}")
