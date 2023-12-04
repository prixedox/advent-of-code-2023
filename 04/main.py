from src.TaskSolver import TaskSolver
from src.FileReader import FileReader

#FILENAME = "input-sm.txt"
#FILENAME = "input-sm2.txt"
FILENAME = "input.txt"

PART_TWO = True

def main():
    ts = TaskSolver()
    result = ts.solve(FILENAME, PART_TWO)
    print(sum(result))

main()