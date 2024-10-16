import os
import csv
import openslide
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MetadataExtractor:
    def __init__(self, svs_file_path, output_dir):
        self.svs_file_path = svs_file_path
        self.output_dir = output_dir

    def extract(self):
        if not os.path.exists(self.svs_file_path):
            logging.error(f"File {self.svs_file_path} not found.")
            return

        slide = None
        try:
            slide = openslide.OpenSlide(self.svs_file_path)
            metadata = slide.properties
            output_csv = os.path.join(self.output_dir, f"{os.path.splitext(os.path.basename(self.svs_file_path))[0]}_metadata.csv")

            with open(output_csv, mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Key', 'Value'])
                for key, value in metadata.items():
                    writer.writerow([key, value])

            logging.info(f"Metadata written to {output_csv}")
        except openslide.OpenSlideError as e:
            logging.error(f"Error reading the SVS file: {e}")
        finally:
            if slide:
                slide.close()
