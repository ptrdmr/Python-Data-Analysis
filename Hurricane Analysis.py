#!/usr/bin/env python
# coding: utf-8

# In[28]:


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

# 1
# Update Recorded Damages
print("'Damage totals before formating'")
print(damages)
conversion = {"M": 1000000,
              "B": 1000000000}

def damages_1(damages):
  new_damages =[]
  # conversion = {"M": 1000000, "B": 1000000000}
  for i in damages:
    if 'B' in i:
      i = i.strip("B")
      i = float(i)
      i = i * conversion.get("B")
      new_damages.append(i)
    elif 'M' in i:
      i = i.strip("M")
      i = float(i)
      i = i * conversion.get("M")
      new_damages.append(i)
    else:
      new_damages.append(i)
  return new_damages
# test function by updating damages
damages = damages_1(damages)
print("")
print("'Damage totals after formatting'")
print(damages)


# In[29]:


# 2 
# Create a Table
dict_hurricane = {}
def hurr_table_generator(names,months, years, max_sustained_winds, areas_affected, damages, deaths):
  #this for loop will start by using the length of names as our unit of measurement for the coming table records. It will iterate us forward in the records.
  for i in range(len(names)):
  #this makes names our key value, moved foward by i. It also establishes the frame work for a single hurricane record.
    dict_hurricane[names[i]] = {"Name": names[i],"Month":months[i], "Year":years[i], "Max Sust. Wind": max_sustained_winds[i], "Affected Areas": areas_affected[i], "Cost of Damage(USD)": damages[i], "Deaths": deaths[i]}
  return dict_hurricane

#Create and view the hurricanes dictionary
hurricanes_by_name = {}
hurricanes_by_name.update(hurr_table_generator(names,months, years, max_sustained_winds, areas_affected, damages, deaths))
print("")
print("'DICTIONARY: HURRICANES BY NAME'")
#to see each hurricane, add a [] with the name of the hurricane inside the print statement below.
print(hurricanes_by_name)
print("")


# In[30]:



# 3
# Organizing by Year
def create_year_dictionary(hurricanes_by_name):
    """Convert dictionary with hurricane name as key to a new dictionary with hurricane year as the key and return new dictionary."""
    
    hurricanes_by_year = dict()
    for cane in hurricanes_by_name:
        current_year = hurricanes_by_name[cane]['Year']
        current_cane = hurricanes_by_name[cane]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_cane]
        else:
            hurricanes_by_year[current_year].append(current_cane)
    return hurricanes_by_year
    
# create a new dictionary of hurricanes with year and key
hurricanes_by_year = create_year_dictionary(hurricanes_by_name)
print("'DICTIONARY: HURRICANES BY YEAR'")
#to see each hurricane, add a [] with a year of the hurricane inside the print statement below.
print(hurricanes_by_year)
print("")



# In[32]:


# 4
# Counting Damaged Areas
def count_affected_areas(hurricanes_by_name):
    """Find the count of affected areas across all hurricanes and return as a dictionary with the affected areas as keys."""
    affected_areas_count = dict()
    for cane in hurricanes_by_name:
        for area in hurricanes_by_name[cane]['Affected Areas']:
            if area not in affected_areas_count:
                affected_areas_count[area] = 1
            else:
                affected_areas_count[area] += 1
    return affected_areas_count

# create dictionary of areas to store the number of hurricanes involved in
affected_areas_count = count_affected_areas(hurricanes_by_name)
print("'DICTIONARY: AFFECTED AREAS & THEIR COUNTS'")
print(affected_areas_count)


# In[33]:




# 5 
# Calculating Maximum Hurricane Count
def most_affected_area(affected_areas_count):
  max_area_count = 0
  max_area = 'Central America'
  for a in affected_areas_count:
    if affected_areas_count[a]> max_area_count:
      max_area = a
      max_area_count = affected_areas_count[a]
    return max_area, max_area_count 

# find most frequently affected area and the number of hurricanes involved in
print(" ")
l,m = most_affected_area(affected_areas_count)
print("'Area most affected by hurricanes and it's count")
print(l,m)




# In[34]:


# 6
# Calculating the Deadliest Hurricane
def max_mortality(hurricanes_by_name):
  max_mortality_cane = 'Cuba I'
  max_mortality = 0
  for death in hurricanes_by_name:
    if hurricanes_by_name[death]['Deaths']> max_mortality:
      max_mortality_cane = death
      max_mortality = hurricanes_by_name[death]['Deaths']
  return max_mortality_cane,max_mortality

# find highest mortality hurricane and the number of deaths
print("")
max_mortality_cane, max_mortality = max_mortality(hurricanes_by_name)
print("Hurricane that killed the most people, and how many.")
print(max_mortality_cane, max_mortality)




# In[ ]:


# 7
# Rating Hurricanes by Mortality

def hurricanes_mortality_ranker(hurricanes_by_name):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for mort in hurricanes_by_name:
    num_deaths = hurricanes_by_name[mort]['Deaths']
    if num_deaths == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricanes_by_name[mort])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricanes_by_name[mort])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricanes_by_name[mort])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricanes_by_name[mort])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricanes_by_name[mort])
    elif num_deaths > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricanes_by_name[mort])
  return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = hurricanes_mortality_ranker(hurricanes_by_name)
print("")
print("'DICTIONARY: HURRICANES RANKED 0-5 BASED ON THEIR DEATH TOLLS'")
#to see each rank, add a [] with the number 0-5 inside the print statement below.
print(hurricanes_by_mortality)





# In[36]:


# 8 Calculating Hurricane Maximum Damage
def highest_damages(hurricanes_by_name):
  max_cost_cane = 'Cuba I'
  max_cost = 0
  for cost in hurricanes_by_name:
    if hurricanes_by_name[cost]['Cost of Damage(USD)'] == 'Damages not recorded':
      pass
    elif hurricanes_by_name[cost]['Cost of Damage(USD)'] > max_cost:
      max_cost_cane = cost
      max_cost = hurricanes_by_name[cost]['Cost of Damage(USD)']
  return max_cost_cane,max_cost
# find highest damage inducing hurricane and its total cost
print("")
max_cost_cane, max_cost = highest_damages(hurricanes_by_name)
print("'Hurricane that caused the most damage, and it's total in USD")
print(max_cost_cane, max_cost)
print("")


# In[31]:


# 9
# Rating Hurricanes by Damage
#
def catagorize_by_damage(hurricanes_by_name):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for damage in hurricanes_by_name:
    damage_total = hurricanes_by_name[damage]['Deaths']
    if damage_total == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes_by_name[damage])
    elif damage_total > damage_scale[0] and damage_total <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes_by_name[damage])
    elif damage_total > damage_scale[1] and damage_total <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes_by_name[damage])
    elif damage_total > damage_scale[2] and damage_total <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes_by_name[damage])
    elif damage_total > damage_scale[3] and damage_total <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes_by_name[damage])
    elif damage_total > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricanes_by_name[damage])
  return hurricanes_by_mortality
  
# categorize hurricanes in new dictionary with damage severity as key
hurricanes_by_damages = catagorize_by_damage(hurricanes_by_name)
print("'DICTIONARY: HURRICANES RANKED 0-5 BASED ON COST OF DAMAGE IN USD'")
#to see each rank, add a [] with the number 0-5 inside the print statement below.
print(hurricanes_by_damages)

