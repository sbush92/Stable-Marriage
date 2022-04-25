import time
import random
# male_pref = [["A" ,["D", "E", "F","G"]], ["B", ["G","E", "F"]], ["C", ["F", "D", "E","G"]]]
# female_pref = [["D", ["B", "C"]], ["E", ["A"]], ["F", ["C", "B"]], ["G",["A","B","C"]]]
male_pref = []
female_pref = []
for x in range(34, 126):
    if(x <= 79):   
        newPref = list(random.sample(range(80,127), 20))
        #print(newPref)
        random.shuffle(newPref)
        for y in range(20):
            newPref[y] = chr(newPref[y])
        #print(newPref)
        #print(chr(x))
        male_pref.append([chr(x), newPref])
    else:
        newPref = list(random.sample(range(34,80), 20))
        random.shuffle(newPref)
        for y in range(20):
            newPref[y] = chr(newPref[y])
        #print(newPref)
        #print(chr(x))
        female_pref.append([chr(x), newPref])
#print(len(male_pref))
#print(len(female_pref))

print("Male list before", male_pref)
print("Female list before", female_pref)
start = time.perf_counter()
#loop through Males
for i in range(len(male_pref)):
    # Create new preference list for male and female
    pref_male = []
    
    # Female list is accumulative for each male
    pref_female = [] 
    
    # loop through female in order of preference for male
    for j in range(len(male_pref[i][1])):

        # Check if Male is in Female's preference list
        for k in range(len(female_pref[j][1])):
            if(female_pref[j][1][k] == male_pref[i][0]):
                pref_male.append(female_pref[j][0])
        
            # Add all Famale's preferences to accumulative preference list 
            duplicate = False
            for l in range(len(pref_female)):
                if(pref_female[l] == female_pref[j][1][k]):
                    duplicate = True
            # Check for duplicates in pref_female
            if(duplicate == False):

                    pref_female.append(female_pref[j][1][k])

                # compare list lengths
            # If male pref is greater than accumulated female pref list then break
            if(len(pref_male) >= len(pref_female)):
                break
    
            #print("Female length", len(pref_female), "Male length", len(pref_male))
          
    # Reduce Male Preference 
    male_pref[i][1] = pref_male

#check if females still in male preference
keep = []
for i in range(len(male_pref)):
    #compile list of female in male pref list
    for j in range(len(male_pref[i][1])):
        for l in range(len(female_pref)):
            if(male_pref[i][1][j] != female_pref[l][0]):
                keep.append(male_pref[i][1][j])
#compare and delete female not in list      
#print(keep)          
deleted = []
for i in range(len(female_pref)):
    delete = True
    for j in range(len(keep)):
        if(keep[j] == female_pref[i][0]):
            delete = False
    if(delete == True):
        deleted.append(female_pref[i][0])

#reduce Female list       
for i in range(len(deleted)):
    for j in range(len(female_pref)):
        if(female_pref[j][0] == deleted[i]):
            female_pref.remove(female_pref[j])
            break
#reduce Male List
tempList = []
for i in range(len(male_pref)):
    if(len(male_pref[i][1]) > 0):
        tempList.append(male_pref[i])

male_pref = tempList
end = time.perf_counter()

print("Deleted", deleted)
print("Time elapsed ", end - start)
#Proceed to match pairs
print("Male list after FPT", male_pref)
print("Female list after FPT", female_pref)

print(len(male_pref))
print(len(female_pref))
