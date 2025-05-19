# Level 02 - Network Packet Analysis

## Step 1: Examine available files

We find a file named `level02.pcap` in the home directory.

A `.pcap` file is a packet capture file that contains captured network traffic data. These files are typically created and analyzed using packet sniffing tools.

## Step 2: Download the file to your host machine

We need to download this file from the VM to our host machine using `scp` (Secure Copy Protocol):

```sh
# Run this command on your host machine, not on the VM
scp -P 4242 level02@[VM_IP_ADDRESS]:/home/user/level02/level02.pcap /path/on/your/host
# Example: scp -P 4242 level02@localhost:/home/user/level02/level02.pcap ./
```

Enter the level02 password when prompted.

## Step 3: Analyze the packet capture file

If we open this file and search for `Password:`, we can find it, but it's encoded.

To decode it, we'll use the `tshark` program (Wireshark's command-line version):

```sh
tshark -r level02.pcap -T fields -e data | xxd -r -p | tr '\177' . | strings | grep assword

# or

python3 extract_password.py level02.pcap
```

## Step 4: Interpret the results

The command outputs:

```
Password: ft_wandr...NDRel.L0L
```

Remove the dots and characters before them to extract the password:

```
ft_waNDReL0L
```

The flag is:

```
kooda2puivaav1idi4f57q8iq
```
