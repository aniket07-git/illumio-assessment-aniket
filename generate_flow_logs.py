import random
import time

def generate_flow_logs(filename, target_size_mb):
    version = '2'
    account_id = '123456789012'
    interface_ids = [f'eni-{random.randint(0, 99999999):08x}' for _ in range(100)]
    ip_addresses = [f'{random.randint(1, 254)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}' for _ in range(1000)]
    protocols = ['1', '6', '17']  # ICMP, TCP, UDP
    actions = ['ACCEPT', 'REJECT']
    log_status = 'OK'

    avg_line_length = 150  # Approximate length per line
    num_lines = (target_size_mb * 1024 * 1024) // avg_line_length

    with open(filename, 'w') as f:
        for _ in range(int(num_lines)):
            interface_id = random.choice(interface_ids)
            srcaddr = random.choice(ip_addresses)
            dstaddr = random.choice(ip_addresses)
            srcport = str(random.randint(0, 65535))
            dstport = str(random.randint(0, 65535))
            protocol = random.choice(protocols)
            packets = str(random.randint(1, 1000))
            bytes_transferred = str(random.randint(100, 1000000))
            start_time = str(int(time.time()) - random.randint(0, 3600))
            end_time = str(int(start_time) + random.randint(0, 3600))
            action = random.choice(actions)

            fields = [
                version,
                account_id,
                interface_id,
                srcaddr,
                dstaddr,
                srcport,
                dstport,
                protocol,
                packets,
                bytes_transferred,
                start_time,
                end_time,
                action,
                log_status
            ]

            line = ' '.join(fields)
            f.write(line + '\n')

    print(f"Flow log file generated with approximately {target_size_mb} MB size.")

if __name__ == "__main__":
    # Generate around 10 MB of flow logs
    generate_flow_logs('flow_logs.txt', target_size_mb=10)
