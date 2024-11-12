# This file contains the code to load the lookup table from a CSV file.
def open_load_lookup_table(filename):
    lookup = {}
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            dstport, protocol, tag = line.split(',')
            # Normalize the data for case-insensitive matching
            dstport = dstport.strip()
            protocol = protocol.strip().lower()
            tag = tag.strip()
            key = (dstport, protocol)
            lookup[key] = tag
    return lookup