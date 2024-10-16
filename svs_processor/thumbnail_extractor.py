import os
import csv
import openslide
import logging

class ThumbnailExtractor:
    def __init__(self, svs_file_path, metadata_output_dir, thumbnail_size, svs_id):
        self.svs_file_path = svs_file_path
        self.metadata_output_dir = metadata_output_dir
        self.thumbnail_size = thumbnail_size
        self.svs_id = svs_id
        self.thumbnail_csv = os.path.join(metadata_output_dir, "svs_thumbnail.csv")

    def extract(self):
        if not os.path.exists(self.svs_file_path):
            logging.error(f"File {self.svs_file_path} not found.")
            return

        if not os.path.exists(self.metadata_output_dir):
            os.makedirs(self.metadata_output_dir)

        try:
            slide = openslide.OpenSlide(self.svs_file_path)
            thumbnail = slide.get_thumbnail(self.thumbnail_size)
            thumbnail_pixels = list(thumbnail.getdata())

            with open(self.thumbnail_csv, mode='a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                if os.stat(self.thumbnail_csv).st_size == 0:
                    writer.writerow(['svs_id', 'file_name', 'x', 'y', 'red', 'green', 'blue'])

                for idx, pixel in enumerate(thumbnail_pixels):
                    x = idx % self.thumbnail_size[0]
                    y = idx // self.thumbnail_size[0]
                    writer.writerow([self.svs_id, os.path.basename(self.svs_file_path), x, y, pixel[0], pixel[1], pixel[2]])

            logging.info(f"Thumbnail pixel data appended to {self.thumbnail_csv}")
        except openslide.OpenSlideError as e:
            logging.error(f"Error reading the SVS file: {e}")
        finally:
            if slide:
                slide.close()
