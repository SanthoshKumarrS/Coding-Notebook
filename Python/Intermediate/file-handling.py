#File-Objects

with open('file.txt',"r") as rf:
    with open('file_copy.txt',"w") as wf:
        for line in rf:
            wf.write(line)

    
    