def main():
    passports = get_passports('input.txt')
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    num_valid_passports = get_num_valid_passports(passports, required_fields)
    print("Number of valid passports: %d" % num_valid_passports)

def get_num_valid_passports(passports, required_fields):
    num_valid_passports = 0

    for key in passports:
        cur_passport_dict = passports[key]
        is_valid = True
        for field in required_fields:
            if field not in cur_passport_dict or not is_valid_field(cur_passport_dict, field):
                is_valid = False
            
        if is_valid:
            num_valid_passports += 1
        is_valid = True

    return num_valid_passports

def is_valid_field(passport_dict, field):
    value = passport_dict[field]
    if len(value) == 0:
        return False

    if field == 'byr' and value.isnumeric() \
        and (int(value) in range(1920, 2003)):
        return True
    elif field == 'iyr' and value.isnumeric() \
        and (int(value) in range(2010, 2021)):
        return True
    elif field == 'eyr' and value.isnumeric() \
        and (int(value) in range(2020, 2031)):
        return True
    elif field == 'hgt':
        if ('cm' in value) and \
            (int(value.replace('cm', '')) in range(150, 194)):
            return True
        elif ('in' in value) and \
            (int(value.replace('in', '')) in range(59, 77)):
            return True
    elif field == 'hcl':
        if value[0] == '#' and value.replace('#', '').isalnum():
            return True
    elif field == 'ecl' and value in \
        ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    elif field == 'pid' and len(value) == 9 and value.isnumeric(): 
        return True

    return False

def get_passports(filename):
    counter = 0
    passport_dict = {}
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    cur_dict = {}
    for line in lines:
        if line == '\n':
            passport_dict[counter] = cur_dict
            cur_dict = {}
            counter += 1
        else:
            for s in line.split():
                key_value_pair = s.strip().split(':')
                cur_dict[key_value_pair[0]] = key_value_pair[1]

    return passport_dict

if __name__ == '__main__':
    main()