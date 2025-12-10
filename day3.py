def part1(list_joltages) -> int:
    res = []
    for joltages in list_joltages:
        print(joltages)
        joltages = [int(d) for d in joltages.strip()]
        b = max(joltages)
        b_idx = joltages.index(b)
        if b_idx<len(joltages)-1: 
            sb = max(joltages[b_idx+1:])
        
        if b_idx == len(joltages) - 1:
            sb = max(joltages[0:len(joltages)-1])
            b, sb = sb, b
        elif b_idx == 0:
            sb = max(joltages[1:])
        print(f"b->{b} sb->{sb}") 
        res.append(int(str(b) + str(sb)))
    
    return sum(res)


def main():
    with open("input.txt","r") as file:
        content = file.read()
        content = content[:len(content)-1]
        joltages = content.split("\n")
    
    print(part1(joltages))
main()
