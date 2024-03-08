import os
import multiprocessing

def child_process():
    print("Child Process")

def parent_process():
    print("Parent Process")

if __name__ == "__main__":
    p = multiprocessing.Process(target=child_process)
    p.start()  # Start the child process
    p.join()  # Wait for the child process to finish
    parent_process()