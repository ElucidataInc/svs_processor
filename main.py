import os
from svs_processor.processor import SVSProcessor

if __name__ == "__main__":
    images_dir = '../images/'

    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    wsi_filename = 'TCGA-02-0010-01Z-00-DX4.07de2e55-a8fe-40ee-9e98-bcb78050b9f7.svs'

    wsi_url = 'https://data.kitware.com/api/v1/file/5899dd6d8d777f07219fcb23/download'

    output_dir = '../output_directory'

    processor = SVSProcessor(os.path.join(images_dir, wsi_filename), output_dir, thumbnail_size=(200, 200), level=0, wsi_url=wsi_url)
    processor.process()

