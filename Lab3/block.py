import hashlib
import datetime

class Block:
    num = 0
    def __init__(self, data, previous = 0x0, next = 0x0):
        self.number = self.num
        self.data = data
        self.previous = previous
        self.next = next
        self.hash = None
        self.timestamp = datetime.datetime.now()
        self.num += 1
    
    def calc_hash(self):
        max = 10000000
        flag = 0
        i = 0
        h = ''
        while i<max and flag==0:
            h = hashlib.sha256()
            h.update(str(self.number).encode('utf-8') + str(self.data).encode('utf-8') +
            str(self.previous).encode('utf-8') + str(self.next).encode('utf-8') + str(i).encode('utf-8'))
            if str(h.hexdigest())[:4] == '0'*4:
                self.nonce = i
                self.hash = h.hexdigest()
                break
            i += 1
        if i>=max and flag==0:
            self.nonce = max
            self.hash = h.hexdigest()
    
    def disp(self):
        print('Number of Block: ' + str(self.number) + '\nData of block: ' + str(self.data) + '\nHash of block: ' + str(self.hash) + '\nHash of Previous Block: ' + str(self.previous) + '\nHash of Next Block: ' + str(self.next) + '\nTimestamp: ' + str(self.timestamp) + '\nNonce of block: ' +
        str(self.nonce))

b = Block('First Block')
b.calc_hash()
b.disp

