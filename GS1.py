import time
import random
#male_pref = [["A" ,["G", "E", "F","H"], "", 0], ["B", ["G", "F", "E","H"], "", 0], ["C", ["G", "F", "E","H"], "", 0], ["D", ["H", "F", "E", "G"], "", 0]]
#female_pref = [["E", ["A", "C", "B","D"], ""], ["F", ["C", "B", "A","D"], ""],["H", ["C", "B", "A","D"], ""],["G", ["A", "B", "C","D"], ""]]
#male_pref = [[1 ,[7, 5, 6, 8], "", 0], [2, [7, 6, 5, 8], "", 0], [3, [7, 6, 5, 8], "", 0], [4, [8, 6, 5, 7], "", 0]]
#female_pref = [[5, [1, 3, 2, 4], ""], [6, [3, 2, 1, 4], ""],[7, [3, 2, 1, 4], ""],[8, [1, 2, 3, 4], ""]]
male_pref = []
female_pref = []
for x in range(34, 126):
    if(x <= 79):   
        newPref = list(range(80,127))
        #print(newPref)
        random.shuffle(newPref)
        for y in range(46):
            newPref[y] = chr(newPref[y])
        #print(newPref)
        #print(chr(x))
        male_pref.append([chr(x), newPref, "", 0])
    else:
        newPref = list(range(34,80))
        random.shuffle(newPref)
        for y in range(46):
            newPref[y] = chr(newPref[y])
        #print(newPref)
        #print(chr(x))
        female_pref.append([chr(x), newPref, ""])
print(len(male_pref))
print(len(female_pref))

start = time.perf_counter()
# Each unpaired item in list A asks to pair with their top preferredchoice in list
for i in range(len(male_pref)):
    for n in range(len(male_pref)):
        male_pref[n][3] = 0
    # Repeat until all paired
    for j in range(len(male_pref)):
        #print(male_pref[j][1][i]) #The preference of A
        # Unpaired items in List A ask to pair with their next preferred choicein list
        if(male_pref[j][2] == ""): 
            #print(male_pref[j][0], "Male Looking", male_pref[j][1][male_pref[j][3]+i],  "pref Level", male_pref[j][3] + i)
            for k in range(len(female_pref)): 
                if(male_pref[j][1][male_pref[j][3]+i] == female_pref[k][0]):
                    if(female_pref[k][2] == ""):
                        female_pref[k][2] = male_pref[j][0]
                        male_pref[j][2] = female_pref[k][0]
                        #print("match", male_pref[j][0], "with", male_pref[j][1][male_pref[j][3]+i])
                    # Items in list B accept pair and decline all other pairs that are lowerthan on Item B’s preferential list than the pair that item B is alreadypaired to.
                    else:
                        # If female is currently matched
                        current = None
                        prospective = None
                        # Check the female's preferences to see if the current proposal is preferable to the currently matched
                        for l in range(len(female_pref[k][1])):
                            if(female_pref[k][1][l] == male_pref[j][0]):
                                prospective = l
                            if(female_pref[k][1][l] == female_pref[k][2]):
                                current = l
                            if(current != None and prospective != None):
                                # If prospective is greater than current
                                if(prospective < current):
                                    #print("Female",female_pref[k][0], "prospective", male_pref[j][0], "Current", female_pref[k][2])
                                    #unmatch Male in 
                                    for m in range(len(male_pref)): 
                                        if(male_pref[m][0] == female_pref[k][2]):
                                            male_pref[m][2] = ""
                                            male_pref[m][3] = male_pref[m][3] + 1
                                            #print(male_pref[m][0]," is now unpaired pref now", male_pref[m][3] )
                                     
                                    female_pref[k][2] = male_pref[j][0]
                                    male_pref[j][2] = female_pref[k][0]
                                    
                                    #print("match", female_pref[k][2], "with",  male_pref[j][2])
                                    #print( female_pref[k][2], male_pref[j][2])
                                    break
        if(male_pref[j][2] == ""):
            male_pref[j][3] = male_pref[j][3] + 1

end = time.perf_counter()
print("Time elapsed ", end - start)
for i in range(len(male_pref)):
    print("Male", male_pref[i][0], "Matched with Female", male_pref[i][2])