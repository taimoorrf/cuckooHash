import time

class hashTable:
    maxSize = 11
    offset = 0
    firstTable = [None] * maxSize
    secondTable = [None] * maxSize
    currSizeOne = 0
    currSizeTwo = 0
    cycleCounter = 0
    def printTables(self):
        print("\n")
        print("Table 1:")
        for value in self.firstTable:
            print(value)
        
        print("\n")
        
        print("Table 2:")        
        for value in self.secondTable:
            print(value) 
        print("\n")

    def hashOne(self, value):
        return int(((2**self.offset) * value) % self.maxSize)
    
    def hashTwo(self, value):
        return int((((2**self.offset) * (value / self.maxSize))) % self.maxSize)
    
    def search(self, value):
        indexOne = self.hashOne(value)
        indexTwo = self.hashTwo(value)
        if self.firstTable[indexOne] == value:
            print(value, " in table 1 at index ", indexOne)
            return [1, indexOne]
        elif self.secondTable[indexTwo] == value:
            print(value, "in table 2 at index ", indexTwo)
            return [2, indexTwo]
        else:
            print("Value not in either of the tables")
            return None
        
    def delete(self, value):
        index = self.search(value)
        if index is not None:
            if index[0] == 1:
                self.firstTable[index[1]] = None
                if self.currSizeOne != 0:
                    self.currSizeOne = self.currSizeOne - 1
            elif index[0] == 2:
                self.secondTable[index[1]] = None
                if self.currSizeTwo != 0:
                    self.currSizeTwo = self.currSizeTwo - 1
        else:
            return
    
    def rehash(self):
        self.cycleCounter = 0
        self.offset = self.offset + 1
        tempTableOne = self.firstTable
        tempTableTwo = self.secondTable
        self.firstTable = [None] * self.maxSize
        self.secondTable = [None] * self.maxSize
        for value in tempTableOne:
            if value != None:
                self.insert(value)
        for value in tempTableTwo:
            if value != None:
                self.insert(value)
        

    def insert(self, value):
        key = self.hashOne(value)
        if self.firstTable[key] == None:
            self.firstTable[key] = value
            self.currSizeOne = self.currSizeOne + 1
        else:
            tempVal = self.firstTable[key]
            self.firstTable[key] = value
            self.currSizeOne = self.currSizeOne + 1
            tempKey = self.hashTwo(tempVal)
            if self.secondTable[tempKey] == None:
                self.secondTable[tempKey] = tempVal
                self.currSizeTwo = self.currSizeTwo + 1
            else: 
                tempVal2 = self.secondTable[tempKey]
                self.secondTable[tempKey] = tempVal
                self.currSizeTwo = self.currSizeTwo + 1
                self.cycleCounter = self.cycleCounter + 1
                if self.cycleCounter == self.maxSize:
                    print("Rehashing...")
                    self.rehash()
                    time.sleep(1)
                    self.insert(tempVal2)
                    return False
                else:    
                    self.insert(tempVal2)
        return True
                


    def menu(self):
        while True:
            print("\n")
            print("1- Search for a value in the tables.")
            print("2- Insert a value in the tables.")
            print("3- Delete a value from the tables.")
            print("4- Print both the tables.")
            print("0- Exit.")
            choice = input()

            if choice == "1":
                value = input("Insert the value you want to look up: ")
                self.search(int(value))
            elif choice == "2":
                value = input("Insert the value you want to insert: ")
                self.insert(int(value))
            elif choice == "3":
                value = input("Insert the value you want to delete: ")
                self.delete(int(value))
                print(value, "deleted successfully")
            elif choice == "4":
                self.printTables()
            elif choice == "0":
                break
            else:
                print("Invalid input")
        
    

def main():
    myTable = hashTable()
    myTable.menu()
    
main()



