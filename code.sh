
fashion()  { cat data/fashion.txt | ascii ; }
ascii()    { cat - | tr -cd "[:print:]"  | sed  's/\r//g' ;  }
downcase() { cat - | tr A-Z a-z ; }
words()    { cat - | gawk '{for(i=1;i<=NF;i++) if ($i) print $i}' ; }
tokenize() { cat - | sed  's/[,\(\);‘’,{}:;]/ /g'  ; }
ngrams()   { cat - | gawk '
             BEGIN { split("",a,"") }
                   { a[ length(a) + 1 ] = $1 # here, $1 is the actual word
                     m = length(a) - '$1' # here, $1 is the ngram size
                     if (m > 0) {
	                for(j= m+1 ; j <= length(a); j++)
	                   printf("%s ",a[j])
	                print("")
                   }}'  
}

trendy() { cat - | gawk '/(chic|fash|cloth|weave|textile|fabric|mode)/'; }

lines() { cat - |wc -l; }

has() { cat - | grep $1 ; }
hasnt() { cat -  | grep -v $1 ; }
eg1() { fashion  | tokenize | #downcase |
        words  | ngrams 4 | sort; }

eg2() { eg1 | uniq -c | sort -n | gawk '$1 > 3'; }

eg3() { eg1 | uniq -c | sort -n  ;  }

eg4() {
  fashion  | tokenize | downcase | words  | ngrams 4 | trendy | sort > /tmp/eg4.out;
  }

eg5() {
  eg4
  grep  more /tmp/eg4.out > /tmp/eg5.more
  grep less /tmp/eg4.out > /tmp/eg5.less
}

clean() {
   rm /tmp/eg*
}



r() { reload; }
