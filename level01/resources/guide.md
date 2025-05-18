* `/etc/passwd` stores the system’s user account information-each line holds a user’s entry with fields like username, encrypted password placeholder, UID, GID, user description, home directory, and default shell.

* let's look at /etc/passwd
```sh
cat /etc/passwd
```

x in password field means real encripted password is stored in `/etc/shadow`

But, We can see that for user `flag01` field for encripted password is not hidden. We can see hashed password `42hDRfypTqqnw`
```
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
```
