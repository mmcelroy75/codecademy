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

# write your update damages function here:
def update_damages(lst):
  updated_damages = []
  conversion = {"M": 1000000,
              "B": 1000000000}
  for item in lst:
    if item == 'Damages not recorded':
      updated_damages.append(item)
    else:
      new_item = conversion[item[-1]] * float(item[:-1])
      updated_damages.append(new_item)

  return updated_damages


# write your construct hurricane dictionary function here:

def hurricane_dict():
  hurricane_dict = {}
  updated_damages = update_damages(damages)
  for i in range(len(names)):
    hurricane_dict[names[i]] = {"Name": names[i],
 "Month": months[i],
 "Year": years[i],
 "Max Sustained Wind": max_sustained_winds[i],
 "Areas Affected": areas_affected[i],
 "Damage": updated_damages[i],
 "Deaths": deaths[i]}

  return hurricane_dict

# write your construct hurricane by year dictionary function here:
def hurricane_dict_year():
  new_cane_dict = {}
  for value in hurricane_dict().values():
    current_year = value['Year']
    current_cane = value
    if current_year not in new_cane_dict.keys():
      new_cane_dict[current_year] = [current_cane]
    else:
      new_cane_dict[current_year].append(current_cane)

  return new_cane_dict

# write your count affected areas function here:
def count_areas():
  count_dict = {}
  for value in hurricane_dict().values():
    for i in value['Areas Affected']:
      new_key = i
      if new_key not in count_dict.keys():
        count_dict[new_key] = 1
      else:
        count_dict[new_key] += 1

  return count_dict

# write your find most affected area function here:
def most_affected():
  affected_areas = count_areas()
  most_affected = {}
  max_affect = max(affected_areas, key=lambda key: affected_areas[key])
  most_affected[max_affect] = []
  for value in hurricane_dict().values():
    if max_affect in value['Areas Affected']:
      most_affected[max_affect].append(value['Year'])

  return most_affected

# write your greatest number of deaths function here:
def most_deaths():
  most_deaths = {}
  for key, value in hurricane_dict().items():
    most_deaths[key] = value['Deaths']
  max_death = max(most_deaths, key=lambda key: most_deaths[key])

  return most_deaths #max_death + ": " + str(most_deaths.get(max_death))

    
# write your catgeorize by mortality function here:
def mortality(): #This one written from misreading directions.
  mortality_dict = {}
  mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
  for key, value in most_deaths().items():
    if value > mortality_scale[0] and value <= mortality_scale[1]:
      mortality_dict[key] = 1
    elif value > mortality_scale[1] and value <= mortality_scale[2]:
      mortality_dict[key] = 2
    elif value > mortality_scale[2] and value <= mortality_scale[3]:
      mortality_dict[key] = 3
    elif value > mortality_scale[3] and value <= mortality_scale[4]:
      mortality_dict[key] = 4
    else:
      mortality_dict[key] = 5
    
  return mortality_dict

def mortality_two():
  mortality_dict = {1: [], 2: [], 3: [], 4: [], 5: []}
  mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
  for value in hurricane_dict().values():
    if value['Deaths'] > mortality_scale[0] and value['Deaths'] <= mortality_scale[1]:
      mortality_dict[1].append(value)
    elif value['Deaths'] > mortality_scale[1] and value['Deaths'] <= mortality_scale[2]:
      mortality_dict[2].append(value)
    elif value['Deaths'] > mortality_scale[2] and value['Deaths'] <= mortality_scale[3]:
      mortality_dict[3].append(value)
    elif value['Deaths'] > mortality_scale[3] and value['Deaths'] <= mortality_scale[4]:
      mortality_dict[4].append(value)
    else:
      mortality_dict[5].append(value)
  
  return mortality_dict

# write your greatest damage function here:
def most_damage():
  most_damage = {}
  for key, value in hurricane_dict().items():
    if value['Damage'] == 'Damages not recorded':
      most_damage[key] = 0
    else:
      most_damage[key] = value['Damage']
  max_damage = max(most_damage, key=lambda key: most_damage[key])

  return max_damage + ": " + str(most_damage.get(max_damage))

# write your catgeorize by damage function here:
def damage_scale():
  damage_dict = {'Not Recorded': [], 1: [], 2: [], 3: [], 4: [], 5: []}
  damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
  for value in hurricane_dict().values():
    if value['Damage'] == 'Damages not recorded':
      damage_dict['Not Recorded'].append(value)
    elif value['Damage'] > damage_scale[0] and value['Damage'] <= damage_scale[1]:
      damage_dict[1].append(value)
    elif value['Damage'] > damage_scale[1] and value['Damage'] <= damage_scale[2]:
      damage_dict[2].append(value)
    elif value['Damage'] > damage_scale[2] and value['Damage'] <= damage_scale[3]:
      damage_dict[3].append(value)
    elif value['Damage'] > damage_scale[3] and value['Damage'] <= damage_scale[4]:
      damage_dict[4].append(value)
    else:
      damage_dict[5].append(value)

  return damage_dict