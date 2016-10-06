# Exercise 10
# Runs
# Input: a binary sequence
# Output: print the length of the logest run (sequence of continuous 1s or zeros


sequence =input("Please enter a binary sequence: ") + 'a'
                                                    # Secure last digit enters the list

runs =[]                            # list of runs
digit1=sequence[0]                  # comparison digit
seq = digit1                        #initiate first sequence


for i in range(1,len(sequence)):
    #print("Seq[i]", sequence[i])
    if digit1 == sequence[i]:       #Check for continious digits
        
        seq += sequence[i]          #Update sequence
        #print("counter=",i)
        #print("Digit1= ",digit1)
        #print(seq)
    else:                           #Sequence disrupted
        #print(i)
        runs.append(seq)            # udate list
        digit1 = sequence[i]        # alter compsrison digit
        seq = sequence[i]           # initiate new sequence
        #print("Digit1= ",digit1)


        
lengths = list(map(len,runs))   
print(max(lengths))

