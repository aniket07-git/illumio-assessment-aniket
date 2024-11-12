# Function to generate the output file
def generate_output(tag_counts, port_protocol_counts, output_filename):
    with open(output_filename, 'w') as file:
        # Write Tag Counts
        file.write("Tag Counts:\n\n")
        file.write("Tag,Count\n")
        # Write the tag counts
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")
        file.write("\n")

        # Write Port/Protocol Combination Counts
        file.write("Port/Protocol Combination Counts:\n\n")
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")