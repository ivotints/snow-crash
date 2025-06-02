# Snow-crash

This project is an introductory cybersecurity challenge. Structured as a **Capture The Flag (CTF)** exercise, the project comprises multiple levels, each presenting a unique security vulnerability that participants must exploit to progress to the next level.

### 🔐 Project Overview

- **Format**: The project is delivered as a downloadable ISO file. We need to run it in the VM after the installation.
- **Levels**: There are 0-9 levels (10-14 levels for the bonus part), each corresponding to a user account (e.g., `level00`, `level01`, etc.).
- **Tools & Techniques**: Participants engage with various tools and methodologies, including:
    - **Reverse engineering**
    - **Assembly language analysis**
    - **Buffer overflow exploitation**
    - **Format string vulnerabilities**
    - **Privilege escalation**
    - **Network traffic analysis**
    - **Scripting with languages like Bash, Perl, and PHP**

### 🛠️ Getting Started

To embark on the Snow Crash project:

1. **Download the ISO**: Obtain the Snow Crash ISO file from the 42 school's internal resources.
2. **Set Up a Virtual Machine**: Use virtualization software like VirtualBox or VMware to create a new virtual machine.
3. **Configure Network Settings**: Adjust the VM's network settings in   **Setting →Expert→Network →Port Forwarding** change Host IP to use a Host-only Adapter, facilitating SSH access.
4. **Boot the VM**: Start the virtual machine and log in using ssh and use the credentials provided in the subject for `level00`.
5. **Begin the Challenge**: Analyze the system to find vulnerabilities, exploit them to retrieve the next level's password, and repeat the process for subsequent levels.