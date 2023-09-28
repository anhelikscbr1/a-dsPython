
class Plates():
    def __init__(self, max_plates):
        self.max_plates = max_plates
        self.stacks = []
    
    def push(self, value):
        stacks = self.stacks
        max_plates = self.max_plates
        if(len(stacks) == 0):
            stacks.append([value])
            return
        if(len(stacks[-1]) < max_plates):
            stacks[-1].append(value)
            return
        if(len(stacks[-1]) == max_plates):
            stacks.append([value])
            return
    def pop(self):
        stacks = self.stacks
        if(len(stacks) == 0):
            print("No plates in the stacks")
            return
        if(len(stacks[-1]) == 1):
            stacks.pop()
            return
        stacks[-1].pop()
        return
        
myPlates = Plates(2)
myPlates.push(1)
myPlates.push(2)
myPlates.push(3)
myPlates.push(4)
myPlates.push(5)
print(myPlates.stacks)
myPlates.pop()
myPlates.pop()


print(myPlates.stacks)