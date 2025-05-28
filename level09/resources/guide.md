# Level 09 - Custom Encoding Algorithm

## Step 1: Examine available files

Let's check what files we have in the home directory:

```sh
ls -l
```

Output:
```
-rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09 level09   26 Mar  5  2016 token
```

We have:
- An executable `level09` with SUID bit set
- A readable file named `token`

## Step 2: Test the executable

Running the program without arguments:

```sh
./level09
```

Output:
```
You need to provied only one arg.
```

Testing with some arguments:

```sh
./level09 111111
```

Output:
```
123456
```

```sh
./level09 AAAAAAAAAA
```

Output:
```
ABCDEFGHIJ
```

## Step 3: Understand the encoding algorithm

Based on the output pattern, we can see that the program is encoding strings by adding the position index to each character:
- Character at position 0 remains the same (0 is added)
- Character at position 1 gets 1 added to its ASCII value
- Character at position 2 gets 2 added
- And so on...

## Step 4: Analyze the binary for hints

Let's look for strings in the binary:

```sh
strings level09
```

Notable output:
```
You should not reverse this
// ...other strings...
You need to provied only one arg.
// ...other strings...
```

The message "You should not reverse this" hints that we need to reverse the encoding process.

## Step 5: Examine the token file

Let's see what's in the token file:

```sh
cat token
```

Output (showing some non-printable characters):
```
f4kmm6p|=�p�n��DB�Du{��
```

The token appears to be encoded using the same algorithm the executable uses.

## Step 6: Create a decoder

To decode the token, we need to reverse the encoding by subtracting the position index from each character.

First, let's download the token file to our local machine:

```sh
scp -P 4242 level09@[VM_IP]:/home/user/level09/token ./
chmod 777 token
```

Now let's write a Python script to decode it:

```python
#!/usr/bin/env python3

with open("token", 'rb') as f:
    cipher = f.read()

for i in range(len(cipher)):
    val = cipher[i] - i
    if 0 <= val < 255:
        print(chr(val), end='')
print()
```

## Step 7: Run the decoder and get the password

Execute the Python script:

```sh
python3 decoder.py
```

Output:
```
f3iji1ju5yuevaus41q1afiuq
```

## Step 8: Use the token to get the flag

Now we can switch to the flag09 user:

```sh
su flag09
Password: f3iji1ju5yuevaus41q1afiuq
```

And get the flag:

```sh
getflag
```

Output:
```
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
```

## Step 9: Proceed to next level

Now we can advance to level10:

```sh
su level10
Password: s5cAJpM8ev6XHw998pRWG728z
```
