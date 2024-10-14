import os
import csv
import openslide

class ThumbnailExtractor:
    """
    A class to extract a thumbnail from an SVS file and save its pixel data to a CSV file.

    Attributes:
        svs_file_path (str): The path to the SVS file to process.
        output_dir (str): The directory where output files will be saved.
        thumbnail_size (tuple): The size of the thumbnail to extract.
    """
    def __init__(self, svs_file_path, output_dir, thumbnail_size=(200, 200)):
        self.svs_file_path = svs_file_path
        self.output_dir = output_dir
        self.thumbnail_size = thumbnail_size

    def extract(self):
        """Extracts a thumbnail from the SVS file and writes pixel data to a CSV."""
        if not os.path.exists(self.svs_file_path):
            print(f"Error: File {self.svs_file_path} not found.")
            return

        try:
            slide = openslide.OpenSlide(self.svs_file_path)
            output_csv = os.path.join(self.output_dir, f"{os.path.splitext(os.path.basename(self.svs_file_path))[0]}_thumbnail.csv")
            thumbnail = slide.get_thumbnail(self.thumbnail_size)
            thumbnail_pixels = list(thumbnail.getdata())

            with open(output_csv, mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['X', 'Y', 'Red', 'Green', 'Blue'])
                for idx, pixel in enumerate(thumbnail_pixels):
                    x = idx % self.thumbnail_size[0]
                    y = idx // self.thumbnail_size[0]
                    writer.writerow([x, y, *pixel])

            print(f"Thumbnail pixel data written to {output_csv}")
        except openslide.OpenSlideError as e:
            print(f"Error reading the SVS file: {e}")
        finally:
            slide.close()
