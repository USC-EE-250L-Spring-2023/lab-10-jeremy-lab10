# Name: Jeremy Pogue
# Link to GitHub Repo: https://github.com/USC-EE-250L-Spring-2023/lab-10-jeremy-lab10

import time
import numpy as np
from typing import List, Optional

import threading
import pandas as pd
import requests
import plotly.express as px

def generate_data() -> List[int]:
    """Generate some random data."""
    return np.random.randint(100, 10000, 1000).tolist()

def process1(data: List[int]) -> List[int]:
    """Given a (presumably large) list of integers, find the next largest prime number for each integer.

    Args:
        data: A list of integers. 

    Returns:
        List[int]: Another list of integers, containing the next largest prime number of each integer in the original list.
    """
    def foo(x):
        """Find the next largest prime number."""
        while True:
            x += 1
            if all(x % i for i in range(2, x)):
                return x
    return [foo(x) for x in data]

def process2(data: List[int]) -> List[int]:
    """Given a (presumably large) list of integers, find the next largest perfect square for each integer.

    Args:
        data: A list of integers. 

    Returns:
        List[int]: Another list of integers, containing the next largest perfect square of each integer in the original list.
    """
    def foo(x):
        """Find the next largest perfect square."""
        while True:
            x += 1
            if int(np.sqrt(x)) ** 2 == x:
                return x
    return [foo(x) for x in data]

def final_process(data1: List[int], data2: List[int]) -> float:
    """Given two (presumably large) lists of integers, find the index-by-index differences of the lists, then find the mean of the resulting list.

    Args: 
        data1: A list of integers
        data2: Another list of integers, presumably of the same length as data1

    Returns:
        float: The mean of the index-by-index differences of the two input lists
    """
    return np.mean([x - y for x, y in zip(data1, data2)])

offload_url = 'http://localhost:5001' # TODO: Change this to the IP address of your server

def run(offload: Optional[str] = None) -> float:
    """Run the program, offloading the specified function(s) to the server.
    
    Args:
        offload: Which function(s) to offload to the server. Can be None, 'process1', 'process2', or 'both'.

    Returns:
        float: the final result of the program.
    """
    data = generate_data()
    if offload is None: # in this case, we run the program locally
        data1 = process1(data)
        data2 = process2(data)
        ans = final_process(data1, data2)
    elif offload == 'process1':
        data1 = None
        def offload_process1(data):
            nonlocal data1
            # Send a POST request to the server with the input data
            response = requests.post(f'{offload_url}/process1', json={'data':data})
            data1 = response.json()
        thread = threading.Thread(target=offload_process1, args=(data,))
        thread.start()
        data2 = process2(data)
        thread.join()
        # Question 2: Why do we need to join the thread here?
        # Question 3: Are the processing functions executing in parallel or just concurrently? What is the difference?
        #   See this article: https://oxylabs.io/blog/concurrency-vs-parallelism
        #   ChatGPT is also good at explaining the difference between parallel and concurrent execution!
        #   Make sure to cite any sources you use to answer this question.
        ans = final_process(data1, data2)
    elif offload == 'process2':
        data2 = None
        def offload_process2(data):
            nonlocal data2
            # Send a POST request to the server with the input data
            response = requests.post(f'{offload_url}/process2', json={'data':data})
            data2 = response.json()
        thread = threading.Thread(target=offload_process2, args=(data,))
        thread.start()
        data1 = process1(data)
        thread.join()
        ans = final_process(data1, data2)
    elif offload == 'both':
        data1 = None
        data2 = None
        def offload_processboth(data):
            nonlocal data1
            response = requests.post(f'{offload_url}/process1', json={'data':data})
            data1 = response.json()
            nonlocal data2
            response = requests.post(f'{offload_url}/process2', json={'data':data})
            data2 = response.json()
        thread = threading.Thread(target=offload_processboth, args=(data,))
        thread.start()
        thread.join()
        ans = final_process(data1, data2)

    return ans 

def main():
    # TODO: Run the program 5 times for each offloading mode, and record the total execution time
    #   Compute the mean and standard deviation of the execution times
    #   Hint: store the results in a pandas DataFrame, use previous labs as a reference
    modes = [None, 'process1', 'process2', 'both']
    samples = 5

    data = []
    for mode in modes:
        times = []
        for i in range(samples):
            start_time = time.time()
            run(mode)
            times.append(time.time() - start_time)
        times_mean = np.mean(times)
        times_std = np.std(times)
        data.append([mode, times_mean, times_std])

    # TODO: Plot makespans (total execution time) as a bar chart with error bars
    # Make sure to include a title and x and y labels
    df = pd.DataFrame(data, columns=['mode', 'times_mean', 'times_std'])
    fig = px.bar(
        df,
        x=['None', 'process1', 'process2', 'both'],
        y='times_mean',
        error_y='times_std',
        labels={
            'x': "Offloading Mode",
            "times_mean": "Processing Time (in s)",
            "times_std": "Standard Deviation (in s)"
        },
        title="Processing Time of Different Distributed Computing Methods"
    )

    # TODO: save plot to "makespan.png"
    fig.write_image("makespan.png")

    # Question 4: What is the best offloading mode? Why do you think that is?
    # Question 5: What is the worst offloading mode? Why do you think that is?
    # Question 6: The processing functions in the example aren't very likely to be used in a real-world application. 
    #   What kind of processing functions would be more likely to be used in a real-world application?
    #   When would you want to offload these functions to a server?
    
    
if __name__ == '__main__':
    main()
