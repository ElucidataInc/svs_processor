import os
import csv
import openslide

class MetadataExtractor:
    """
    A class to extract metadata from an SVS file and save it to a CSV file.

    Attributes:
        svs_file_path (str): The path to the SVS file to process.
        output_dir (str): The directory where output files will be saved.
    """
    def __init__(self, svs_file_path, output_dir):
        self.svs_file_path = svs_file_path
        self.output_dir = output_dir

    def extract(self):
        """Extracts metadata from the SVS file and writes it to a CSV."""
        if not os.path.exists(self.svs_file_path):
            print(f"Error: File {self.svs_file_path} not found.")
            return

        try:
            slide = openslide.OpenSlide(self.svs_file_path)
            metadata = slide.properties
            output_csv = os.path.join(self.output_dir, f"{os.path.splitext(os.path.basename(self.svs_file_path))[0]}_metadata.csv")

            with open(output_csv, mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Key', 'Value'])
                for key, value in metadata.items():
                    writer.writerow([key, value])

            print(f"Metadata written to {output_csv}")
        except openslide.OpenSlideError as e:
            print(f"Error reading the SVS file: {e}")
        finally:
            slide.close()
