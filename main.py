import os
from svs_processor.processor import SVSProcessor

if __name__ == "__main__":
    
    images_dir = 'images/'
    output_dir = 'output_directory/'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(images_dir):
        print(f"Error: The images directory '{images_dir}' does not exist.")
    else:
        print(f"Processing files in {os.path.abspath(images_dir)}...")

    processed_files = 0
    for svs_filename in os.listdir(images_dir):
        if svs_filename.endswith(".svs"):
            svs_file_path = os.path.join(images_dir, svs_filename)

            print(f"Looking for SVS file at: {os.path.abspath(svs_file_path)}")

            if not os.path.exists(svs_file_path):
                print(f"Error: File {os.path.abspath(svs_file_path)} not found.")
                continue

            file_output_dir = os.path.join(output_dir, os.path.splitext(svs_filename)[0])
            if not os.path.exists(file_output_dir):
                os.makedirs(file_output_dir)

            # Check if the metadata file already exists
            metadata_file_path = os.path.join(file_output_dir, f"{os.path.splitext(svs_filename)[0]}_metadata.csv")
            if os.path.exists(metadata_file_path):
                print(f"Metadata already exists for {svs_filename}. Skipping...")
                continue

            print(f"Processing {svs_filename}...")
            processor = SVSProcessor(svs_file_path, file_output_dir, thumbnail_size=(200, 200), level=0)
            processor.process()

            processed_files += 1
            print(f"Finished processing {svs_filename}\n")

    if processed_files == 0:
        print(f"No SVS files found in {images_dir}. Please check the folder and try again.")
    else:
        print(f"Processed {processed_files} SVS files.")
