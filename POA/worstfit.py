def find_best(blocks,p,memory):
    pi = -1
    
    for i,b in enumerate(blocks):
        if b >= p and memory[i] == -1: 
            if pi == -1:
                pi = i
            elif b < blocks[pi]:
                pi = i
        
    return pi
    
blocks = [200,400,600,500,300,250]
process = [357,210,468,491]
print(f"Blocks: {blocks}\nProcess : {process}\n")
memory = [-1] * len(blocks)
for p in process:
    pos = find_best(blocks,p,memory)
    if pos != -1:
        memory[pos] = p
        print(f"Memory allocation for {p} : {memory}")
    else:
        print(f"Memory allocation for {p} : No space to allocate")

print(f"Final answer : {memory}")
