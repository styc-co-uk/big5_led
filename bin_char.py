#! python
# codr inspired by ref https://github.com/will127534/AdafruitGFX-ChineseFont-Addon/blob/master/hash.py

def bin_char(char):

    # encode to big5
    c = char.encode('big5')
    # print('big5: %X%X' % (c[0],c[1]))

    # get bytes

    font_size = 24

    if font_size == 24:
        # 24*24 = 576 bits = 72 bytes
        arraySize = 72
        BytePerline = 3
        pass
    if font_size == 15:
        arraySize = 30
        BytePerline = 2
        pass

    offset = 0

    hi = c[0]
    lo = c[1]

    if lo>=0xa1:
        serCode = (hi - 0xa1) * 157 + lo + 0x3f - 0xa1 + 1
    else:
        serCode = (hi - 0xa1) * 157 + lo - 0x3f

    if serCode >= 472 & serCode < 5872:
        offset = (serCode - 472) * arraySize
    elif serCode >= 6281 & serCode <= 13973:
        offset = (serCode - 6281) * arraySize + 5401 * arraySize
        pass

    # print('offset: %d' % offset)

    # import font
    font = open('./stdfont.24f','rb')

    import numpy as np
    binchar = np.zeros([font_size,BytePerline*8])
    font.seek(offset)
    for x in range(font_size):
        line = font.read(BytePerline)
        data = line.hex()
        linebin = bin(int(data,base=16))[2:].zfill(BytePerline*8)
        binchar[x] = np.array(list(linebin), dtype=int)

    return binchar