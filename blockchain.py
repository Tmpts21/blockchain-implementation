#blockchain implentation with python :D  
import hashlib 
from datetime import datetime


class block : 
    def __init__ (self, index , data)  : 
        self.data = data  
        self.hash = self.get_hash() 
        self.index = index  
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_hash(self) : 
        return hashlib.sha256( self.data.encode('utf-8')).hexdigest() 

class blockchain : 
    def __init__ (self) : 
        self.blockchain = [block('0','genesis block')]    

    def create_genesis_block (self) :   
        return block( 0 , 'genesis block ' )     

    def show_blocks(self) :      
        #check first the validity of the blockchain 
        is_valid = self.check_validity()  
        counter = 0 
        for i in  self.blockchain :  
            counter +=1    
            for attr , value  in i.__dict__.items() :    
                if counter >= is_valid : 
                    print(f'[x] {attr} : {value} ' )
                else : 
                    print(f'[+] {attr} : {value}')    
            print()

    def add_block(self, data ) :    
        new_block = block ( len(self.blockchain) , data +  datetime.now().strftime("%d/%m/%Y %H:%M:%S"))   
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

    def update_block(self, index , data ) :   

        self.blockchain[index].data = data  
        self.blockchain[index].hash = self.blockchain[index].get_hash()   

        return True  

def main() :    
    chain = blockchain() 
    while True :  
        user = input ("[A] : add block \n[B] show block chain \n[C] exit")  
        if user.lower() == 'a' :   
            data = input("enter data") 
            chain.add_block(data) 
        elif user.lower() == 'b' : 
            chain.show_blocks() 
        elif user.lower() == 'c' : 
            exit() 
        else : 
            print("invvalid input")   
            print("try again") 

            

 

if __name__ == "__main__" : 
    main() 






