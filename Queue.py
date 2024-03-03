class Queue:
    def __init__(self):
        """bu yerda items(listga) malumot saqlanadi"""
        self.items = []

    def is_empty(self):
        """bu yerda listda malumot bolsa false malumot bolmasa True"""
        return len(self.items) == 0

    def enqueue(self, item):
        """bu yerda listga malumot qoshiladi"""
        self.items.append(item)

    def dequeue(self):
        """bu yerda listni boshidan malumot ochiriladdi"""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        """bu yerda listni boshidan malumot korsatadi"""
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        """bu yerda listni ichida necta malumot borligini korsatadi"""
        return len(self.items)



queue = Queue()

queue.enqueue(1)
queue.enqueue("ab")
queue.enqueue(3)
queue.enqueue("ID")
queue.enqueue(5)
queue.enqueue("6")
queue.enqueue(7)



# print(queue.is_empty())
# print(queue.items)
# queue.enqueue("a")
# print(queue.items)

# top_item = queue.dequeue()
# print(top_item)
# print(queue.items)
#
# top_item = queue.dequeue()
# print(top_item)
# print(queue.items)

print(queue.items)
peeked_item = queue.peek()
print(peeked_item)


# print("This is Stack")
# for i in queue.items[-1::-1]:
#     print(i)
#
# print("This is Queue")
# for i in queue.items:
#     print(i)


# print(queue.size())