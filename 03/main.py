from src.TaskSolver import TaskSolver

FILENAME = "input-sm.txt"
#FILENAME = "input-sm2.txt"
#FILENAME = "input.txt"

PART_TWO = True

def main():
    ts = TaskSolver()
    result = ts.solve(FILENAME, PART_TWO)
    print(result)

main()