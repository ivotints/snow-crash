Execute this
```sh
find / -user flag00 2>/dev/null
```
* find / -  this will start search from the root directory.
* -user flag00 - only list files whouse owner is the user flag00
* 2>/dev/null - supress errors


Result is
```sh
/usr/sbin/john
/rofs/usr/sbin/john
```

```sh
cat /usr/sbin/john
```

will output us
```sh
v
```
This is some kind of a cipher
To decode it we use ceaser cipher and shift alphabet on 11 chars.
https://cryptii.com/pipes/caesar-cipher
Result is
```
nottoohardhere
```

now lets enter flag00 user
```
su flag00
Password: nottoohardhere
```
It will output
```
Don't forget to launch getflag !
```
We do it
```
getflag
```
Output is
```
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
```
We save flag in our repo and continue to the next level
```
su level01
Password: x24ti5gi3x0ol2eh4esiuxias
```
