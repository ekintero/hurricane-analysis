# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
updated_damages = []
def updateDamage(damages):
  conversion = {"M": 1000000, "B": 1000000000}
  for element in damages:
    if element[-1] == "M":
      updated_damages.append(float(element[:-1])*conversion["M"])
    elif element[-1] == "B":
      updated_damages.append(float(element[:-1])*conversion["B"])
    else:
      updated_damages.append("Damages not recorded")
  return updated_damages

updateDamage(damages)

# write your construct hurricane dictionary function here:
hurricaneDictionary = {}
def create_dictionary():
  for index in range(len(names)):
   hurricaneDictionary[names[index]]={"Name": names[index],
                                      "Month": months[index],
                                      "Year": years[index],
                                      "Max Sustained Wind": max_sustained_winds[index],
                                      "Areas Affected": areas_affected[index],
                                      "Damage": updated_damages[index],
                                      "Deaths": deaths[index]}
  
create_dictionary()
#print(hurricaneDictionary["Hugo"])

# write your construct hurricane by year dictionary function here:
def hurricane_year(year):
  hurricane_year = []
  for key in hurricaneDictionary:
    if hurricaneDictionary[key]["Year"]==year:
      hurricane_year.append(hurricaneDictionary[key])
  return hurricane_year


# write your count affected areas function here:
def hurricane_areas_afected():
  count_areas_afected = {}
  for key in hurricaneDictionary:
    for area in hurricaneDictionary[key]["Areas Affected"]:
      if area in count_areas_afected:
        count += 1
        count_areas_afected[area] = count
      else:
        count = 1
        count_areas_afected[area] = count
  return count_areas_afected

#print(hurricane_areas_afected())
# write your find most affected area function here:
def dangeroust_hurricane():
  hurricane_most_deaths = 'Cuba I'
  number_deaths = 0
  for key in hurricaneDictionary:
    if hurricaneDictionary[key]["Deaths"] > number_deaths:
      number_deaths = hurricaneDictionary[key]["Deaths"]
      hurricane_most_deaths = hurricaneDictionary[key]["Name"]
  return number_deaths, hurricane_most_deaths

print(dangeroust_hurricane())
# write your greatest number of deaths function here:


# write your catgeorize by mortality function here:
def hurricanes_by_mortality():
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  for key in hurricaneDictionary:
    if hurricaneDictionary[key]["Deaths"] == mortality_scale[0]:
      hurricanes_by_mortality[0].append(key)
    elif hurricaneDictionary[key]["Deaths"] <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(key)
    elif hurricaneDictionary[key]["Deaths"] <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(key)
    elif hurricaneDictionary[key]["Deaths"] <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(key)
    elif hurricaneDictionary[key]["Deaths"] <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(key)
    else: 
      hurricanes_by_mortality[5].append(key)
  return hurricanes_by_mortality

print(hurricanes_by_mortality())
print
# write your greatest damage function here:
def damage_hurricane():
  hurricane_damage = 0
  max_damage = 0.0
  for key in hurricaneDictionary:
    if hurricaneDictionary[key]["Damage"] == "Damages not recorded":
      continue
    else:
      if hurricaneDictionary[key]["Damage"] >max_damage:
          max_damage = hurricaneDictionary[key]["Damage"]
          hurricane_damage = hurricaneDictionary[key]["Name"]
  return max_damage, hurricane_damage

print(damage_hurricane())



# write your catgeorize by damage function here:

def hurricanes_by_damage():
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  for key in hurricaneDictionary:

    if hurricaneDictionary[key]["Damage"] == "Damages not recorded":
      continue
    elif hurricaneDictionary[key]["Damage"] < damage_scale[1]:
      hurricanes_by_damage[0].append(key)
    elif damage_scale[1] >= hurricaneDictionary[key]["Damage"]  < damage_scale[2]:
      hurricanes_by_damage[1].append(key)
    elif damage_scale[2] >= hurricaneDictionary[key]["Damage"]  < damage_scale[3]:
      hurricanes_by_damage[2].append(key)
    elif damage_scale[4] >= hurricaneDictionary[key]["Damage"]  < damage_scale[4]:
      hurricanes_by_damage[3].append(key)
    elif hurricaneDictionary[key]["Deaths"] >= damage_scale[4]:
      hurricanes_by_damage[4].append(key)
   
  return hurricanes_by_damage
  print(hurricanes_by_damage())

