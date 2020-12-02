'''
find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
'''
def get_entry_two_sum(entries, target_sum):
    if not entries or len(entries) < 2:
        return None

    complement_dict = get_complement_dict(entries, target_sum)

    for entry in entries:
        if entry in complement_dict:
            return (entry, complement_dict[entry])

    return None

def get_entry_three_sum(entries, target_sum):
    if not entries or len(entries) < 2:
        return None
    
    complement_dict = get_complement_dict(entries, target_sum)

    for complement in complement_dict:
        two_sum = get_entry_two_sum(entries, complement)
        if two_sum is not None:
            return (complement_dict[complement], two_sum[0], two_sum[1])
    
    return None

def get_complement_dict(entries, target_sum):
    complement_dict = {}

    # Create dictionary of target_sum complement to entry
    for entry in entries:
        complement = target_sum - entry
        complement_dict[complement] = entry
    
    return complement_dict

def get_sorted_entries_from_file(filename):
    entries = []
    with open(filename, 'r') as f:
        # Convert each line to a number and add to entries list
        entries = [ int(num_str.strip()) for num_str in f.readlines() ]

    entries.sort()
    return entries

if __name__ == '__main__':
    entries = get_sorted_entries_from_file('entries.txt')
    target = 2020
    two_sum = get_entry_two_sum(entries, target)
    print("Product of two sum for target of {0} is {1}".format(target, two_sum[0] * two_sum[1]))
    three_sum = get_entry_three_sum(entries, target)
    print("Product of three sum for target of {0} is {1}".format(target, three_sum[0] * three_sum[1] * three_sum[2]))