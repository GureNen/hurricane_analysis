# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# update damages function :

def update_damages(damages_lst):
    updated_damages_lst = []
    for damage in damages_lst:
        if damage[-1] == "M":
            updated_damage = float(damage[:-1]) * 1000000
        elif damage[-1] == "B":
            updated_damage = float(damage[:-1]) * 1000000000
        else:
            updated_damage = damage
        updated_damages_lst.append(updated_damage)
    return updated_damages_lst

updated_damages = update_damages(damages)
print(updated_damages)

# construct hurricane dictionary function :

def hurricane_dict_constructor(name, month, year, max_sustained_wind, area_affected, damage, death):
    hurricane_dict = {}
    length = len(names)
    for i in range(length):
        hurricane_dict[name[i]] = {"Name": name[i], "Month": month[i], "Year": year[i], "Max Sustained Wind": max_sustained_wind[i], "Areas Affected": area_affected[i], "Damage": damage[i], "Deaths": death[i]}
    return hurricane_dict

hurricane_dataset = hurricane_dict_constructor(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricane_dataset)

# construct hurricane by year dictionary function :

def hurricane_converter(hurricane_dict):
    new_hurricane = {}
    for value in hurricane_dict.values():
        key = value["Year"]
        try:
            new_hurricane[key].append(value)
        except KeyError:
            new_hurricane[key] = [value]
    return new_hurricane

converted_hurricane = hurricane_converter(hurricane_dataset)
print(converted_hurricane)


# count affected areas function :

def areas_counter(hurricane_dict):
    areas_count_dict = {}
    for value in hurricane_dict.values():
        for area in value.get("Areas Affected"):
            try:
                areas_count_dict[area] += 1
            except KeyError:
                areas_count_dict[area] = 1
    return areas_count_dict

areas_count = areas_counter(hurricane_dataset)
print(areas_count)


# find most affected area function :

def most_affected_area(areas_dict):
    max_hit = 0
    target_area = None
    for area in areas_dict:
        if areas_dict[area] > max_hit:
            max_hit = areas_dict[area]
            target_area = area
    print("The area that is affected by hurricanes the most is {area} with a total hit count of {hit_count}.".format(area = target_area, hit_count = max_hit))

most_affected_area(areas_count)

# greatest number of deaths function :

def greatest_number_of_deaths(hurricane_dict):
    max_deaths = 0
    hurricane = None
    for value in hurricane_dict.values():
        if value["Deaths"] > max_deaths:
            max_deaths = value["Deaths"]
            hurricane = value["Name"]
    print("The hurricane that caused the greatest number of deaths is {hurricane} with a number of {number_of_deaths}.".format(hurricane = hurricane, number_of_deaths = max_deaths))

greatest_number_of_deaths(hurricane_dataset)

# catgeorize by mortality function :

def hurricane_death_categorizer(hurricane_dict):
    death_category_dict = {key: value for key, value in [(0, []), (1, []), (2, []), (3, []), (4, []), (5, [])]}
    for value in hurricane_dict.values():
        deaths = value["Deaths"]
        name = value["Name"]
        if deaths == 0:
            death_category_dict[0].append(name)
        elif deaths <= 100:
            death_category_dict[1].append(name)
        elif deaths <= 500:
            death_category_dict[2].append(name)
        elif deaths <= 1000:
            death_category_dict[3].append(name)
        elif deaths <= 10000:
            death_category_dict[4].append(name)
        else:
            death_category_dict[5].append(name)
    return death_category_dict

hurricane_death_category = hurricane_death_categorizer(hurricane_dataset)
print(hurricane_death_category)

# greatest damage function :

def greatest_damage(hurricane_dict):
    max_dmg = 0
    hurricane = None
    for value in hurricane_dict.values():
        if value["Damage"] != "Damages not recorded" and value["Damage"] > max_dmg:
            max_dmg = value["Damage"]
            hurricane = value["Name"]
    print("The hurricane that caused the greatest damage is {hurricane} with a cost of {cost}".format(hurricane = hurricane, cost = max_dmg))

greatest_damage(hurricane_dataset)

# catgeorize by damage function :

def hurricane_damage_categorizer(hurricane_dict):
    damage_category_dict = {key: value for key, value in [(0, []), (1, []), (2, []), (3, []), (4, []), (5, [])]}
    for value in hurricane_dict.values():
        damage = value["Damage"]
        name = value["Name"]
        if damage == "Damages not recorded":
            continue
        if damage == 0:
            damage_category_dict[0].append(name)
        elif damage <= 100000000:
            damage_category_dict[1].append(name)
        elif damage <= 1000000000:
            damage_category_dict[2].append(name)
        elif damage <= 10000000000:
            damage_category_dict[3].append(name)
        elif damage <= 50000000000:
            damage_category_dict[4].append(name)
        else:
            damage_category_dict[5].append(name)
    return damage_category_dict

hurricane_damage_category = hurricane_damage_categorizer(hurricane_dataset)
print(hurricane_damage_category)