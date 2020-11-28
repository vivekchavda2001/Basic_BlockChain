
import datetime # add datetime lib for time

import hashlib # dd hashlib for hashing of blckData
#creating single block of chain 
class Block:


    blckNo = 0 # represent no of block

    blckData = None # represent blckData

    next = None # represent next block

    hash = None #represent hash function of given rnge

    blckNounce = 0 # used once value for block

    previous_hash = 0x0 #represent hashing of previous block

    timestamp = datetime.datetime.now() #represent currunt time and date

    #initialize blckData
    def __init__(self, blckData):
        self.blckData = blckData

  
    def hash(self):
        
        # generates an almost-unique 256-bit signature that represents
        # some piece of text

        h = hashlib.sha256()

        #the input to the SHA-256 algorithm
        #will be a concatenated string
        #consisting of 5 block attributes
        #the blckNounce, blckData, previous hash, timestamp, & block #
        
        h.update(
        str(self.blckNounce).encode('utf-8') +
        str(self.blckData).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blckNo).encode('utf-8')
        )
        #returns a hexademical string
        return h.hexdigest()
      
       #print out the value of a block
    def __str__(self):
        
        return "Block Hash: " + str(self.hash()) + "\Block Number: " + str(self.blckNo) + "\nBlock Data: " + str(self.blckData) + "\nHashes: " + str(self.blckNounce) + "\n--------------"
 #Chain blckData structure to link each and every block in chain      
class Chain:
    

    diff = 20  #difficulty in hash

    maxblckNounce = 2**32 # maximum nounce value
   
    target = 2 ** (256-diff) #target value


    block = Block("Genesis") #initialize first block as Genesis block as per rule

    head = block #initialize first block as head

    # add block in chain
    def add(self, block):
        

        block.previos_huash = self.block.hash() #set the hash of a given block
        #as our new block's previous hash
        
        block.blckNo = self.block.blckNo + 1 #set the block # of our new block
        #as the given block's # + 1, since
        #its next in the chain0

   
        self.block.next = block #update values of head and initialize next block for previous one
        self.block = self.block.next

     #mining block
    def mine(self, block):

        for n in range(self.maxblckNounce): # checking for max nounce in hash
          
            if int(block.hash(), 16) <= self.target:   #from 2 into 0 to 32 is the value of the given block's hash less than our target value?
               
                self.add(block)

                print(block)

                break
            else:
                block.blckNounce += 1
chain = Chain()

# adding 10 blocks as sample

for n in range(10):
    chain.mine(Block("Block " + str(n+1)))
    
# printing 10 blocks

while chain.head != None:
    print(chain.head)
    chain.head = chain.head.next 

