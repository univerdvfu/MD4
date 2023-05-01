

class CriptoMD:
    def __init__(self):
        self.A = 0x67452301
        self.B = 0xEFCDAB89
        self.C = 0x98BADCFE
        self.D = 0x10325476

    def cripto(self, text):
        binar = []

        for i in text:
            binar.append(bin(ord(i))[2:].zfill(8))


        self.binText = ''.join(binar)
        binLenText = bin(len(self.binText))[2:].zfill(64)
        if (len(self.binText) == 0) or (len(self.binText) == 512):
            count = 447
        else:
            count = 447 - (len(self.binText)%512)

        self.binText += '1' + '0'* count + str(binLenText)

        self.stepOne(self.binText)
        print(len(self.binText))
        print(self.binText)

    def stepOne(self,binText):

        self.textBlock = []

        countBlock = int(len(binText)/512)
        for i in range(countBlock):
            row = []
            for j in range(16):
                row.append(binText[j*32:(j+1)*32])
            self.textBlock.append(row)
        print(len(self.textBlock[0][15]))

#print(int(1024/512))
text ='1'*50 #input(str('Your massege: '))
print(len(text))
# text =bin(2)
# text += 0x00
# print(text)
md4 = CriptoMD()
md4.cripto(text)