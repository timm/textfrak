
fashion()  { cat data/fashion.txt; }
downcase() { cat - | tr A-Z a-z ; }
words()    { cat - | gawk '{for(i=1;i<=NF;i++) if ($i) print $i}' ; }
tokenize() { cat - | sed 's/[,\.\(\);‘’,{}:;]/ /g'  ; }
ngrams()   { cat - | awk '
             BEGIN { split("",a,"") }
                   { a[ length(a) + 1 ] = $1
                     m = length(a) - '$1'
                     if (m > 0) {
	                for(j= m+1 ; j <= length(a); j++)
	                   printf("%s ",a[j])
	                print("")
                   }}'  | sort
           }	     
	     
eg1() { fashion | tokenize | downcase |
	words | ngrams 3; } 
