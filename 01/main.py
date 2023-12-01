from src.TaskSolver import TaskSolver

#FILENAME = "input-sm.txt"
#FILENAME = "input-sm2.txt"
FILENAME = "input.txt"
#FILENAME = "test.txt"

PART_TWO = True

def main():
    ts = TaskSolver()
    result = ts.solve(FILENAME, PART_TWO)
    print(result) #part 1 = 54951, part 2 = 55218

main()