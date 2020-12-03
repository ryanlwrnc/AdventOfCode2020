TREE_CHAR = '#'
OPEN_CHAR = '.'

def main():
    grid = get_grid('input.txt')
    output_template = "%s trees encountered when using a slope of right %d and down %d"
    num_trees = count_trees(grid, 3, 1)
    print(output_template % (num_trees, 3, 1))

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for slope in slopes:
        count = count_trees(grid, slope[0], slope[1])
        print(output_template % (count, slope[0], slope[1]))
        product *= count
    
    print("Product of slopes = %s" % product)
    
def count_trees(grid, slope_right, slope_down):
    num_trees = 0
    cur_row = slope_down

    if cur_row >= len(grid):
        return num_trees

    cur_col = slope_right % (len(grid) - 1)
    
    while True:
        if grid[cur_row][cur_col] == TREE_CHAR:
            num_trees += 1

        cur_row += slope_down
        if cur_row >= len(grid):
            break
        cur_col = (cur_col + slope_right) % (len(grid[cur_row]))
    
    return num_trees

def get_grid(filename):
    with open(filename, 'r') as f:
        return [ list(line.strip()) for line in f.readlines() ]

if __name__ == "__main__":
    main()