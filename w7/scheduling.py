"""
Each job j has:
 - Weight(priority): wj
 - Length: lj
 - completion_times cj: sum of job lengths l(1->j)
 - weighted: wj*cj
Objective: minimize sum of weighted completion_times of all jobs
"""

def scheduling(jobs):
    """
    job: tuple(weight, length)
    return jobs in decreasing order of (w - l)
    """
    jobs = [(w, l, w-l) for w, l in jobs]
    scheduled = sorted(jobs, key=lambda x: (x[2], x[0]), reverse=True)
    return scheduled


print scheduling([(1,3), (5,3), (5,5), (4,2)])
