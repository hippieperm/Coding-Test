
def solution(sides):
    max_val = 0
    mid = 0
    min_val = 0

    if sides[0] >= sides[1] and sides[0] >= sides[2]:
        max_val = sides[0]
        mid = sides[1] if sides[1] >= sides[2] else sides[2]
        min_val = sides[2] if sides[1] > sides[2] else sides[1]
    elif sides[1] >= sides[0] and sides[1] >= sides[2]:
        max_val = sides[1]
        mid = sides[0] if sides[0] >= sides[2] else sides[2]
        min_val = sides[2] if sides[0] > sides[2] else sides[0]
    elif sides[2] >= sides[0] and sides[2] >= sides[1]:
        max_val = sides[2]
        mid = sides[0] if sides[0] >= sides[1] else sides[1]
        min_val = sides[1] if sides[0] > sides[1] else sides[0]

    print(f'max : {max_val}  /mid : {mid}  /min : {min_val}')
    result = 1 if max_val < (mid + min_val) else 2
    print(result)
    return result