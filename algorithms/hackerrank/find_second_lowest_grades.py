def find_second_lowest_grade(grades):
    """Find the second lowest grade in list of [['student', grade]]."""
    scores = sorted(list(set([subl[1] for subl in grades]))) 
    return scores

if __name__ == '__main__':
    print(find_second_lowest_grade([['eu', 10], ['tu', 10], ['ele', 9]]))
