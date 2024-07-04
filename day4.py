passports = []
with open("input day4", 'r') as file:
    i=0
    passport = []
    for row in file:
        if row=="\n":
            passports.append(passport)
            i+=1
            passport=[]
        else:
            for field in row.removesuffix("\n").split(' '):
                passport.append(field)
    passports.append(passport)

validPassports=0
for passport in passports:
    validate = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
        "cid": False
    }
    for field in passport:
        key = field[:field.find(':')]
        if validate[key] == False:
            validate[key] = True

    if validate["byr"] and validate["iyr"] and validate["eyr"] and validate["hgt"] and validate["hcl"] and validate["ecl"] and validate["pid"]:
            validPassports+=1
            
print("Valid passports (part 1):", validPassports)

#Part 2

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

validPassports=0
for passport in passports:
    validate = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
        "cid": False
    }

    for field in passport:
        key = field[:field.find(':')]
        value = field[field.find(':')+1:]
        if key == "byr" and len(value) == 4 and 1920 <= int(value) <= 2002:
            validate[key] = True
        elif key == "iyr" and len(value) == 4 and 2010 <= int(value) <= 2020:
            validate[key] = True
        elif key == "eyr" and len(value) == 4 and 2020 <= int(value) <= 2030:
            validate[key] = True
        elif key == "hgt" and ((value[-2:] == "cm" and 150 <= int(value[:-2]) <= 193) or (value[-2:] == "in" and 59 <= int(value[:-2]) <= 76)):
            validate[key] = True
        elif key == "hcl" and value.startswith('#') and len(value[1:])==6 and is_hex(value[1:]):
            validate[key] = True
        elif key == "ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            validate[key] = True
        elif key == "pid" and len(value)==9 and value.isnumeric():
            validate[key] = True

    if validate["byr"] and validate["iyr"] and validate["eyr"] and validate["hgt"] and validate["hcl"] and validate["ecl"] and validate["pid"]:
            validPassports+=1

print("Valid passports (part 2):", validPassports)
    
    
