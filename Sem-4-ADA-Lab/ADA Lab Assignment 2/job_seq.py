def job_sequencing(jobs):
    # sort jobs by profit (highest first)
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * max_deadline
    total_profit = 0
    
    for job in jobs:
        # try to place job before its deadline
        for j in range(job[1]-1, -1, -1):
            if slots[j] == -1:
                slots[j] = job[0]
                total_profit += job[2]
                break
    
    return slots, total_profit


jobs = [
    ('j1', 2, 100),
    ('j2', 1, 50),
    ('j3', 2, 10),
    ('j4', 1, 20)
]

print(job_sequencing(jobs))
