# Lab 10
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Jeremy Pogue

## Link to GitHub Repo
https://github.com/USC-EE-250L-Spring-2023/lab-10-jeremy-lab10

## Lab Question Answers

Question 1: Under what circumstances do you think it will be worthwhile to offload one or both
of the processing tasks to your PC? And conversely, under what circumstances will it not be
worthwhile?

Answer: I imagine that distributed computing is a balance between processing/computing time and offloading/transfer time. For processes that we expect to take a
long time, we need to minimize the processing time as much as possible and the time taken to transfer the instructions is likely negligible. So, in this case, it is
probably worthwhile to offload the processing task to a PC. However, for very simple calculations, the amount of time saved in processing time is likely outweighed
by the amount of time lost in sending instructions. So, in this case, offloading would not be worth it. Another consideration to make here is whether a certain process
has subtasks which can be performed in parallel between a slower device and a faster device. This increases the utility of distributed computing, as it allows us to 
potentially use the computing power of two devices for the entire duration of the processing time (thus expediting computation).

Question 2: Why do we need to join the thread here?

Answer: By writing thread.join(), the program pauses and waits for each thread to complete its computation before proceeding. This is necessary because the
outputs of each subprocess, data1 and data2, are used as an input for a final process. Therefore, it is important that each subprocess is finished before
we move on to the final process. This is reflected by the directed nature of the provided graph (process1 --> final_process; process2 --> final_process) in that specific
order.

Question 3: Are the processing functions executing in parallel or just concurrently? What is the difference?

Answer: Threading allows functions to execute concurrently, NOT in parallel. Parallel computing implies that different processes are being performed on separate CPU
cores, where the computation and activity of one process does not affect the processing time of the other. Parallel computing is true multitasking. In contrast, with
concurrent processing, all computations are performed on the same CPU, and the CPU simply interleaves (alternates between) the two processes so that they are completed 
alongside each other. This is what threading does, rather than splitting computation between CPUs.
Source: ChatGPT

Question 4: What is the best offloading mode? Why do you think that is?

Answer: According to the results, the best offloading mode involved offloading only process2, as this method resulted in the fastest processing time. Perhaps, this was
because process2 was more computationally expensive than process1. In this case, offloading the process to a more capable machine (my PC) would have improved processing
time. Also, this makes sense given the context of processes 1 and 2: there are fewer perfect squares than prime numbers, so we expect that finding the next largest
perfect square for any given number would take more time than finding the next largest prime number. Thus, we expect process2 to take longer than process1, in which case,
offloading it would allow for faster processing.

Question 5: What is the worst offloading mode? Why do you think that is?

Answer: The worst offloading mode involved offloading only process1, as this method resulted in the slowest processing time. This implies that the time spent 
transferring data and instructions for process1 to the more capable machine (PC) outweighed the reduction in computation time. This is logical, as y the same logic described in Question 4, it is likely that process2 was more computationally expensive than process1. So, offloading process1 didn't give the slower device (RPi) much of an advantage.

Question 6: The processing functions in the example aren't very likely to be used in a real-world application.
What kind of processing functions would be more likely to be used in a real-world application? When would you 
want to offload these functions to a server?

Answer: Offloading could be helpful in the real world when working with very large databases. Take, for example, an Amazon database storing the information
of every user, transaction, and vendor that has been registered on the site. Using my PC's computing power, it would take incredible amounts of time to 
perform about any function on this database, but especially ones that would require pulling from many pieces of data (the total number of jackets ever sold, the 
average amount spent by users in a particular region, etc). In this situation, offloading these functions to a more capable server would be essential. 