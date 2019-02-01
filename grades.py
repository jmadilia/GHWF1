
def compute_hw_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades)/len(grades)

def drop_two_lowest(grades):
    if len(grades) < 2:
        grades = []
    grades.pop(min(grades))
    grades.pop(min(grades))
