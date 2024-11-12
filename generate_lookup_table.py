import random
import csv

def generate_lookup_table(filename, num_mappings):
    # Port numbers range from 0 to 65535
    port_range = range(0, 65536)

    # Protocol options
    protocols = ['tcp', 'udp', 'icmp']

    # Tags to assign to mappings
    tags = ['sv_P1', 'sv_P2', 'sv_P3', 'sv_P4', 'sv_P5', 'email', 'web', 'database', 'backup', 'monitoring']

    # Initialize tag mappings
    tag_mappings = {tag: [] for tag in tags}

    # Generate mappings
    mappings = []
    for _ in range(num_mappings):
        dstport = str(random.randint(0, 65535))
        protocol = random.choice(protocols)

        # Randomize case for case insensitivity
        protocol = ''.join(random.choice([c.upper(), c.lower()]) for c in protocol)

        tag = random.choice(tags)

        # Store the mapping
        mappings.append((dstport, protocol, tag))
        tag_mappings[tag].append((dstport, protocol))

    # Write to CSV file
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write header
        csvwriter.writerow(['dstport', 'protocol', 'tag'])
        # Write mappings
        csvwriter.writerows(mappings)

    print(f"Lookup table generated with {num_mappings} mappings.")

if __name__ == "__main__":
    # Generate 10,000 mappings
    generate_lookup_table('lookup_table.csv', 10000)
