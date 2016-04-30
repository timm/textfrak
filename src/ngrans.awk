BEGIN {
    n=3
    empty(buffer)
}

$1 {
    push(buffer, $1)
    m = length(buffer) - n
    if (m > 0) {
	for(j= m ; j < length(buffer); j++)
	    printf("%s ",buffer[j])
	print("")
    }}

function push(a,x) { a[ length(a) + 1 ] = x }
function empty(a)  { split("",a,"") }
	 
