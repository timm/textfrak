 { a[$2] = $1 }

 END { 
   sorted(a,s)
   for(i=1;i<=100;i++) 
     print select(s)
 }

function sorted(a,s,   z,n,i,j,sum) {
  split("",s,"")
  for(i in a) 
    sum += a[i]
  for(i in a) {
    v    = a[i]/sum + rand()/100
    a[i] = v
    z[v] = i
  }
  n = asort(a,tmp)
  for(i=n;i>=1;i--) {
    j = length( s ) + 1
    s[ j ]["p"] = tmp[i]
    s[ j ]["v"] = z[tmp[i]]   }
}
function select(s,   r,n,i) {
  r = rand()
  n = length(s)
  for(i=1;i <= n; i++) {
    r -= s[i]["p"] 
    if (r <= 0)
      return s[i]["v"] }
  return s[n]["v"]
}
