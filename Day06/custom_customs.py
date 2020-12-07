def main():
    lines = get_lines('input.txt')
    group_answers = get_answers(lines)
    print(group_answers[:6])
    print("Sum of answer counts for all groups: %d" % sum([ len(answer_tuple[1]) for answer_tuple in group_answers ]))
    print("Number of questions to which everyone answered 'yes': %d" % get_unanimous_answer_count(group_answers))

def get_unanimous_answer_count(group_answers):
    answer_count = 0

    for answer_tuple in group_answers:
        num_people = answer_tuple[0]
        answer_dict = answer_tuple[1]
        cur_count = 0
        
        for key in answer_dict.keys():
            if answer_dict[key] == num_people:
                cur_count += 1
            
        answer_count += cur_count

    return answer_count

def get_answers(lines):
    group_answers = []

    cur_answer_dict = {}
    cur_group_size = 0
    for line in lines:
        if len(line) == 0:
            group_answers.append((cur_group_size, cur_answer_dict))
            cur_answer_dict = {}
            cur_group_size = 0
        else:
            cur_group_size += 1
            for c in line:
                if c in cur_answer_dict:
                    cur_answer_dict[c] += 1
                else:
                    cur_answer_dict[c] = 1

    group_answers.append((cur_group_size, cur_answer_dict))
    return group_answers

def get_lines(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    return [ line.strip() for line in lines]

if __name__ == '__main__':
    main()