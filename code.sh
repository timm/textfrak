
downcase() { cat - | tr A-Z a-z; }
words()    { cat - | gawk '{for(i=1;i<=NF;i++) print $i}' ; }
tokenize() { cat - | sed 's/[,\.\(\)i;‘’,{}:;]/ /g' ; }

eg1() { cat data/fashion.txt | tokenize | downcase | words | sort | uniq -c; }
