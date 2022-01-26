import zlib
def adui_encode(string):
    bi = string.encode('utf8')
    bi = zlib.compress(bi)
    bits = []
    for b in bi:
        f = str(bin(b // 16))[2:]
        s = str(bin(b % 16))[2:]
        bits.extend((f, s))
    for i, bit in enumerate(bits):
        bits[i] = '0'*(4-len(bit))+bit
    code = ''.join(bits)
    code = code.replace('0', '啊').replace('1', '对')
    return code


def adui_decode(code):
    code = code.replace('啊', '0').replace('对', '1')
    assert not len(code) % 8
    byts = ''
    for n in range(len(code)//8):
        h = str(hex(int(code[8*n:8*n+8], 2)))[2:]
        h = '0'*(2-len(h))+h
        byts = byts + h
    string = zlib.decompress(bytes.fromhex(byts))
    string = string.decode('utf8')
    return string


with open('adui', 'w') as f:
    f.write(adui_encode('https://www.bilibili.com/video/BV1GJ411x7h7'))
with open('adui') as f:
    print(adui_decode(f.read()))