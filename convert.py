import sys

from markdown2Mathjax import sanitizeInput, reconstructMath
from markdown2 import markdown

if (len(sys.argv)==1):
  print('no input specified')
  raise SystemExit

infile = sys.argv[1]

with open(infile, 'r') as f:
    mdfile = f.read()

tmp = sanitizeInput(mdfile)
mdtext = markdown(tmp[0])
finalOutput = reconstructMath(mdtext,tmp[1])

print finalOutput.encode('utf8')
