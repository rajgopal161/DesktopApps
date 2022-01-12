import base64, zlib



#Code to compress a file
def compress(in_file, out_file):
    data = open(in_file, 'r').read()
    data_bytes = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(out_file, 'w')
    compressed_file.write(decoded_data)



#code to decompress a file
def decompress(in_file, out_file):
    compressed_data = open(in_file, 'r').read()
    decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
    dd_data = decompressed_data.decode('utf-8')
    dddata = open(out_file, 'w')
    dddata.write(dd_data)

