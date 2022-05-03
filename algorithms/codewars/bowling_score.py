def is_strike(frame):
    return frame[0] == 'X' 

def is_spare(frame):
    pass

def bowling_score(frames):
    """Caculate a ten-pin bowling score."""


    frames = [list(frame) for frame in frames.split()]
    score  = 0
    num_frames = len(frames)
    for i in range(0, num_frames):

        if is_strike(frames[i]):

        else:
            pass

        if is_spare(frame[i]):
            pass
        else:
            pass

        frame = list(map(int, frames[i]))
        score += sum(frame)

    print(score)
    return score 

if __name__=="__main__":
    assert bowling_score('11 11 11 11 11 11 11 11 11 11') == 20
