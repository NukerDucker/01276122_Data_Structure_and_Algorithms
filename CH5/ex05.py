class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def is_empty(self):
        return self.head is None
    
    def size(self):
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next
            
        return count
    
    def copy(self):
        new_list = LinkedList()
        current = self.head
        
        while current:
            new_list.append(current.data)
            current = current.next
            
        return new_list

    def __str__(self):
        result = []
        current = self.head
        
        while current:
            result.append(str(current.data))
            current = current.next
            
        return " -> ".join(result)

def digits_counter(num):
    return 1 if num == 0 else len(str(abs(num)))

def max_abs_value(ll):
    max_val = 0
    current = ll.head
    while current:
        max_val = max(max_val, abs(current.data))
        current = current.next
    return max_val

def check_all_same(ll):
    if ll.is_empty():
        return True
    first_value = ll.head.data
    current = ll.head.next
    
    while current:
        if current.data != first_value:
            return False
        current = current.next
        
    return True

def merge_buckets(buckets, ll):
    ll.head = ll.tail = None
    for i in range(9, -1, -1):
        current = buckets[i].head
        while current:
            if current.data >= 0:
                ll.append(current.data)
            current = current.next
    for i in range(10):
        current = buckets[i].head
        while current:
            if current.data < 0:
                ll.append(current.data)
            current = current.next

def print_buckets(buckets):
    for i in range(10):
        bucket_items = []
        bucket_current = buckets[i].head
        while bucket_current: 
            if bucket_current.data >= 0:
                bucket_items.append(str(bucket_current.data))
            bucket_current = bucket_current.next
            
        bucket_current = buckets[i].head
        while bucket_current:
            if bucket_current.data < 0:
                bucket_items.append(str(bucket_current.data))
            bucket_current = bucket_current.next
                
        print(f"{i} : {' '.join(bucket_items)}")

def radix_sort(ll):
    if ll.is_empty():
        return ll

    if check_all_same(ll):
        print("------------------------------------------------------------")
        print("0 Time(s)")
        return ll
    max_val = max_abs_value(ll)

    digits_count = digits_counter(max_val)

    for digit in range(digits_count):
        print("------------------------------------------------------------")
        print(f"Round : {digit + 1}")
        
        buckets = [LinkedList() for _ in range(10)]
        current = ll.head
        
        while current:
            bucket_index = (abs(current.data) // (10 ** digit)) % 10
            buckets[bucket_index].append(current.data)
            current = current.next
        
        print_buckets(buckets)
        
        ll.head = None
        ll.tail = None
        
        merge_buckets(buckets, ll)
    
    print("------------------------------------------------------------")
    print(f"{digits_count} Time(s)")
    return ll

def main():
    usr_input = input("Enter Input : ")
    items = [int(num) for num in usr_input.split()]
    ll = LinkedList()
    for item in items:
        ll.append(item)
    
    unsorted_ll = ll.copy()
    ll_sorted = radix_sort(unsorted_ll)
    
    print("Before Radix Sort :", ll)
    print("After  Radix Sort :", ll_sorted)

if __name__ == "__main__":
    main()