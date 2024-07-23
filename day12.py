class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_list(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.next
        print(llstr + 'None')

    def insert_at_the_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_end(data)

    def get_length(self):
        count = 0
        itr = self.head   
        while itr:
            count += 1 
            itr = itr.next
            
        return count

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next  
            return     
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
    def insert_at_index(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_beginning(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    
    def insert_after_value(self,after_value,data):
        itr=self.head
        while itr:
            if itr.data==after_value:
                itr.next=Node(data,itr.next)
                return
            itr=itr.next
        print(f'{after_value} was not found')   
    
    def remove_by_value(self,data,value):
        if self.head is None:
            print('empty list')
            return
        if self.head.data==value:
            self.head=self.head.next
            return
        
        itr=self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next

        print(f'{value} not found in the list')
            
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(['games', 'data', 'james', 'yam'])
    print('Length:', ll.get_length())
    ll.remove_at_index(2)
    #ll.insert_at_index(2,'ram')
    ll.insert_after_value('yam','maggi')
    ll.print_list()
