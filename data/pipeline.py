import sdmx

PATH = 'data/PLASTIC_USE_9.xml'
data = sdmx.read_sdmx(filename_or_obj = PATH, format = 'XML')
data.to_pandas()