import os
import openslide
from PIL import Image
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PNGConverter:
    def __init__(self, svs_file_path, output_dir):
        self.svs_file_path = svs_file_path
        self.output_dir = output_dir

    def convert_all_levels(self):
        if not os.path.exists(self.svs_file_path):
            logging.error(f"File {self.svs_file_path} not found.")
            return

        try:
            slide = openslide.OpenSlide(self.svs_file_path)
            num_levels = slide.level_count

            for level in range(num_levels):
                width, height = slide.level_dimensions[level]
                svs_image = slide.read_region((0, 0), level, (width, height)).convert("RGB")
                output_png = os.path.join(self.output_dir, f"{os.path.splitext(os.path.basename(self.svs_file_path))[0]}_level_{level}.png")

                svs_image.save(output_png, "PNG")
                logging.info(f"Image at level {level} written to {output_png}")
        except openslide.OpenSlideError as e:
            logging.error(f"Error reading the SVS file: {e}")
        finally:
            if slide:
                slide.close()
