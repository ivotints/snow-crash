# Level 00 - Finding the Password

## Step 1: Find files owned by flag00

Execute this command to find all files owned by the user flag00:

```sh
find / -user flag00 2>/dev/null
```

**Command explanation:**
- `find /` - Search starting from the root directory
- `-user flag00` - Only list files owned by user flag00
- `2>/dev/null` - Suppress error messages

## Step 2: Examine the results

The search returns these files:
```sh
/usr/sbin/john
/rofs/usr/sbin/john
```

Let's check what's inside:
```sh
cat /usr/sbin/john
```

Output:
```sh
cdiiddwpgswtgt
```

This appears to be a cipher. To decode it, we use a Caesar cipher with a shift of 11 characters. You can use an online tool like [Cryptii](https://cryptii.com/pipes/caesar-cipher).

Decoded result:
```
nottoohardhere
```

## Step 3: Switch to flag00 user

Use the decoded password to switch to the flag00 user:
```sh
su flag00
Password: nottoohardhere
```

Output:
```
Don't forget to launch getflag!
```

## Step 4: Get the flag

Run the following command to retrieve the flag:
```sh
getflag
```

Output:
```
Check flag.Here is your token: x24ti5gi3x0ol2eh4esiuxias
```

Save the flag in your repository and proceed to the next level:
```sh
su level01
Password: x24ti5gi3x0ol2eh4esiuxias
```
