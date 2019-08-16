import numpy as np
import pandas as pd
import datetime

# Read Excle File:

df = pd.read_excel (r'C:\Users\Aws Al-Shedayfat\Desktop\CODES\Python\Challange\data.xlsx')


# Read & count the Number of violations for each catagory 
Biohazards1 = df[df.violation_category=='Biohazards'].violation_date.count()
Air_P1 = df[df.violation_category=='Air Pollutants and Odors'].violation_date.count()
Animal1 = df[df.violation_category=='Animals and Pests'].violation_date.count()
Building1 = df[df.violation_category=='Building Conditions'].violation_date.count()
Chemimical1 = df[df.violation_category=='Chemical Hazards'].violation_date.count()
Garbage1 = df[df.violation_category=='Garbage and Refuse'].violation_date.count()
Retail1 = df[df.violation_category=='Retail Food'].violation_date.count()
Unsantary1 = df[df.violation_category=='Unsanitary Conditions'].violation_date.count()
Vegetation1 = df[df.violation_category=='Vegetation'].violation_date.count()

# Read & Find the most recent Date of violations for each catagory 
Biohazards = df[df.violation_category=='Biohazards'].violation_date.max()
Air_P = df[df.violation_category=='Air Pollutants and Odors'].violation_date.max()
Animal = df[df.violation_category=='Animals and Pests'].violation_date.max()
Building = df[df.violation_category=='Building Conditions'].violation_date.max()
Chemimical = df[df.violation_category=='Chemical Hazards'].violation_date.max()
Garbage = df[df.violation_category=='Garbage and Refuse'].violation_date.max()
Retail = df[df.violation_category=='Retail Food'].violation_date.max()
Unsantary = df[df.violation_category=='Unsanitary Conditions'].violation_date.max()
Vegetation = df[df.violation_category=='Vegetation'].violation_date.max()

a = "Most Recent Violation in the catagory of: "
b =  "The Number of violations for the catagory of: "

print(a, "Biohazards",Biohazards)
print(a, "Air Pollutants and Odors", Air_P)
print(a, "Animals and Pests " , Animal)
print(a, "Building Conditions ", Building)
print(a, "Chemical Hazards ", Chemimical)
print(a, "Garbage and Refuse ", Garbage)
print(a, "Retail Food " , Retail)
print(a, "Unsanitary Conditions " , Unsantary)
print(a, "Vegetation" , Vegetation)
print("\n")
print(b, "Biohazards",Biohazards1)
print(b, "Air Pollutants and Odors", Air_P1)
print(b, "Animals and Pests " , Animal1)
print(b, "Building Conditions ", Building1)
print(b, "Chemical Hazards ", Chemimical1)
print(b, "Garbage and Refuse ", Garbage1)
print(b, "Retail Food " , Retail1)
print(b, "Unsanitary Conditions " , Unsantary1)
print(b, "Vegetation" , Vegetation1)



#under here is a code to see the number of unclosed violation
#roupby_count1 = df.groupby(['violation_category']).count()
# print ('Count of values, grouped by the violation type:' +  str(groupby_count1))