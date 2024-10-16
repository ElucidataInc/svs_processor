import os
import logging
from svs_processor.processor import SVSProcessor

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    images_dir = 'images/'
    png_output_dir = 'output_directory/png/'
    metadata_output_dir = 'output_directory/metadata/'

    if not os.path.exists(png_output_dir):
        os.makedirs(png_output_dir)

    all_metadata_keys = set()  # Initialize the set to collect all unique metadata keys
    processors = []  # Store processor objects for the second pass (for PNG generation)
    processed_files = 0
    svs_id = 1  # Unique identifier for each SVS file

    # -------- First Pass: Process Metadata --------
    for svs_filename in os.listdir(images_dir):
        if svs_filename.endswith(".svs"):
            svs_file_path = os.path.join(images_dir, svs_filename)
            file_png_output_dir = os.path.join(png_output_dir, os.path.splitext(svs_filename)[0])

            if not os.path.exists(file_png_output_dir):
                os.makedirs(file_png_output_dir)

            logging.info(f"Processing metadata for {svs_filename}...")
            processor = SVSProcessor(svs_file_path, file_png_output_dir, metadata_output_dir, thumbnail_size=(200, 200), level=0, svs_id=svs_id)
            
            # Process the SVS file to collect metadata (keys)
            processor.process_metadata_only()

            # Collect all unique metadata keys
            all_metadata_keys.update(processor.metadata_extractor.metadata_dict[svs_id].keys())

            # Save processor for second pass (PNG generation)
            processors.append(processor)

            processed_files += 1
            svs_id += 1
            logging.info(f"Finished processing metadata for {svs_filename}\n")

    if processed_files == 0:
        logging.warning(f"No SVS files found in {images_dir}. Please check the folder and try again.")
    else:
        logging.info(f"Processed metadata for {processed_files} SVS files.")

    # -------- Combine Metadata and Write to CSV --------
    all_metadata_keys = list(all_metadata_keys)  # Convert set to list before concatenating
    logging.info(f"Writing combined metadata to CSV files with {len(all_metadata_keys)} unique metadata keys...")

    for processor in processors:
        processor.metadata_extractor.write_metadata(all_metadata_keys)

    logging.info("Combined metadata written to CSV.")

    # -------- Second Pass: Generate PNG Images --------
    logging.info("Starting PNG generation for all files...")

    for processor in processors:
        logging.info(f"Generating PNG images for {processor.svs_file_path}...")
        processor.generate_pngs()

    logging.info("Finished generating PNG images for all files.")
