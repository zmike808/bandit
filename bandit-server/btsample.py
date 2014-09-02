from bcoding import bencode, bdecode
import hashlib
import sys
import base64
import urblib

if len(sys.argv) == 3:
  tfile = open(sys.argv[1], 'rb')
  afile = open(sys.argv[2], 'rb')
  verifyFileContent(tfile, afile)
  realfile.close()
  torrentFile.close()
else:
  print('enter torrent filename and filename')
  exit()

def verifyFileContent(torrentFile, actualFile):
  torrent = bdecode(f)
  plength = torrent['info']['piece length']
  thash = torrent['info']['pieces']
  flength = torrent['info']['length']
  realfile = actualFile
  realfile.seek(0,2)
  realfileLength = realfile.tell()
  realfile.seek(0,0)
  if flength != realfileLength:
    print("File sizes do not match! Invalid file!")
    return False
  piece = realfile.read(plength)
  digest = hashlib.sha1(piece).digest()
  while piece != bytes():
    piece = realfile.read(plength)
    if piece != bytes():
      phash = hashlib.sha1(piece).digest()
      digest = digest + phash
  if digest == thash:
    print("file integrity is intact!!")
    print("MAGENT URI:", genenateMagentURI(torrent))
    return True
  else:
    print("kid, what are you trying to pull? get that malicious shit outta here")
    return False

def genenateMagentURI(metadata):
  hashcontents = bencode.bencode(metadata['info'])
  digest = hashlib.sha1(hashcontents).digest()
  b32hash = base64.b32encode(digest)
  params = {'xt': 'urn:btih:%s' % b32hash,
            'dn': metadata['info']['name'],
            'tr': metadata['announce'],
            'xl': metadata['info']['length']}
  paramstr = urllib.urlencode(params)
  magneturi = 'magnet:?%s' % paramstr
  return magenturi