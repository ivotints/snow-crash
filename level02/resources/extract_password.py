import sys
import re
from scapy.all import rdpcap, TCP, Raw


def reassemble_payload(packets):
    payload = bytearray()
    for packet in packets:
        if packet.haslayer(TCP) and packet.haslayer(Raw):
            payload.extend(packet[Raw].load)
    return payload


def mark_del_as_dot(data):
    return bytes(b if b != 127 else b'.'[0] for b in data)


def extract_password_line(data_bytes):
    match = re.search(b'Password:[^\r\n]*', data_bytes)
    return match.group().decode('ascii') if match else None


def main():
    if len(sys.argv) != 2:
        file = "level02.pcap"
    else:
        file = sys.argv[1]

    try:
        packets = rdpcap(file)
    except FileNotFoundError:
        sys.exit("Usage: python3 extract_password.py <pcap_file>")

    raw_payload = reassemble_payload(packets)
    visible_payload = mark_del_as_dot(raw_payload)

    password_line = extract_password_line(visible_payload)
    if password_line:
        print(password_line)
    else:
        print("Password line not found.")


if __name__ == '__main__':
    main()
