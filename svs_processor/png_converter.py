import os
import openslide
from PIL import Image

class PNGConverter:
    """
    A class to convert an SVS file to PNG format at all downsampling levels.

    Attributes:
        svs_file_path (str): The path to the SVS file to process.
        output_dir (str): The directory where output PNG files will be saved.
    """
    def __init__(self, svs_file_path, output_dir):
        self.svs_file_path = svs_file_path
        self.output_dir = output_dir

    def convert_all_levels(self):
        """Convert the SVS file to PNG images for all downsampling levels."""
        if not os.path.exists(self.svs_file_path):
            print(f"Error: File {self.svs_file_path} not found.")
            return

        try:
            slide = openslide.OpenSlide(self.svs_file_path)
            num_levels = slide.level_count  # Get the number of downsampling levels

            # Convert image at each level and save as PNG
            for level in range(num_levels):
                width, height = slide.level_dimensions[level]
                svs_image = slide.read_region((0, 0), level, (width, height)).convert("RGB")

                # Define the output PNG file name for each level
                output_png = os.path.join(self.output_dir, f"{os.path.splitext(os.path.basename(self.svs_file_path))[0]}_level_{level}.png")

                # Save the PNG image
                svs_image.save(output_png, "PNG")
                print(f"Image at level {level} written to {output_png}")

        except openslide.OpenSlideError as e:
            print(f"Error reading the SVS file: {e}")
        finally:
            slide.close()
