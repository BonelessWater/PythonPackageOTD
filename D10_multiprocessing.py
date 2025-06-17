import logging


import multiprocessing as mp
import time

def cpu_task(n):
    start = time.time()
    result = sum(i**2 for i in range(n))
    logging.info(f"Task {n} completed in {time.time()-start:.2f}s")
    return result

if __name__ == "__main__":
    tasks = [50000000] * 4
    
    # Sequential execution
    start_time = time.time()
    sequential_results = [cpu_task(n) for n in tasks]
    sequential_time = time.time() - start_time
    
    # Parallel execution
    start_time = time.time()
    with mp.Pool(processes=4) as pool:
        parallel_results = pool.map(cpu_task, tasks)
    parallel_time = time.time() - start_time
    
    logging.info(f"Sequential: {sequential_time:.2f}s")
    logging.info(f"Parallel:   {parallel_time:.2f}s") 
    logging.info(f"Speedup:    {sequential_time/parallel_time:.2f}x")