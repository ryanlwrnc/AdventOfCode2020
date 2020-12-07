def main():
    boarding_passes = get_boarding_passes('input.txt')
    row_cols = get_row_cols(boarding_passes)
    seat_ids = [ ((row_col[0] * 8) + row_col[1]) for row_col in row_cols if row_col[0] != - 1 and row_col[1] != - 1 ]
    print("The highest seat id on a boarding pass is %s" % max(seat_ids))
    missing_seat = get_missing_seat(row_cols)
    print("The missing seat is %s" % missing_seat)

def get_missing_seat(row_cols):
    rows = [ row_col[0] for row_col in row_cols ]
    row_dict = {}
    
    for row_col in row_cols:
        row = row_col[0]
        col = row_col[1]

        if row in row_dict:
            row_dict[row].append(col)
        else:
            row_dict[row] = [col]
    
    for row in range(min(rows) + 1, max(rows)):
        cur_cols = row_dict[row]
        if len(cur_cols) != 8:
            for col in range(8):
                if col not in cur_cols:
                    return (row * 8) + col
    return -1  

'''
Returns a list of tuples of the row and columns of each seat number 
from the boarding passes
'''
def get_row_cols(boarding_passes):
    row_cols = []

    for boarding_pass in boarding_passes:
        if len(boarding_pass) != 10:
            continue
        cur_row_col = (get_binary_partition_val(boarding_pass, 127, 0, 'B', 'F', 0, 6), \
            get_binary_partition_val(boarding_pass, 7, 0, 'R', 'L', 7, 9))

        row_cols.append(cur_row_col)

    return row_cols

def get_binary_partition_val(boarding_pass, high, low, high_char, low_char, \
    start_idx, end_idx):
    diff = 0
    for i in range(start_idx, end_idx + 1):
        c = boarding_pass[i]
        diff = (high - low) + 1
        if c == low_char:
            high -= (diff / 2)
        elif c == high_char:
            low += (diff / 2)
        else:
            return -1
    return int(high)

def get_boarding_passes(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    return [ line.strip() for line in lines ]

if __name__ == "__main__":
    main()