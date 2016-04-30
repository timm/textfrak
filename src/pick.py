from __future__ import division,print_function
import sys,re
sys.dont_write_bytecode = True

class o(object):
  def __init__(i,**d): 
    i.has().update(d)
  def has(i)  : return i.__dict__
  def items(i): return i.has().items()
  def __getitem__(i, k): return i.has()[k]
  def __setitem__(i, k, v): i.has()[k]=v
  def __repr__(i):
    return i.__class__.__name__+str(i.has())
  def show(i) : 
    print(i.__class__.__name__)
    pretty(i.has(),1)

def often(d,enough=10**32):
  n, lst = 0, []
  for x in d: 
    n   += d[x]
    lst += [(d[x],x)]
  lst = sorted(lst, reverse=True)
  while enough > 0:
    r = random.random()
    for freq,thing in lst:
      r -= freq*1.0/n
      if r <= 0:
        yield thing
        enough -= 1
        break

def lines(file=None):
  if file:
    for line in open(file):  yield line
  else:
    while True:
      try:   yield raw_input("")
      except (EOFError):
        break

def rows(file=None,bad=r'["\'\t\r\n]',sep='[ ]*::[ ]*',nums=[]):
  def str2num(token):
    try: return int(token)
    except ValueError:
      return float(token)
  def words(line):
    return strips(re.sub(bad,"",line).split(sep))
  def strips(line):
    for i,x in enumerate(line):
      line[i] = x.strip()
    return line
  for line in lines(file):
    data = words(line)
    for num in nums:
      data[num] = str2num(data[num])
    yield data


class P:
  all = {}
  def __init__(i,x,p):
    i.pairs={}
    i.x=x
    i.p=p
    P.all += [i]
  def add(i,y,p) :
    old = i.pairs.get(y,[])
    old += [(p,x)]

ps = []
for row in rows(sep="::",nums=[0,2]):
  p = P(row[2])
  
  
  
  k = row[1]
  l = d.get(k,o(what=row[2],has={}))
  d = l.has.get(row[-1],o(what=row[-1],has={}))
  
  print(row)    
