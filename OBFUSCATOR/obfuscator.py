import os
import sys
import zlib
import time
import base64
import marshal
import py_compile

# Select raw_input() or input()
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\n YOUR PYTHON VERSION IS NOT SUPPORTED!")

# Encoding
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))
note = "\x23\x20\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x50\x79\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x0a\x23\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x69\x74\x68\x75\x62\x2e\x63\x6f\x6d\x2f\x68\x74\x72\x2d\x74\x65\x63\x68\x0a\x23\x20\x54\x69\x6d\x65\x20\x3a\x20%s\n\x23\x20\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x0a" % time.ctime()

def banner(): # Program Banner
    print('\033[91m ╔═════════════════════════════════╗\033[0m')
    print('\033[92m ║         OBFUSCATOR             ║\033[0m')
    print('\033[93m ║  PYTHON CODE OBFUSCATOR!       ║\033[0m')
    print('\033[94m ║  AUTHOR : X4X0X4X             ║\033[0m')
    print('\033[95m ║  IP : UNKNOWN                 ║\033[0m')
    print('\033[91m ╚═════════════════════════════════╝\033[0m')
    print()

def menu(): # Program Menu
    print('\033[96m [01] ENCODE MARSHAL\033[0m')
    print('\033[97m [02] ENCODE ZLIB\033[0m')
    print('\033[91m [03] ENCODE BASE16\033[0m')
    print('\033[92m [04] ENCODE BASE32\033[0m')
    print('\033[93m [05] ENCODE BASE64\033[0m')
    print('\033[94m [06] ENCODE ZLIB,BASE16\033[0m')
    print('\033[95m [07] ENCODE ZLIB,BASE32\033[0m')
    print('\033[96m [08] ENCODE ZLIB,BASE64\033[0m')
    print('\033[97m [09] ENCODE MARSHAL,ZLIB\033[0m')
    print('\033[91m [10] ENCODE MARSHAL,BASE16\033[0m')
    print('\033[92m [11] ENCODE MARSHAL,BASE32\033[0m')
    print('\033[93m [12] ENCODE MARSHAL,BASE64\033[0m')
    print('\033[94m [13] ENCODE MARSHAL,ZLIB,B16\033[0m')
    print('\033[95m [14] ENCODE MARSHAL,ZLIB,B32\033[0m')
    print('\033[96m [15] ENCODE MARSHAL,ZLIB,B64\033[0m')
    print('\033[97m [16] SIMPLE ENCODE\033[0m')
    print('\033[91m [17] EXIT\033[0m')
    print()

class FileSize: # Gets the File Size
    def datas(self,z):
        for x in ['BYTE','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [-] ENCODED FILE SIZE : %s\n" % self.datas(dts))
# FileSize('rec.py')

# Encode Menu
def Encode(option,data,output):
    loop = int(eval(_input % " [-] ENCODE COUNT : "))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        sys.exit("\n INVALID OPTION!")

    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TYPEERROR : " + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()

# Special Encode
def SEncode(data,output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output,output)

# Main Menu
def MainMenu():
    try:
        os.system('clear') # os.system('cls')
        banner()
        menu()
        try:
            option = int(eval(_input % " [-] OPTION : "))
        except ValueError:
            sys.exit("\n INVALID OPTION !")

        if option > 0 and option <= 17:
            if option == 17:
                sys.exit("\n THANKS FOR USING THIS TOOL")
            os.system('clear') # os.system('cls')
            banner()
        else:
            sys.exit('\n INVALID OPTION !')
        try:
            file = eval(_input % " [-] FILE NAME : ")
            data = open(file).read()
        except IOError:
            sys.exit("\n FILE NOT FOUND!")

        output = file.lower().replace('.py', '') + '_enc.py'
        if option == 16:
            SEncode(data,output)
        else:
            Encode(option,data,output)
        print("\n [-] SUCCESSFULLY ENCRYPTED %s" % file)
        print(" [-] SAVED AS %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    MainMenu()