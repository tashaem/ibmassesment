def lookforsize():
    if m>n:
        print("No")
        exit()
    else:
        avail = False
        for i in range(m):
            avail=True
            for j in range(n):
                if len(m_sizes[i])>1:
                    if (m_sizes[i][-1]=="S"):
                        if (n_sizes[j][-1]=="S") and (len(n_sizes[j])>len(m_sizes[i])):
                            avail = False
                    elif (m_sizes[i][-1]=="L"):  
                        if (n_sizes[j][-1]!="L"):
                            avail = False
                        elif (n_sizes[j][-1]=="L") and (len(n_sizes[j])<len(m_sizes[i])):
                            avail = False
                elif m_sizes[i]=="S":
                    if (len(n_sizes[j])>1) and (n_sizes[j][-1]=="S"):
                        avail = False
                elif m_sizes[i]=="M":
                    if (n_sizes[j][-1]=="S"):
                        avail = False
                elif m_sizes[i]=="L":
                    if (n_sizes[j][-1]=="S") or (n_sizes[j]=="M"):
                        avail = False

                if avail==True:
                    break

            if avail==False:
                print("No")
                exit()
                    
        if avail==True:
            print("Yes")
            exit()


import sys
n = int(input())
n_sizes = input()
m = int(input())
m_sizes = input()

lookforsize()