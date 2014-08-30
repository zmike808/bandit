from bcoding import bencode, bdecode
import hashlib
import sys

if len(sys.argv) < 3:
  print('enter torrent filename and filename')
  exit()
with open(sys.argv[1], 'rb') as f:
  torrent = bdecode(f)
  plength = torrent['info']['piece length']
  thash = torrent['info']['pieces']
  realfile = open(sys.argv[2], 'rb')
  piece = realfile.read(plength)
  digest = hashlib.sha1(piece).digest()
  while piece != bytes():
    piece = realfile.read(plength)
    if piece != bytes():
      phash = hashlib.sha1(piece).digest()
      digest = digest + phash
  if digest == thash:
    print("file integrity is intact!!")
  else:
    print("kid, what are you trying to pull? get that malicious shit outta here")
  realfile.close()
