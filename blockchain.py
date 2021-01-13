import hashlib 
from datetime import datetime  

class block : 
    def __init__ (self, index , data , difficulty = 5 )  : 
        self.data = data  
        self.index = index   
        self.nonce = 1 
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")     
        self.hash = self.mine_block(difficulty) 
 
    def get_hash(self) :    
        return hashlib.sha256( self.data.encode('utf-8') +  self.timestamp.encode('utf-8') + str(self.nonce).encode('utf-8')).hexdigest()      

    def mine_block(self , difficulty ) :  
        while True :  
            self.hash = self.get_hash()
            if self.hash[:difficulty] == "0" * difficulty:  
                return  self.hash
            else : 
                self.nonce += 1 
                continue  
                

class blockchain :  

    def __init__ (self) : 
        self.blockchain = [block('0','genesis block')]    

    def create_genesis_block (self) :    
        return block( 0 , 'genesis block ' )     

    def show_blocks(self) :      
        #check first the validity of the blockchain 
        valid = self.check_validity()   
        counter = 0  
        for i in  self.blockchain :  
            for attr , value  in i.__dict__.items() :    
                print(f'[+] {attr} : {value}')    
            print()

    def add_block(self, data ) :    
        new_block = block ( len(self.blockchain) , data , )     
        new_block.prev_hash = self.blockchain[-1].hash      

        # add the new block 
        self.blockchain.append(new_block) 

    def check_validity(self) :  
        if len(self.blockchain) == 1 : return  
        blocks = self.blockchain 
        for i in range ( 1, len(self.blockchain ) ) :        
            if blocks[i].prev_hash != blocks[i-1].hash : return i 
            else : 
                continue  
        return True 


def main() :    
    chain = blockchain()   
    chain.add_block('test')  

    chain.show_blocks() 
    chain.add_block('test123')   
    chain.show_blocks() 

            

 

if __name__ == "__main__" : 
    main() 

