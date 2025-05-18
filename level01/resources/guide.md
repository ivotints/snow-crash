# Level 01 - Password Cracking

## Step 1: Examine the password file

The `/etc/passwd` file stores the system's user account information. Each line contains fields such as username, encrypted password placeholder, UID, GID, user description, home directory, and default shell.

Let's examine this file:
```sh
cat /etc/passwd
```

## Step 2: Locate password information

Normally, an 'x' in the password field indicates that the real encrypted password is stored in `/etc/shadow`.

However, we notice that the user `flag01` has an actual hashed password instead of an 'x':
```
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
```

## Step 3: Crack the hashed password

We will use brute force and a dictionary file `rockyou.txt` to crack the hashed password.

Download the dictionary file:
```sh
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

Run the cracking script:
```sh
python3 crack.py
```

The result is:
```
Found: abcdefg
```

## Step 4: Switch to the `flag01` user

Use the cracked password to switch to the `flag01` user:
```sh
su flag01
Password: abcdefg
```

You will see the following output:
```
Don't forget to launch getflag !
```

## Step 5: Retrieve the flag

Run the `getflag` command:
```sh
getflag
```

The output will be:
```
Check flag.Here is your token : f2av5il02puano7naaf6adaaf
```

Save the flag and proceed to the next level:
```sh
su level02
Password: f2av5il02puano7naaf6adaaf
```
