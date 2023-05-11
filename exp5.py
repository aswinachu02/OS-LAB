def Waiting(processes, n, bt, wt, at):
    servicetime = [0] * n
    servicetime[0] = 0
    wt[0] = 0
    for i in range(1, n):
        servicetime[i] = (servicetime[i - 1] + bt[i - 1])
        wt[i] = servicetime[i] - at[i]
        if (wt[i] < 0):
            wt[i] = 0

def TurnAround(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def avg(processes, n, bt, at):
    wt = [0] * n
    tat = [0] * n
    Waiting(processes, n, bt, wt, at)
    TurnAround(processes, n, bt, wt, tat)
    print("Processes    BurstTime    ArrivalTime    WaitingTime    Turn-AroundTime   CompletionTime \n")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time = tat[i] + at[i]
        print(" ", i + 1, "\t\t", bt[i], "\t\t", at[i], "\t\t", wt[i], "\t\t ", tat[i], "\t\t ", compl_time)
    print("\nAverage waiting time = %.5f "%(total_wt /n))
    print("\nAverage turn around time = ", total_tat / n)

if __name__ =="__main__":
    processes = [1, 2, 3]
    n = 3
    burst_time = [5, 9, 6]
    arrival_time = [0, 3, 6]
    avg(processes, n, burst_time, arrival_time)