import re

class Field_Validator:
    def __init__(self, profile_dict):
        self.keys = []
        self.profile_dict = profile_dict
        self.profile_valid = False

        if 'byr' in profile_dict:
            self.birth_year = profile_dict['byr']
            self.keys.append('byr')
        if 'iyr' in profile_dict:
            self.issue_year = profile_dict['iyr'] 
            self.keys.append('iyr')
        if 'eyr' in profile_dict:
            self.expiration_year = profile_dict['eyr'] 
            self.keys.append('eyr')
        if 'hgt' in profile_dict:
            self.height =  profile_dict['hgt'] 
            self.keys.append('hgt')
        if 'hcl' in profile_dict:
            self.hair_colour = profile_dict['hcl'] 
            self.keys.append('hcl')
        if 'ecl' in profile_dict:
            self.eye_colour = profile_dict['ecl'] 
            self.keys.append('ecl')
        if 'pid' in profile_dict:
            self.passport_id = profile_dict['pid']
            self.keys.append('pid')
    
    def check_validity(self):
        for key in self.keys:
            print(self.profile_dict[key])
            if key == 'byr':
                if not 1920 < int(self.profile_dict['byr']) < 2002:
                    self.profile_valid = False
            if key == 'iyr':
                if not 2010 < int(self.profile_dict['iyr']) < 2020:
                    self.profile_valid = False
            if key == 'eyr':
                if not 2020 < int(self.profile_dict['iyr']) < 2030:
                    self.profile_valid = False
            if key == 'hgt':
                x = re.findall("(cm)|(in)$" , str(self.profile_dict['hgt']))
                height = re.findall("\d+", self.profile_dict['hgt'])[0]
                if 'cm' in x[0]:
                    if not 150 < int(height) < 193:
                        self.profile_valid = False
                if 'in' in x[0]:
                    if not 59 < int(height) < 76:
                        self.profile_valid = False
            if key == 'hcl':
                x = re.findall("[r'\A#'][r'\d']r'{6}'", self.profile_dict['hcl'])
                print(x)






            



        

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
        profile.pop('cid') #this changes the original!
        cleaned_minus_cid.append(profile)
    else:
        cleaned_minus_cid.append(profile)

for profile in cleaned_minus_cid:
    if (set(profile.keys()) == fullset_minus_cid):
        num_of_valid_passports += 1

print(num_of_valid_passports)


# print(cleaned[0])

validations = Field_Validator(cleaned[4])

# print(validations.hair_colour)

validations.check_validity()






