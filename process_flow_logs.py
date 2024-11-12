# This module processes flow logs and generates tag counts and port/protocol combination counts.
from map_protocol import get_protocol_name

# Function to process flow logs
def process_flow_logs(flow_log_filename, lookup_table):
    tag_counts = {}
    port_protocol_counts = {}
    untagged_count = 0

    with open(flow_log_filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            fields = line.split()
            if len(fields) < 14:
                continue  # Skip malformed lines

            # Extract required fields based on field positions
            dstport = fields[5].strip()
            protocol_number = fields[7].strip()

            # Convert protocol number to protocol name
            protocol_name = get_protocol_name(protocol_number)

            # Normalize for case-insensitive matching
            dstport = dstport
            protocol_name = protocol_name.lower()

            # Lookup the tag
            key = (dstport, protocol_name)
            tag = lookup_table.get(key, 'Untagged')

            # Update tag counts
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

            # Update port/protocol combination counts
            port_protocol_key = (dstport, protocol_name)
            port_protocol_counts[port_protocol_key] = port_protocol_counts.get(port_protocol_key, 0) + 1

    return tag_counts, port_protocol_counts

