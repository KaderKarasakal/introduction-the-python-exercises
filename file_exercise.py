def process_file(fname):
    count = 0 
    with open(fname,'r') as file:
        for line in file:
            if line.startswith("From "):
                count += 1
                words=line.split()
                if len(words)>1:
                    print(words[1])
        
    print("There were", count, "lines in the file with From as the first word")

fname = input("Enter file name: ")
process_file(fname)


