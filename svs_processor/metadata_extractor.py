import os
import csv
import openslide
import logging
from collections import defaultdict

class MetadataExtractor:
    def __init__(self, svs_file_path, metadata_output_dir, svs_id):
        self.svs_file_path = svs_file_path
        self.metadata_output_dir = metadata_output_dir
        self.svs_id = svs_id
        self.metadata_csv = os.path.join(metadata_output_dir, "svs_metadata.csv")
        self.metadata_dict = defaultdict(dict)  # Store metadata for each file as a dictionary

    def extract(self):
        if not os.path.exists(self.svs_file_path):
            logging.error(f"File {self.svs_file_path} not found.")
            return

        if not os.path.exists(self.metadata_output_dir):
            os.makedirs(self.metadata_output_dir)

        slide = None
        try:
            slide = openslide.OpenSlide(self.svs_file_path)
            metadata = slide.properties

            # Store metadata in dictionary with keys as column names
            for key, value in metadata.items():
                self.metadata_dict[self.svs_id][key] = value

            # Add file name
            self.metadata_dict[self.svs_id]['file_name'] = os.path.basename(self.svs_file_path)

            logging.info(f"Metadata collected for {self.svs_file_path}")
        except openslide.OpenSlideError as e:
            logging.error(f"Error reading the SVS file: {e}")
        finally:
            if slide:
                slide.close()

    def write_metadata(self, all_keys):
        """ Write metadata to CSV in a wide format (one row per file with metadata keys as columns) """
        with open(self.metadata_csv, mode='a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['svs_id', 'file_name'] + all_keys)

            # Write header only if file is empty
            if os.stat(self.metadata_csv).st_size == 0:
                writer.writeheader()

            # Write the row for this SVS file
            for svs_id, metadata in self.metadata_dict.items():
                row = {'svs_id': svs_id}
                row.update(metadata)
                writer.writerow(row)
