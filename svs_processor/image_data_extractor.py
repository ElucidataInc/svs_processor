import os
import csv
import openslide
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ImageDataExtractor:
    def __init__(self, svs_file_path, output_dir):
        self.svs_file_path = svs_file_path
        self.output_dir = output_dir

    def extract(self):
        if not os.path.exists(self.svs_file_path):
            logging.error(f"File {self.svs_file_path} not found.")
            return

        try:
            slide = openslide.OpenSlide(self.svs_file_path)
            output_csv = os.path.join(self.output_dir, f"{os.path.splitext(os.path.basename(self.svs_file_path))[0]}_image_data.csv")
            image_data = []
            num_levels = slide.level_count

            for level in range(num_levels):
                width, height = slide.level_dimensions[level]
                downsample = slide.level_downsamples[level]
                image_data.append([level, width, height, downsample])

            with open(output_csv, mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Level', 'Width', 'Height', 'Downsample'])
                writer.writerows(image_data)

            logging.info(f"Image data written to {output_csv}")
        except openslide.OpenSlideError as e:
            logging.error(f"Error reading the SVS file: {e}")
        finally:
            if slide:
                slide.close()
