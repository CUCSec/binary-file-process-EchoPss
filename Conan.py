import struct
import os

def tamper(student_id):
  oname=os.path.abspath(__file__)
  father_name=os.path.dirname(oname)
  global full_name
  full_name=os.path.join(father_name,"lenna.bmp")
  with open(full_name, 'r+b') as f:
    f.seek(54,0)
    for i in range(12):
      if(student_id[i]=='0'):
        f.seek(3*10,1)
      else:
        f.seek(3*int(student_id[i]),1)
      f.write(bytes(3))
      f.seek(-3,1)
  f.close()
      



def detect():
  with open(full_name, 'rb') as f:
    bmp_file_header = f.read(14)

    bm, size, r1, r2, offset = struct.unpack('<2sIHHI', bmp_file_header)

    f.seek(offset)

    count = 12
    offset = 0
    last_offset = 0
    while count > 0:
      color = f.read(3)

      if color == b'\x00\x00\x00':

        if offset - last_offset == 10:
          print(0)
        else:
          print(offset - last_offset)

        last_offset = offset
        count -= 1

      
      offset += 1


if __name__ == '__main__':
  import sys
  tamper(sys.argv[1])

  detect()
