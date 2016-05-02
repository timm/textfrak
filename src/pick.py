from __future__ import division,print_function
import sys,re,random,string
sys.dont_write_bytecode = True





def rows(file=None,bad=r'["\'\t\r\n]',sep='\s+',nums=[]):
  def lines():
    if file:
      for line in open(file):  yield line
    else:
      while True:
        try:   yield raw_input("")
        except (EOFError):
          break
  def str2num(token):
    try: return int(token)
    except ValueError:
      return float(token)
  def words(line):
    line=re.sub(bad,"",line)
    return [item for item in map(string.strip, re.split(sep, line))
             if len(item) > 0]
  def strips(line):
    for i,x in enumerate(line):
      line[i] = x.strip()
    return line
  for line in lines():
    data = words(line)
    for num in nums:
      data[num] = str2num(data[num])
    yield data

def say(*lst):
  for x in lst: sys.stdout.write(str(x))
  sys.stdout.flush()

def any(pairs):
  r = random.random()
  for freq,thing in pairs:
    r -= freq
    if r <= 0:
      return thing
  return pairs[-1][1]

class node:
  def __init__(i):
    i.n=0
    i.kids={}
    i.pairs=[]
  def add(i,lst) :
    if lst:
      i.pairs=[]
      k = lst[0]
      if k in i.kids:
        v= i.kids[k]
        v.n += 1
        return v.add(lst[1:])
      else:
        kid = i.kids[k] = node()
        kid.k = k
        kid.n = 1
        kid.add(lst[1:])
  def any(i):
    if i.kids:
      i.prep()
      one = any(i.pairs)
      return [one.k] + one.any()
    else:
      return []
  def prep(i):
    if not i.pairs:
      i.pairs=[]
      sum=0
      for kid in i.kids.values():
        sum += kid.n
        i.pairs += [(kid.n, kid)]
      i.pairs = sorted(map(lambda x: (x[0]/sum,x[1]),
                           i.pairs),
                       reverse=True)
      for kid in i.kids.values():
        kid.prep()
  def show(i,indent='|.. ', lvl=0):
    for k in sorted(i.kids.keys()):
      kid = i.kids[k]
      print("=",indent*lvl +  str(k), kid.n)
      kid.show(indent=indent,lvl=lvl+1)

l =[  list('abcd'), list('abcd'), list('abcd'),list('abce'),
     list('akbk'),
     list('akbk')
     ]
# n = node()
# for one in l:
#   n.add(one)

# n.prep()
# n.show()
# for _ in xrange(100):
#    print("X", ''.join(n.any()))



#n.show()


def gen(want=[], phrases=5, file=None):
  n=node()
  for row in rows(file):
    n.add(row)
  found=0
  uppers = [v for v in n.kids.values() if v.k[0].isupper()]
  while found < 10:
    last = None
    out=[]
    out = [random.choice(uppers).k]
    last = out[-1]
    for _ in xrange(phrases):
      more = n.kids[last]  if last in n.kids else n
      more = more.any()
      first = more[0]
      last = more[-1]
      out += more
    if set(out) & set(want) and last[-1] == "." :
      out =  ' '.join(out)
      if len(out) < phrases*15:
        found += 1
        print("\n",out)
    

gen(["Chanel","clothing.","jewellry","women",
     "dressing","chic","fashion","Fashion","dress",
     "clothes","vestimentary", "clothing,","cloth",
     "weave","textile","fabric","mode"],
    phrases=15)





    
