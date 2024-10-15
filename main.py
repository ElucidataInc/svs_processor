from svs_processor.processor import SVSProcessor

if __name__ == "__main__":
    # URL to download the SVS file if it's not present
    wsi_url = 'https://data.kitware.com/api/v1/file/5899dd6d8d777f07219fcb23/download'

    # Test SVS file
    wsi_filename = 'TCGA-02-0010-01Z-00-DX4.07de2e55-a8fe-40ee-9e98-bcb78050b9f7.svs'
    output_dir = 'output_directory'

    processor = SVSProcessor(wsi_filename, output_dir, thumbnail_size=(200, 200), level=0, wsi_url=wsi_url)
    processor.process()
