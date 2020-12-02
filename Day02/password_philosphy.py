from collections import Counter

def main():
    num_valid_passwords = count_valid_passwords('input.txt')
    print("Valid passwords with policy 1: {0} and with policy 2: {1}".format( \
        num_valid_passwords[0], num_valid_passwords[1]))

def count_valid_passwords(filename):
    # number of valid passwords for policy 1
    num_valid_passwords_1 = 0
    # number of valid passwords for policy 2
    num_valid_passwords_2 = 0

    # Cache character count Counters for passwords we have already seen
    seen_password_counter = {}
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        line_split = line.split(':')
        policy = line_split[0].split()
        password = line_split[1].strip()
        policy_char = policy[1]
        policy_counts = policy[0].split('-')
        policy_min = int(policy_counts[0])
        policy_max = int(policy_counts[1])

        if is_valid_password_policy1(password, policy_char, policy_min, policy_max, \
            seen_password_counter):
            num_valid_passwords_1 += 1
        if is_valid_password_policy2(password, policy_char, policy_min, policy_max):
            num_valid_passwords_2 += 1

    return (num_valid_passwords_1, num_valid_passwords_2)

'''
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times a given 
letter must appear for the password to be valid. For example, 1-3 a means that 
the password must contain a at least 1 time and at most 3 times.
'''
def is_valid_password_policy1(password, policy_char, policy_min, policy_max, \
    seen_password_counter):
    password_counter = Counter()

    # Look in cache to see if we already have the password's counter
    if password in seen_password_counter:
        password_counter = seen_password_counter[password]
    else:
        password_counter = Counter(password)
        seen_password_counter[password] = password_counter

    if policy_char in password_counter and \
        (password_counter[policy_char] >= policy_min and \
        password_counter[policy_char] <= policy_max):
        return True

    return False

'''
Each policy actually describes two positions in the password, where 1 means 
the first character, 2 means the second character, and so on. (Be careful; 
Toboggan Corporate Policies have no concept of "index zero"!) Exactly one 
of these positions must contain the given letter. Other occurrences of the 
letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
'''
def is_valid_password_policy2(password, policy_char, policy_idx1, policy_idx2):
    matching_positions = 0

    if password[policy_idx1 - 1] == policy_char:
        matching_positions += 1
    if password[policy_idx2 - 1] == policy_char:
        matching_positions += 1

    if matching_positions == 1:
        return True

    return False

if __name__ == "__main__":
    main()