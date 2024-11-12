# Main script to run the entire process
def main():
    # File names 
    lookup_table_filename = 'lookup_table.csv' # This file should be generated using generate_lookup_table.py
    # flow_logs.txt is a sample file that contains flow logs around 10 MB in size
    flow_log_filename = 'flow_logs.txt' # This file should be generated using generate_flow_logs.py
    output_filename = 'output.txt' # Output file to write the results

    # Load the lookup table
    lookup_table = open_load_lookup_table(lookup_table_filename)

    # Process the flow logs
    tag_counts, port_protocol_counts = process_flow_logs(flow_log_filename, lookup_table)

    # Generate the output file
    generate_output(tag_counts, port_protocol_counts, output_filename)

    print(f"Processing complete. Output written to {output_filename}")

# Entry point of the script
if __name__ == "__main__":
    # Import the required functions
    from lookup_table import open_load_lookup_table
    from map_protocol import get_protocol_name
    from process_flow_logs import process_flow_logs
    from generate_outputs import generate_output

    main()
