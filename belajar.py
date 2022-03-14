def sequentialsearch(alist, value):
    pos=0
    found=False
    for pos in range (len(alist)) :
        if alist[pos]== value:
            found=True
            print(found)
            break
        else:
            return found
data=[1,7,8,3,5]
nilai=sequentialsearch(data,1)
print(nilai)
# cara membuta linkedlist kita terlabih dahulu membuat class node
class node:
    def __init__(self,element,next=None):
        self.element=element
        self.next=next
# mendefenisikan atribut atribut
class linkedlist:
    def __init__ (self):
        self.head=None # digunakan untuk menunjuk simpul pertama dalam list
        self.tail=None # di gunakan untuk simpul terakhir dalam tuple
        self.size=0 # du gunakan menyatakan jumlah simpul terakhir list 
# memeriksa ukuran list
    def isempty(self):
        return self.size == 0 # di dunakan untuk mengecek ukuran list
     
    def addfirst(self, element):
        newnode=node(element,self.head)# menambah simpul pada posisi pertama 
        self.head= newnode # head menuju simpul baru 
        self.size+=1 # menambah ukuran list 
        if self.tail == None:  # jika list hanya satu simpul
            self.tail=self.head
    def getfirst(self):
        if self.isempty():
            return None
        else:
            return self.head.element
    def removefirst(self):
        if not self.isempty():
            temp= self.head
            self.head=self.head.next
            self.size -=1 # mengurangi ukuran list
            del temp
    #menambah simpul baru ke dalam list terakhir 
    def addlast(self,element):
        newnode=node(element)
        #jika list masih kosong
        if self.tail==None:  
            self.head=newnode # head menuju simpul baru
            self.tail=self.head # tail menuju ke head
        else:
            self.tail.next=newnode
            self.tail = self.tail.next
        self.size +=1
    #mendapatkan elemen pada simpul terakhir
    def getlast(self):
        if self.isempty():
            return None 
        else:
             return self.tail.element
    #menghapus simpul terakhir 
    def removelast(self):
        if not self.isempty():
            if self.size== 1:
                temp = self.head
                self.head = None
                self.tail = None 
                self.size = 0
                del temp
            else:
                current = self.head
                while current .next!= self.tail:
                    current = current.next
                temp = self.tail
                self.tail = current 
                self .tail.next = None
                self.size -= 1
                del temp
    # menampilkan element-element pada setiap simpul di dalam list
    def __str__(self):
        s = '['
        current= self.head
        while current != None:
            s+= str(current.element)
            if current != self.tail:
                s += ','
            current = current.next
        s += ']'
        return s
    def __repr__(self) :
        return self.__str__()                
                
            

    

    
    
        
    
      
        
        