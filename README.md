# Snow Crash

## About the Project

Snow Crash is a cybersecurity project designed to introduce students to basic techniques in computer security, including:

- Binary exploitation
- Web vulnerabilities
- Permission exploits
- Environment variable manipulation
- Reverse engineering
- And more...

The project consists of multiple levels (00-09+), each presenting a unique security challenge to solve in a Linux environment.

## Project Structure

```
/snow-crash
├── level00/
│   ├── resources/
│   |   └── guide.md
│   └── flag
├── level01/
│   ├── resources/
│   |   └── guide.md
│   └── flag
├── level02/
│   ├── resources/
│   |   └── guide.md
│   └── flag
...
└── README.md
```

Each level directory contains a `resources` folder with a detailed guide on how to solve the challenge.

## How to Use This Repository

1. Connect to the Snow Crash virtual machine:
   ```
   ssh level00@[VM_IP_ADDRESS] -p 4242
   ```
   Initial password: `level00`

2. Follow the guide for each level in the corresponding directory
3. Each level's solution reveals a token/password for the next level
4. After obtaining a token, use it to access the next level:
   ```
   su levelXX
   Password: [token from previous level]
   ```

5. Use the `getflag` command once logged in as the flag user to reveal the level's token

## Skills Developed

Working through the Snow Crash project will help you develop skills in:

- Command line and shell scripting
- Understanding SUID/SGID permissions
- Network traffic analysis
- Basic cryptography
- PHP security
- Python scripting
- Process manipulation
- Code review and vulnerability spotting

## Environment Setup

The Snow Crash challenges are designed to be solved within a provided VM:

- Operating System: Linux (Ubuntu-based)
- Required Tools:
  - SSH client
  - Basic Linux command line knowledge
  - Tools like `ltrace`, `strings`, `wireshark`/`tshark` (for specific levels)
  - Python for scripting solutions

## Challenge Levels Overview

- **Level 00**: Finding hidden files and basic cipher decoding
- **Level 01**: Password cracking and understanding Linux password storage
- **Level 02**: Network packet analysis and examining .pcap files
- **Level 03**: Path manipulation and exploiting SUID binaries
- **Level 04**: Command injection via CGI scripts
- **Level 05**: Exploiting cron jobs and file permissions
- **Level 06**: PHP regex vulnerabilities and code execution
- **Level 07**: Environment variable exploitation
- **Level 08**: Bypassing file access restrictions
- **Level 09**: Reverse engineering a custom encoding algorithm

## Notes

- Always make sure to document your solutions
- Some levels require transferring files between the VM and your host machine using `scp`
- Practice good security habits, even in a training environment

## Acknowledgments

This project is part of the 42 School curriculum and is designed to teach practical cybersecurity concepts through hands-on challenges.
