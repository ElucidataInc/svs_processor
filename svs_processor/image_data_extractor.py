import os
import csv
import openslide
import logging

class ImageDataExtractor:
    def __init__(self, svs_file_path, metadata_output_dir, svs_id):
        self.svs_file_path = svs_file_path
        self.metadata_output_dir = metadata_output_dir
        self.svs_id = svs_id
        self.image_data_csv = os.path.join(metadata_output_dir, "svs_image_data.csv")

    def extract(self):
        if not os.path.exists(self.svs_file_path):
            logging.error(f"File {self.svs_file_path} not found.")
            return

        if not os.path.exists(self.metadata_output_dir):
            os.makedirs(self.metadata_output_dir)

        try:
            slide = openslide.OpenSlide(self.svs_file_path)
            image_data = []
            num_levels = slide.level_count

            with open(self.image_data_csv, mode='a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                if os.stat(self.image_data_csv).st_size == 0:
                    writer.writerow(['svs_id', 'file_name', 'level', 'width', 'height', 'downsample'])

                for level in range(num_levels):
                    width, height = slide.level_dimensions[level]
                    downsample = slide.level_downsamples[level]
                    writer.writerow([self.svs_id, os.path.basename(self.svs_file_path), level, width, height, downsample])

            logging.info(f"Image data appended to {self.image_data_csv}")
        except openslide.OpenSlideError as e:
            logging.error(f"Error reading the SVS file: {e}")
        finally:
            if slide:
                slide.close()
