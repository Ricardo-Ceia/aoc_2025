def is_invalid_id(id:str)->bool:
    size = len(id)
    if size%2!=0:
        return False
    if size==2:
        return (int(id[0])-int(id[1]))==0
    beg_to_middle = int(id[0:(size//2)])
    middle_to_end = int(id[size//2:size])
    if (beg_to_middle-middle_to_end)==0:
        return True
    return False
    


def part1(list_ids)->int:
    res_list = []
    for ids in list_ids:
      min = int(ids[0])
      max = int(ids[1])
      for i in range(min,max+1):
          if is_invalid_id(str(i)):
              res_list.append(int(i))
    return sum(res_list)
def main():
    splited_text = []  
    with open("input.txt","r") as file:
        while True:
            line = file.readline()[:-1]
            if not line:
                break
            splited_text.append(line.split("-"))

    print(part1(splited_text))

main()
