class Stack:
    def __init__(self):
        """bu yerda items(listga) malumot saqlanadi"""
        self.items = []

    def is_empty(self):
        """bu yerda listda malumot bolsa false malumot bolmasa True"""
        return len(self.items) == 0

    def push(self, item):
        """bu yerda listga malumot qoshiladi"""
        self.items.append(item)

    def pop(self):
        """bu yerda listni oxiridan malumot ochiriladdi"""
        if not self.is_empty():
             return self.items.pop()
        else:
             print("Error: Stack is empty")

    def peek(self):
        """bu yerda listni oxiridan malumot korsatadi"""
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        """bu yerda listni ichida necta malumot borligini korsatadi"""
        return len(self.items)



# stack = Stack()
#
#
# stack.push(1)
# stack.push("ab")
# stack.push(3)
# stack.push("ID")
# stack.push(5)
# stack.push("6")
# stack.push(7)

# print(stack.is_empty())

# print(stack.items)

# print(stack.items)

# for i in stack.items:
#     print(i)

# top_item = stack.pop()
# print(top_item)
# print(stack.items)
#
# top_item = stack.pop()
# print(top_item)
# print(stack.items)

# peeked_item = stack.peek()
# print(peeked_item)


# print(stack.size())