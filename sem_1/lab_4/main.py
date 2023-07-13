class Node():
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev__ = prev
        self.__next__ = next


    def get_data(self):
        return self.__data


    def __str__(self):
        if self.__next__ is None:
            next = None
        else:
            next = self.__next__.get_data()
        if self.__prev__ is None:
            prev = None
        else:
            prev = self.__prev__.get_data()        
        return "data: {}, prev: {}, next: {}".format(self.get_data(), prev, next)

    
class LinkedList():
    def __init__(self, first=None, last=None):
        self.__first__ = first
        self.__last__ = last
        self.__length = 0
        if first is None and last is not None:
            raise ValueError("invalid value for last")
        if first is not None and last is None:
            self.__length = 1
            self.__first__ = Node(first)
            self.__last__ = self.__first__
        if (first is not None) and (last is not None):
            self.__length = 2
            self.__first__ = Node(first)
            self.__last__ = Node(last)
            self.__first__.__next__ = self.__last__
            self.__last__.__prev__ = self.__first__
            

    def __len__(self):
        return self.__length


    def append(self, element):
        if self.__first__ is None:
            self.__length = self.__length + 1
            self.__init__(element) 
        else:
            self.__length = self.__length + 1
            self.__last__.__next__ = Node(element, prev = self.__last__)
            self.__last__ = self.__last__.__next__           
            
    def __str__(self):
        if self.__first__ is None:
            return "LinkedList[]"
        if self.__first__ is not None:
            buffer = self.__first__
            list_r = str(buffer)
            while buffer.__next__ is not None:
                buffer = buffer.__next__
                list_r += "; " + str(buffer)
            return "LinkedList[length = {}, [{}]]".format(len(self), list_r)     
    
    
    def pop(self):
        if self.__length == 0:
            raise IndexError("LinkedList is empty!")
        else:
            self.__last__ = self.__last__.__prev__
            self.__last__.__next__ = None
            self.__length = self.__length - 1
 

    def popitem(self, element):
        if self.__first__ is None:
            raise KeyError("{} doesn't exist!".format(element))
        if len(self) == 1 and self.__first__.get_data() == element:
            self.clear()
        elif self.__first__.get_data() == element:
            self.__first__ = self.__first__.__next__
            self.__first__.__prev__ = None
            self.__length = self.__length - 1
        elif self.__last__.get_data() == element:
            self.pop()
        else:
            bufer = self.__first__
            while bufer.get_data() != element and bufer.__next__ != None:
                bufer = bufer.__next__
            if bufer.__next__ == None:
                raise KeyError("{} doesn't exist!".format(element))
            bufer.__prev__.__next__ = bufer.__next__
            bufer.__next__.__prev__ = bufer.__prev__
            
            
    def clear(self):
        self.__length = 0
        self.__init__() 