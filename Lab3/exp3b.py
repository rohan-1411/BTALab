import hashlib
import datetime

class Block:
    num = 0
    def __init__(self, data, previous = 0x0, next = 0x0):
        self.number = self.num
        self.data = data
        self.previous_hash = previous
        self.next_hash = next
        self.next = None
        self.timestamp = datetime.datetime.now()
        self.nonce = 0
        self.hash = None
        self.num += 1
    
    def calculate_nonce(self):
        nonce_max = 10000000
        flag = 0
        i = 0
        while i<nonce_max and flag==0:
            hash1 = hashlib.sha256()
            hash1.update(str(i).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.number).encode('utf-8'))
            if str(hash1.hexdigest())[:5] == '0'*5:
                self.nonce = i
                self.hash = hash1.hexdigest()
                break
            i += 1
        if i>=nonce_max and flag==0:
            self.nonce = nonce_max
            self.hash = hash1.hexdigest()
            
    def display(self):
        return ('Number of Block: ' + str(self.number) + '\nData of block: ' + str(self.data) + '\nHash of block: ' + str(self.hash) + '\nHash of Previous Block: ' + str(self.previous_hash) + '\nHash of Next Hash: ' + str(self.next_hash) + '\nTimestamp: ' + str(self.timestamp) + '\nNonce of Block: ' + str(self.nonce) + '\n')

class Blockchain:
    def __init__(self):
        self.block = Block(data = 'Genesis')
        self.block.calculate_nonce()
        self.head = self.block
        def abc(self):
            return self.block.data
        
    def add(self, block):
        num = self.block.number + 1
        block.previous_hash = self.block.hash
        block.number = num
        block.calculate_nonce()
        self.block.next = block
        self.block.next_hash = block.hash
        self.block = self.block.next
        
    def get_head(self):
        return self.head
    
    def iterate(self):
        head = self.head
        while head:
            print(head.display())
            head = head.next

b = Blockchain()
for i in range(5):
    block = Block('Block '+str(i+1))
    b.add(block)
b.iterate()
        