def isSafe(processes, available, maxm, allot):
    P = len(processes)

    R = len(available)
 
    finish = [0] * P
 
    safeSeq = [0] * P
 
    work = [i for i in available]
 
    count = 0
    while(count < P):
 
        found = False
        for p in range(P):
 
            if finish[p] == 0:
 
                for j in range(R):
                    if maxm[p][j] - allot[p][j] > work[j]:
                        break
                     
                if j == R - 1:
 
                    for k in range(R):
                        work[k] += allot[p][k]
 
                    safeSeq[count] = processes[p]
                    count += 1
 
                    finish[p] = 1
 
                    found = True
        
        if not found:
            print("System is not in safe state")
            return False

        print("System is in safe state.",
              "\nSafe sequence is: ", end = " ")
        print(*safeSeq)
 
        return True
 
processes = [0, 1, 2, 3, 4]
 
available = [3, 3, 2]
 
maxm = [[7, 5, 3],[3, 2, 2],[9, 0, 2],[2, 2, 2],[4, 3, 3]]
 
allot = [[0, 1, 0],[2, 0, 0],[3, 0, 2],[2, 1, 1],[0, 0, 2]]
 
isSafe(processes, available, maxm, allot)