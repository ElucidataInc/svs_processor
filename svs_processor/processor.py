import logging
from .metadata_extractor import MetadataExtractor
from .image_data_extractor import ImageDataExtractor
from .thumbnail_extractor import ThumbnailExtractor
from .png_converter import PNGConverter

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SVSProcessor:
    def __init__(self, svs_file_path, output_dir, thumbnail_size=(200, 200), level=0):
        self.svs_file_path = svs_file_path
        self.output_dir = output_dir
        self.thumbnail_size = thumbnail_size
        self.level = level

    def process(self):
        logging.info(f"Starting processing for {self.svs_file_path}")

        try:
            metadata_extractor = MetadataExtractor(self.svs_file_path, self.output_dir)
            metadata_extractor.extract()

            image_data_extractor = ImageDataExtractor(self.svs_file_path, self.output_dir)
            image_data_extractor.extract()

            thumbnail_extractor = ThumbnailExtractor(self.svs_file_path, self.output_dir, self.thumbnail_size)
            thumbnail_extractor.extract()

            png_converter = PNGConverter(self.svs_file_path, self.output_dir)
            png_converter.convert_all_levels()

            logging.info(f"Successfully processed {self.svs_file_path}")
        except Exception as e:
            logging.error(f"Error processing {self.svs_file_path}: {e}")
