def part1(input:str)->int:
    dialStarter = 50 
    instructions = input.split("\n")
    count = 0
    for instruction in instructions:
        if instruction[0]=='L':
            dialStarter = dialStarter-int(instruction[1:])
        else:
            dialStarter = dialStarter+int(instruction[1:])
        dialStarter = dialStarter%100 
        if dialStarter==0:
            count+=1
    return count       

def part2(input:str)->int:
    dialStarter = 50 
    instructions = input.split("\n")
    count = 0
    for instruction in instructions:
        amount = int(instruction[1:])
        for _ in range(amount):
            if instruction[0]=='L':
                dialStarter = (dialStarter-1+100)%100 
            else:
                dialStarter = (dialStarter+1)%100
            if dialStarter==0:
                count+=1
    return count


def main():
    with open("input.txt","r") as file:
        content = file.read()
        content = content[:len(content)-1]
    print(f"part1->{part1(content)}")
    print(f"part2->{part2(content)}")
main()
