import hashlib
import json

class Block:
    
    def __init__(self, index, timestamp, data, previousHash = ''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        return hashlib.sha256((str(self.index) + self.timestamp + self.previousHash + json.dumps(self.data) + str(self.nonce)).encode('utf-8')).hexdigest()

    def mineBlock(self, difficulty):
        buckets = ['0'] * difficulty
        while(list(self.hash[0:difficulty]) != buckets):
            self.nonce += 1
            self.hash = self.calculateHash();
        
        print("BLOCK MINED: ", self.hash)
    
class Blockchain:
    
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 3
    
    def createGenesisBlock(self):
        return Block(0, "01/01/2017", "Genesis Block", "0")

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)

    def isChainValid(self):
        for i in range(len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]

            if (currentBlock.hash != currentBlock.calculateHash()):
                return False
        
            if (currentBlock.previousHash != previousBlock.hash):
                return False
        
        return True

blockchain = Blockchain()
print("Mining block 1...")
blockchain.addBlock(Block(1, "09/12/2017", { 'amount': 5 }))

print("Mining block 2...")
blockchain.addBlock(Block(2, "09/12/2017", { 'amount': 7 }))