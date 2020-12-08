def main():
    rules = get_rules('input.txt')
    part1(rules, "shiny gold")
    part2(rules, "shiny gold")

def part1(rules, target):
    bag_set = set()

    for bag in rules:
        bag_set.update(check_bags(rules, [bag], target, bag_set))

    print("%d bag colors can eventually contain at least one %s bag" % \
        (len(bag_set), target))

def part2(rules, target):
    num_bags = traverse_bags(1, get_inner_bags(rules, target))
    print("%d individual bags are required inside your single %s bag" % \
        (num_bags, target))

def get_inner_bags(rules, bag):
    inner_bags = rules[bag]
    if not inner_bags:
        return []
    
    return [ (num, bag_name, get_inner_bags(rules, bag_name)) for num, bag_name \
        in inner_bags ]

def traverse_bags(weight, inner_bags):
    total = 0
    if inner_bags:
        for num, _, cur_inner_bags in inner_bags:
            total += (num * (1 + traverse_bags(num, cur_inner_bags)))

    return total

def check_bags(rules, bags, value, visited):
    bag_set = set()

    for bag in bags:
        if bag in visited:
            continue

        inner_bags = [ b[1] for b in rules[bag] ]

        if inner_bags:
            if value in inner_bags:
                bag_set.add(bag)
            elif len(visited.intersection(inner_bags)) > 0:
                bag_set.add(bag)
            else:
                new_set = check_bags(rules, inner_bags, value, visited)
                if new_set:
                    bag_set.update(new_set)
                    bag_set.add(bag)
    
    return bag_set

def get_rules(filename):
    rules = dict()
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        words = line.split()
        bag_color = " ".join(words[:2])
        bag_contents = " ".join(words[4:])
        cur_contents = []

        # If there are other bags inside, add them to the dict
        if bag_contents != "no other bags.":
            for inner_bag in bag_contents.split(","):
                cur_words = inner_bag.strip().split(" ")
                cur_contents.append((int(cur_words[0]), " ".join(cur_words[1:3])))

        rules[bag_color] = cur_contents

    return rules

if __name__ == '__main__':
    main()