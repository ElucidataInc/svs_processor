import os
import logging
from svs_processor.processor import SVSProcessor

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    
    images_dir = 'images/'
    output_dir = 'output_directory/'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(images_dir):
        logging.error(f"The images directory '{images_dir}' does not exist.")
    else:
        logging.info(f"Processing files in {os.path.abspath(images_dir)}...")

    processed_files = 0  # Counter to track files that were actually processed
    skipped_files = 0    # Counter to track skipped files (where metadata already exists)

    for svs_filename in os.listdir(images_dir):
        if svs_filename.endswith(".svs"):
            svs_file_path = os.path.join(images_dir, svs_filename)

            logging.info(f"Looking for SVS file at: {os.path.abspath(svs_file_path)}")

            if not os.path.exists(svs_file_path):
                logging.error(f"File {os.path.abspath(svs_file_path)} not found.")
                continue

            file_output_dir = os.path.join(output_dir, os.path.splitext(svs_filename)[0])
            if not os.path.exists(file_output_dir):
                os.makedirs(file_output_dir)

            metadata_file_path = os.path.join(file_output_dir, f"{os.path.splitext(svs_filename)[0]}_metadata.csv")
            if os.path.exists(metadata_file_path):
                logging.info(f"Metadata already exists for {svs_filename}. Skipping...")
                skipped_files += 1  # Increment the skipped files counter
                continue

            logging.info(f"Processing {svs_filename}...")
            processor = SVSProcessor(svs_file_path, file_output_dir, thumbnail_size=(200, 200), level=0)
            processor.process()

            processed_files += 1
            logging.info(f"Finished processing {svs_filename}\n")

    # Final status reporting
    if processed_files == 0 and skipped_files == 0:
        logging.warning(f"No SVS files found in {images_dir}. Please check the folder and try again.")
    elif processed_files > 0:
        logging.info(f"Processed {processed_files} SVS files.")
    if skipped_files > 0:
        logging.info(f"Skipped {skipped_files} SVS files (metadata already exists).")
