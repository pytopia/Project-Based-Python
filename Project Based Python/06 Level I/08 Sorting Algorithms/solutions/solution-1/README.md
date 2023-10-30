# Python Sorting Algorithms Project Report

## Introduction
This project aimed to evaluate the efficiency of three key sorting algorithms: Bubble Sort, Insertion Sort, and Selection Sort. The goal of this project was to assess these algorithms' suitability under different conditions, i.e., different input sizes.

## Directory Structure
The project has the following directory structure:

```
.
├── run.ipynb                                       # main Jupyter notebook file
├── bubble_sort.py                                  # module implementing the Bubble Sort algorithm
├── insertion_sort.py                               # module implementing the Insertion Sort algorithm
├── selection_sort.py                               # module implementing the Selection Sort algorithm
└── utils.py                                        # utility module for measuring time and space complexity
```

## Requirements
To run the project, the following packages are required:

- Python3.7+
- Matplotlib
- Streamlit

to install the packages, run the following command:

```bash
pip install -r requirements.txt
```

## Implementation
Each algorithm was implemented in a separate Python module. The modules were then imported into a final interactive Jupyter notebook 'run.ipynb'. This implementation generated different-sized lists (10 - 10,000 elements long) and applied each of the sorting algorithms to these lists. The time and space complexity of sorting each list via each algorithm was computed, storing the results. The results of these computations are then visualized using Python's Matplotlib library, with two line plots being generated for each algorithm's time and space complexities.

## Results
The results of the project should show line graphs indicating the changes in time and space complexity for each sorting algorithm as list sizes increase.

## How to Run
1. Clone the project or download the files in your local environment.
2. Navigate to the directory containing `run.ipynb`.
3. Start Jupyter Notebook by typing `jupyter notebook` on your command line or terminal.
4. Open `run.ipynb` in Jupyter Notebook.
5. Run all cells in the notebook.

## Conclusion
This project aimed to enhance understanding of the efficiency and scalability of different sorting algorithms. 

## Recommendations
Potential improvements for this project could be the incorporation of additional sorting algorithms, allowing for a wider comparison. 
