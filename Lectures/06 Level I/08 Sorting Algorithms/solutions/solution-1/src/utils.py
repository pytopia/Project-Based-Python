import time
import sys
from typing import Callable, List

def measure_time_complexity(func: Callable, list: List[int]) -> float:
    """
    Measures time complexity of a function

    :param func: The function to test
    :type func: Callable
    :param list: The list to pass to the function
    :type list: List[int]
    :return: The time taken by the function
    :rtype: float
    """ 
    start_time = time.time()
    func(list)
    end_time = time.time()
    return end_time - start_time

def measure_space_complexity(func: Callable, list: List[int]) -> int:
    """
    Measures space complexity of a function

    :param func: The function to test
    :type func: Callable
    :param list: The list to pass to the function
    :type list: List[int]
    :return: The memory used by the list
    :rtype: int
    """ 
    start_memory = sys.getsizeof(list)
    func(list)
    end_memory = sys.getsizeof(list)
    return end_memory - start_memory

if __name__ == "__main__":
    assert measure_time_complexity(sorted, [3,1,2]) > 0
    assert measure_space_complexity(sorted, [3,1,2]) >= 0
