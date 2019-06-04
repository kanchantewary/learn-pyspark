filter multiple patterns using grep:
you can put your patterns into a file, and use the -f flag. So grep -f patternlist.txt files. Where patternlist.txt is simply:
aaa
bbb
