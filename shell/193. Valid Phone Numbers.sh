#Bash script to check for valid phone number
#Valid: XXX-XXX-XXXX or (XXX) XXX-XXXX

grep -E '^[0-9]{3}-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$' file.txt

<<COMMENTS
  ^ start line
  $ end line
  \ escape trailing character
  () grouping
  [0-9]{3}-[0-9]{3}-[0-9]{4}$
  XXX-XXX-XXXX
  ([0-9]{3}\) [0-9]{3}-[0-9]{4}
  (XXX) XXX-XXXX
COMMENTS
