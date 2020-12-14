
# read the input file
with open("input") as file:
    raw = file.read()

# convert the big string into a list separated by one full empty line
cleaned = raw.split('\n\n')

# separate each field into its own list item
for index, profile in enumerate(cleaned):
    cleaned[index] = profile.split()

# convert the fields into key:value pairs
for index, profile in enumerate(cleaned):
    cleaned[index] = {profile[i].split(':')[0] : profile[i].split(':')[1]  for i in range(0, len(profile))}


# check against these keys
fullset = set(['byr','iyr', 'eyr' , 'hgt', 'hcl', 'ecl', 'pid','cid'])
fullset_minus_cid = set(['byr','iyr', 'eyr' , 'hgt', 'hcl', 'ecl', 'pid'])

cleaned_minus_cid = []
num_of_valid_passports = 0
for profile in cleaned:
    if 'cid' in profile:
        profile.pop('cid')
        cleaned_minus_cid.append(profile)
    else:
        cleaned_minus_cid.append(profile)

for profile in cleaned_minus_cid:
    if (set(profile.keys()) == fullset_minus_cid):
        num_of_valid_passports += 1

print(num_of_valid_passports)










