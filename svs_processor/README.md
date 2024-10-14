## Function Descriptions

### 1. **SVSProcessor** (`processor.py`)

The `SVSProcessor` class coordinates the entire SVS file processing pipeline, handling the file download, metadata extraction, image data extraction, thumbnail creation, and PNG conversion.

#### Methods:
- `__init__(self, wsi_filename, output_dir, thumbnail_size=(200, 200), level=0, wsi_url=None)`:
  Initializes the processor with the SVS file name, output directory, thumbnail size, image level, and optionally a URL for downloading the SVS file.
  
- `download_svs_file(self)`:
  Downloads the SVS file into the `images/` folder if it is not already present.

- `process(self)`:
  Runs the entire processing workflow, which includes extracting metadata, image data, thumbnails, and generating PNG files for all downsampling levels.

### 2. **MetadataExtractor** (`metadata_extractor.py`)

The `MetadataExtractor` class extracts metadata from the SVS file and saves it as a CSV.

#### Methods:
- `__init__(self, svs_file_path, output_dir)`:
  Initializes the metadata extractor with the SVS file path and output directory.

- `extract(self)`:
  Extracts metadata from the SVS file and writes it to a CSV file in the output directory.

### 3. **ImageDataExtractor** (`image_data_extractor.py`)

The `ImageDataExtractor` class extracts image data (dimensions and downsampling levels) from the SVS file and saves it as a CSV.

#### Methods:
- `__init__(self, svs_file_path, output_dir)`:
  Initializes the image data extractor with the SVS file path and output directory.

- `extract(self)`:
  Extracts image data, such as width, height, and downsampling factors, and saves it as a CSV in the output directory.

### 4. **ThumbnailExtractor** (`thumbnail_extractor.py`)

The `ThumbnailExtractor` class generates a thumbnail from the SVS file and saves the pixel data as a CSV.

#### Methods:
- `__init__(self, svs_file_path, output_dir, thumbnail_size)`:
  Initializes the thumbnail extractor with the SVS file path, output directory, and the desired thumbnail size.

- `extract(self)`:
  Generates the thumbnail from the SVS file and writes pixel data (in RGB format) to a CSV file in the output directory.

### 5. **PNGConverter** (`png_converter.py`)

The `PNGConverter` class generates PNG images for each downsampling level in the SVS file and saves them in a `png/` folder inside the output directory.

#### Methods:
- `__init__(self, svs_file_path, output_dir)`:
  Initializes the PNG converter with the SVS file path and output directory.

- `convert_all_levels(self)`:
  Converts the SVS file into PNG images for all available downsampling levels and saves them in a `png/` folder inside the output directory.
