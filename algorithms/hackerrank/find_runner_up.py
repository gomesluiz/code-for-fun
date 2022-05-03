def find_runner_up(n, scores):
    """Find the runner up"""
    return sorted(list(set(scores)), reverse=True)[1]

if __name__ == '__main__':
    # Testing.
    assert find_runner_up(5, [2, 3, 6, 6, 5]) == 5, "Should be 5"
    print("Everything passed!")
