#Author: Kendrick Gholston, Mekaila Quarshie, and Tiara Williams
#Program Description: Assignment 5
#FileName: Assignment 5.py
#Date: 11/5/15

def getPopAge14(): #Finds the total population in age group 0-14
    myfile= open("WorldCensusAges0-14.csv")
    pop=[] #Empty list to store the total poplation of this age group for each country. Note total will be in the same order as countries so they will be paired correctly if both the name and population is called
    for line in myfile: #Goes through each line ine the file
        fields=line.split(",") #Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        sum1=int(fields[1]) + int(fields[2]) #Since the populations for male and female are string in this age group, you must convert them into integers and combined for the total population
        pop.append(sum1) #Each total will be added to the empty list
    return pop #The list is stored in the function

def getPopAge15():#Finds the total population in age group 15-64
    myfile2= open("WorldCensusAges15-64.csv")
    pop2=[]#Empty list to store the total poplation of this age group for each country. Note total will be in the same order as countries so they will be paired correctly if both the name and population is called
    for line2 in myfile2:#Goes through each line ine the file
        fields2=line2.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        sum2=int(fields2[1]) + int(fields2[2])#Since the populations for male and female are string in this age group, you must convert them into integers and combined for the total population
        pop2.append(sum2)#Each total will be added to the empty list
    return pop2#The list is stored in the function

def getPopAge64():#Finds the total population in age group 64+
    myfile3= open("WorldCensusAges64+.csv")
    pop3=[]#Empty list to store the total poplation of this age group for each country. Note total will be in the same order as countries so they will be paired correctly if both the name and population is called
    for line3 in myfile3:#Goes through each line ine the file
        fields3=line3.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        sum3=int(fields3[1]) + int(fields3[2])#Since the populations for male and female are string in this age group, you must convert them into integers and combined for the total population
        pop3.append(sum3)#Each total will be added to the empty list
    return pop3#The list is stored in the function
def Printcountryandtotal():#Option 4, Prints out each country and their total population
    myfile4=open("WorldCensusAges0-14.csv")
    names=[]#Empty list to store the names of each country. Note they will remain in the sam order as in the original file
    for line4 in myfile4:#Goes through each line ine the file
        fields4=line4.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        names.append(fields4[0])#Each country name is added to the empty list
    result=getPopAge14() #The list of total populations from getPopAge14 function is stored here
    result2=getPopAge15()#The list of total populations from getPopAge15 function is stored here
    result3=getPopAge64()#The list of total populations from getPopAge64 function is stored here
    lower=0
    upper=20
    print("Country".ljust(50), "Total Population") #1.just(50) provides beteween the two strings
    starter=""
    while starter != "q":#Loop that allows the user to 20 outputs at a time or quit the program
        for i in range(lower,upper):
            print(names[i].ljust(50), result[i]+result2[i]+result3[i]) #Each country will be printed as well as their total population. The varaible will be increase by 1 and will be able to go throug each index o in country names list and getting the combined total from the 3 population lists
        if lower==220 and upper==228:
            break    
        if upper==220 and lower==200:
            lower=220
            upper=228
        else:    
            upper+=20
            lower+=20
        starter=input("Press enter to continue or enter q to quit: ")#Gives the user the chance to quit the option or keep looking at the outputs
                     
            
def getRatioPop14():#Finds the Male-to-Female Ratio for each country in age group 0-14
    myfile5=open("WorldCensusAges0-14.csv")
    ratio=[]#Empty list to store the Male-to-Female Ratio of this age group for each country. Note the ratio will be in the same order as countries so they will be paired correctly if both the name and ratio is called
    for line5 in myfile5:#Goes through each line ine the file
        fields5=line5.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        quot1=int(fields5[1]) / int(fields5[2])#Since the populations for male and female are strings in this age group, you must convert them into integers and divide the male population by the female population to get the ratio
        ratio.append(quot1)#Each ratio is added to the empty list
    return ratio#The list is stored in the function
def getRatioPop15():#Finds the Male-to-Female Ratio for each country in age group 15-64
    myfile6=open("WorldCensusAges15-64.csv")
    ratio2=[]#Empty list to store the Male-to-Female Ratio of this age group for each country. Note the ratio will be in the same order as countries so they will be paired correctly if both the name and ratio is called
    for line6 in myfile6:#Goes through each line ine the file
        fields6=line6.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        quot2=int(fields6[1]) / int(fields6[2])#Since the populations for male and female are strings in this age group, you must convert them into integers and divide the male population by the female population to get the ratio
        ratio2.append(quot2)#Each ratio is added to the empty list
    return ratio2#The list is stored in the function
def getRatioPop64():#Finds the Male-to-Female Ratio for each country in age group 64+
    myfile7=open("WorldCensusAges64+.csv")
    ratio3=[]#Empty list to store the Male-to-Female Ratio of this age group for each country. Note the ratio will be in the same order as countries so they will be paired correctly if both the name and ratio is called
    for line7 in myfile7:#Goes through each line ine the file
        fields7=line7.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        quot3=int(fields7[1]) / int(fields7[2])#Since the populations for male and female are strings in this age group, you must convert them into integers and divide the male population by the female population to get the ratio
        ratio3.append(quot3)#Each ratio is added to the empty list
    return ratio3#The list is stored in the function
def Printcountryandraio():#Option 5, Prints out each country and their total Male-To-Female Ratio
    myfile8=open("WorldCensusAges0-14.csv")
    names2=[]#Empty list to store the names of each country. Note they will remain in the same order as in the original file
    for line8 in myfile8:#Goes through each line ine the file
        fields8=line8.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        names2.append(fields8[0])#Each country name is added to the empty list
    result4=getRatioPop14()#The list of ratios from getRatioPop14 function is stored here
    result5=getRatioPop15()#The list of ratios from getRatioPop15 function is stored here
    result6=getRatioPop64()#The list of ratios from getRatioPop64 function is stored here
    print("Country".ljust(50), "Total M-F Ratio")#1.just(50) provides beteween the two strings
    for i in range(len(names2)):#Loop that will go through each index in each of the lists that are being used in this function
        print(names2[i].ljust(50), round(result4[i]+result5[i]+result6[i],2)) #Print each country as well as rounded total Male to Female ratio by combing the ratio from each age group. The l.just() function will be used throughout the program as it provides a constant amount of space throughout a loop
        if i%20==0 and i!=0:
            response=input("Enter q to quit or any other key to continue: ")#Gives the user the option to keep looking at outpusst after each group of 20 outputs
            if response=="q": #To quit they must enter the letter q 
                break #If tey do the loop will be exited

def mPop14(): #Gets the population of Males for each country in the age group 0-14
    myfile10=open("WorldCensusAges0-14.csv")
    pop4=[]#Empty list to store the male population of each country in this age group. Note they will remain in the same order as in the original file
    for line10 in myfile10:#Goes through each line ine the file
        fields10=line10.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrypop=int(fields10[1])#Each male population will be converted from a string to an integer 
        pop4.append(countrypop)#Each male population of this age group will be added to the empty list
    return pop4#The list is stored in the function

def mPop15():#Gets the population of Males for each country in the age group 15-64
    myfile11=open("WorldCensusAges15-64.csv")
    pop5=[]#Empty list to store the male population of each country in this age group. Note they will remain in the same order as in the original file
    for line11 in myfile11:#Goes through each line ine the file
        fields11=line11.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrypop2=int(fields11[1])#Each male population will be converted from a string to an integer
        pop5.append(countrypop2)#Each male population of this age group will be added to the empty list
    return pop5#The list is stored in the function

def mPop64():#Gets the population of Males for each country in the age group 64+
    myfile12=open("WorldCensusAges64+.csv")
    pop6=[]#Empty list to store the male population of each country in this age group. Note they will remain in the same order as in the original file
    for line12 in myfile12:#Goes through each line ine the file
        fields12=line12.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrypop3=int(fields12[1])#Each male population will be converted from a string to an integer
        pop6.append(countrypop3)#Each male population of this age group will be added to the empty list
    return pop6#The list is stored in the function

def fPop14():#Gets the population of Females for each country in the age group 0-14
    myfile13=open("WorldCensusAges0-14.csv")
    pop7=[]#Empty list to store the female population of each country in this age group. Note they will remain in the same order as in the original file
    for line13 in myfile13:#Goes through each line ine the file
        fields13=line13.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrypop4=int(fields13[2])#Each female population will be converted from a string to an integer
        pop7.append(countrypop4)#Each female population of this age group will be added to the empty list
    return pop7#The list is stored in the function

def fPop15():#Gets the population of Females for each country in the age group 15-64
    myfile14=open("WorldCensusAges15-64.csv")
    pop8=[]#Empty list to store the female population of each country in this age group. Note they will remain in the same order as in the original file
    for line14 in myfile14:#Goes through each line in the file
        fields14=line14.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrypop5=int(fields14[2])#Each female population will be converted from a string to an integer
        pop8.append(countrypop5)#Each female population of this age group will be added to the empty list
    return pop8#The list is stored in the function

def fPop64():#Gets the population of Females for each country in the age group 64+
    myfile15=open("WorldCensusAges64+.csv")
    pop9=[]#Empty list to store the female population of each country in this age group. Note they will remain in the same order as in the original file
    for line15 in myfile15:#Goes through each line in the file
        fields15=line15.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrypop6=int(fields15[2])#Each female population will be converted from a string to an integer
        pop9.append(countrypop6)#Each female population of this age group will be added to the empty list
    return pop9#The list is stored in the function
def CountryMandFPop():#Option 6, Prints each country and their total male and female populations
    myfile16=open("WorldCensusAges0-14.csv")
    countrynames2=[]#Empty list to store the names of each country. Note they will remain in the same order as in the original file
    for line16 in myfile16:#Goes through each line in the file
        fields16=line16.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrynames2.append(fields16[0])#Each country name is added to the empty list
    result7=mPop14()#The list of male populations from the mPop14() is stored here
    result8=mPop15()#The list of male populations from the mPop15() is stored here
    result9=mPop64()#The list of male populations from the mPop64() is stored here
    result10=fPop14()#The list of female populations from the fPop14() is stored here
    result11=fPop15()#The list of female populations from the fPop15() is stored here
    result12=fPop64()#The list of female populations from the fPop64() is stored here
    print("Country".ljust(20), "Total Male Population".ljust(30), "Total Female Population")
    for i in range(len(countrynames2)):#For loop that goes through each index in each list that is used in the function because each list has the same length
        print(countrynames2[i].ljust(20), str(result7[i]+result8[i]+result9[i]).ljust(30), result10[i]+result11[i]+result12[i]) #Prints each country and their total male and female populations by combing each population fom the respective age group lists
        if i%20==0 and i!=0:
            response=input("Enter q to quit or any other key to continue: ")#Gives the user the option to keep looking at outpusst after each group of 20 outputs
            if response=="q": #To quit they must enter the letter q 
                break #If tey do the loop will be exited

def CountriesandAgePopdifference(): #Option 7, Compares 2 inputted countries' population data within in a certain age group
    myfile17=open("WorldCensusAges15-64.csv")
    countrynames3=[]#Empty list to store the names of each country. Note they will remain in the same order as in the original file
    for line17 in myfile17:#Goes through each line in the file
        fields17=line17.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrynames3.append(fields17[0])#Each country name is added to the empty list
    country=input("Enter the first country.Note:Capitalize the country name: ")#The user enters a country for comparison
    country=country.replace(" ", "")
    while not(country in countrynames3): #This loop checks to see if the country is within the list. If it is not, the user will have to enter another coutry until it's a valid one
        country=input("Country not found. Enter a different one: ")
        country=country.replace(" ", "")
    country2=input("Enter the second country.Note:Capitalize the country name: ")#The user enters the second country for comparison
    country2=country2.replace(" ", "")
    while not(country2 in countrynames3):#This loop checks to see if the country is within the list. If it is not, the user will have to enter another coutry until it's a valid one
        country2=input("Country not found. Enter a different one: ")
        country2=country2.replace(" ", "")
    choice3=input("Enter the age group you wish to look at (0-14, 15-64, 64+): ")#Allows the user to look at a certain age group
    while (choice3 != "0-14") and (choice3 != "15-64") and (choice3 != "64+"):#This loop cehcks to make sure it is a valid age group. If it is not, the user will have to keep entering until they enter a valid age group
        choice3=input("invalid choice. Please enter a valid age group: ")
    if choice3 == "0-14": #If the user selceted the 0-14 age group, the list of populations from that age group will be stored in a varaible to be used for the comparison
        result13=getPopAge14()
    elif choice3 == "15-64":
        result13=getPopAge15()#If the user selceted the 15-64 age group, the list of populations from that age group will be stored in a varaible to be used for the comparison
    elif choice3 == "64+":#If the user selceted the 64+ age group, the list of populations from that age group will be stored in a varaible to be used for the comparison
        result13=getPopAge64()
    if country in countrynames3: #Checks to see if the 1st country entered is in the list of countries.
        index2=countrynames3.index(country)#If so the the index= at which it occurs in the list is stored in to a variable
    if country2 in countrynames3:#Checks to see if the 2nd country entered is in the list of countries
        index3=countrynames3.index(country2)
    if result13[index2] > result13[index3]: #Using the indexes of the countries input, the program will look into whatever age group was selected at those indexes because they are in the same order as the country names so they correspond to each other. Whichever one is greater, its population and country name will be print first, then the other country slong with the difference
        print("Country".ljust(50), "Population of Ages %s" % (choice3))
        print(countrynames3[index2].ljust(50), result13[index2])
        print(countrynames3[index3].ljust(50), result13[index3])
        print("Difference: ", result13[index2] - result13[index3])
    else:
        print("Country".ljust(50), "Population of Ages %s" % (choice3))
        print(countrynames3[index3].ljust(50), result13[index3])
        print(countrynames3[index2].ljust(50), result13[index2])
        print("Difference: ", result13[index3] - result13[index2])

def ListCountriesMaleGreaterFemale():#Option 8, List all countries that have more males than females within their total population
    myfile18=open("WorldCensusAges15-64.csv")
    countrynames4=[]#Empty list to store the names of each country. Note they will remain in the same order as in the original file
    for line18 in myfile18:#Goes through each line in the file
        fields18=line18.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrynames4.append(fields18[0])#Each country name is added to the empty list
    result14= mPop14()#The list of male populations from the mPop14() is stored here
    result15= mPop15()#The list of male populations from the mPop15() is stored here 
    result16= mPop64()#The list of male populations from the mPop64() is stored here
    result17= fPop14()#The list of female populations from the fPop14() is stored here
    result18= fPop15()#The list of female populations from the fPop15() is stored here 
    result19= fPop64()#The list of female populations from the fPop64() is stored here
    countrynamesMvF=[] #An empty list 
    for i in range(len(countrynames4)):#For loop that goes through each index in each of the list as they are the same in length
        if (result14[i]+result15[i]+result16[i]) >(result17[i]+result18[i]+result19[i]): #Gets the total male population and female population of each country. If the country has more males than females, its name will be printed
            countrynamesMvF.append(countrynames4[i])#Countries that pass that condition will have their names to the list
            
    for i in range(len(countrynamesMvF)):#For loop that goes through each element in the list and prints it out
        print(countrynamesMvF[i])
        if i%20==0 and i!=0:
            response=input("Enter q to quit or any other key to continue: ")#Gives the user the option to keep looking at outputs after each group of a certain amount of outputs
            if response=="q": #To quit they must enter the letter q 
                break #If they do the loop will be exite
    
   

def LargestPop():#Option 9, Prints the country with the largest population within a certain country
    myfile19=open("WorldCensusAges15-64.csv")
    index=0
    result20=getPopAge14()#The list of total populations from getPopAge14 function is stored here
    result21=getPopAge15()#The list of total populations from getPopAge15 function is stored here
    result22=getPopAge64()#The list of total populations from getPopAge64 function is stored here
    countrynames5=[]#Empty list to store the names of each country. Note they will remain in the same order as in the original file
    choice4=input("Enter the age group you wish to look at(0-14, 15-64, 64+): ")#Allows the user to look at a certain age group
    while (choice4 != "0-14") and (choice4 != "15-64") and (choice4 != "64+"):#This loop cehcks to make sure it is a valid age group. If it is not, the user will have to keep entering until they enter a valid age group
        choice4=input("invalid choice. Please enter a valid age group: ")
    for line19 in myfile19:#Goes through each line in the file
        fields19=line19.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrynames5.append(fields19[0])#Each country name is added to the empty list    
    if choice4 == "0-14": #Whichever age group is selected the program will find the maximum population in that and store into a variable and store the index of that population    
        num=max(result20)
        index=result20.index(num)
              
    elif choice4 == "15-64":    
        num=max(result21)
        index=result21.index(num)
    elif choice4 == "64+":    
        num=max(result22)
        index=result22.index(num)
    print(countrynames5[index].ljust(50), "Populatiion:", num)   #The index from the max population will be used to find the contry that corresponds to it as the country names lis is in the same order as the group lists, meaing each population iw paired up correctly have in the same ndex in their respectives lists   
    #That country will be printed as well as their population    
                   
def AllCountriesPopAge():#Option 1 Prints all contries and their population data
    myfile20=open("WorldCensusAges15-64.csv")
    countrynames6=[]#Empty list to store the names of each country. Note they will remain in the same order as in the original file
    result23=getPopAge14()#The list of total populations from getPopAge14 function is stored here
    result24=getPopAge15()#The list of total populations from getPopAge15 function is stored here
    result25=getPopAge64()#The list of total populations from getPopAge64 function is stored here
    for line20 in myfile20:#Goes through each line in the file
        fields20=line20.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrynames6.append(fields20[0])#Each country name is added to the empty list
    print("Country".ljust(20), "Ages 0-14".ljust(20), "Ages 15-64".ljust(20), "Ages 64+")
    for i in range(len(countrynames6)):#For loop that goes through each index in each of the list as they are the same in length
        print(countrynames6[i].ljust(20), str(result23[i]).ljust(20), str(result24[i]).ljust(20), str(result25[i]))#Each country will be printed along wit their population data for each age group. Because the index im lookig for is i na dbecause is increasing itwill go every country and their corresponding data
        if i%20==0 and i!=0: #Allows the user to see 20 outputs at a time
            response=input("Enter q to quit or any other key to continue: ") #Gives the user the option of quitting this process or seeing more outputs
            if response=="q":
                break

def NumCountriesMvFPopAge():#Option 2 Tells the number of countries that have more males than females in each age group
    myfile21=open("WorldCensusAges15-64.csv")
    countrynames7=[]#Empty list to store the names of each country. Note they will remain in the same order as in the original file
    result26=mPop14()#The list of male populations from the mPop14() is stored here
    result27=mPop15()#The list of male populations from the mPop15() is stored here
    result28=mPop64()#The list of male populations from the mPop64() is stored here
    result29=fPop14()#The list of female populations from the fPop14() is stored here
    result30=fPop15()#The list of female populations from the fPop15() is stored here 
    result31=fPop64()#The list of female populations from the fPop64() is stored here
    for line21 in myfile21:#Goes through each line in the file
        fields21=line21.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrynames7.append(fields21[0])#Each country name is added to the empty list
    nums14=[]#Empty list that will store the names of countries that have more males than females in the Ages 0-14 group
    nums15=[]#Empty list that will store the names of countries that have more males than females in the Ages 15-64 group
    nums64=[]#Empty list that will store the names of countries that have more males than females in the Ages 64+ group
    for i in range(len(countrynames7)):#For loop that goes through each index in each of the list as they are the same in length 
        if result26[i]>result29[i]: #Compares the male population and female population in the 0-14 Age group
            nums14.append(countrynames7[i]) #If a country in this age group has more males than females, it will be added to nums14 list
    for i in range(len(countrynames7)):
        if result27[i]>result30[i]:#Compares the male population and female population of each country in the 15-64 Age group
            nums15.append(countrynames7[i])#If a country in this age group has more males than females, it will be added to nums15 list
    for i in range(len(countrynames7)):
        if result28[i]>result31[i]:#Compares the male population and female population of each country in the 64+ Age group
            nums15.append(countrynames7[i])#If a country in this age group has more males than females, it will be added to nums64 list

    print("Number of countries with greater males than females in Ages 0-14:", len(nums14)) #This displayS the number of countries that have more males than females in the 0-14 Age Group
    print("Number of countries with greater males than females in Ages 15-64:", len(nums15))#This displayS the number of countries that have more males than females in the 15-64 Age Group
    print("Number of countries with greater males than females in Ages 64+:", len(nums64)) #This displayS the number of countries that have more males than females in the 64+ Age Group


def LetterCountriesPop(letter):#Option 3 #Takes in an inputted letter and prints country names whose first letter is the inpuuted letter along with their respective population data
    myfile22=open("WorldCensusAges15-64.csv")
    countrynames8=[]#Empty list to store the names of each country. Note they will remain in the same order as in the original file
    for line22 in myfile22:#Goes through each line in the file
        fields22=line22.split(",")#Breaks each line into lists. 0th element being the country name, 1st element being male population, and 2nd element being the female population
        countrynames8.append(fields22[0])#Each country name is added to the empty list
        result32=getPopAge14()#The list of total populations from getPopAge14 function is stored here
        result33=getPopAge15()#The list of total populations from getPopAge15 function is stored here
        result34=getPopAge64()#The list of total populations from getPopAge64 function is stored here

    print("Country".ljust(20), "Ages 0-14".ljust(20), "Ages 15-64".ljust(20), "Ages 64+")
    print("If the there is nothing printed after this it means that there is no country starting with the letter you inputted")
    for i in range(len(countrynames8)):#For loop that goes through each index in each of the list as they are the same in length
        mystr=countrynames8[i]#In each iteration the country will be this variable
        if mystr[0]==letter: #This checks the first letter in the country's names to see if it is equal to the inputted letter 
            print(countrynames8[i].ljust(20), str(result32[i]).ljust(20), str(result33[i]).ljust(20), str(result34[i])) #If the condition passes, that country and its population data will be printed
        

def PrintMenu(): #The Menu for the entire program
    print("1. List all countries and the populaton of each Age Group")
    print("2. Show number of countries that have more males than females in each Age Group.")
    print("3. List countries starting with a certain letter and their population data.")
    print("4. List all countries and their total population.")
    print("5. List all countries and their  total male to female ratio.")
    print("6. List all countries and their total male and female populations.")
    print("7. Look at 2 different and see the difference in population in a certain Age Groups.")
    print("8. List all countries that have more males than females.")
    print("9. See which country has the largest population within a certain age group.")
    print("10. Quit.")
    userinput=int(input("Enter the number of option you wish to do: ")) #Allows th user to choose the input they wish to peform
    while (userinput<1) or (userinput>10): #This checks to make sure the user didn't enter a invalid option number
        userinput=int(input("Invalid input. Must be a number between 1 and 10: ")) #If they did, they wil have to keep entering until they enter a valid option number
    return userinput #The inputed option number is then stored into the function

def main():#This function will house the entire program
    option= PrintMenu() #The menu will be displayed and the option number that they choose will be stored in this varaible
    while option != 10: #As long as the option number is not equal to 10, the program will continue to run
        if option == 1:  #The following if statements will check to see which option the prgoram will have to perform. Each number that the option number is being compared to, corresponds to the appropriate option displayed in the menu
            AllCountriesPopAge() 
        elif option == 2:
            NumCountriesMvFPopAge()
        elif option == 3:
            choice=input("Enter the letter you wish to look at: ") #The LetterPopulationPop function has a parameter for a letter. Letter will be the inputted Alphabet letter.
            choice=choice.upper() #As each country in the list has captial letters, this function will make sure the inputted letter is not a lower case letter 
            LetterCountriesPop(choice) #The letter that was inputted by the user will be used as the argument for this function   
        elif option == 4:
            Printcountryandtotal()
        elif option == 5:
            Printcountryandraio()
        elif option == 6:
            CountryMandFPop()
        elif option == 7:
            CountriesandAgePopdifference()
        elif option == 8:
            ListCountriesMaleGreaterFemale()
        else:
            LargestPop()
        print(" ")#Used to create space in between sections
        print(" ")
        print(" ")
        print(" ")  
        option= PrintMenu() #The menu will be displayed so the user will have a chance to do a different option or quit the entire program   
           
main() #This will call the entire program when the Python shell is launched        
    
            
        
    
    
    
        

        
    
#This function calls were used during testing        
##Printcountryandtotal()#
##Printcountryandraio()
##CountryMandFPop()
##CountriesandAgePopdifference()
##LargestPop()
##ListCountriesMaleGreaterFemale()
##AllCountriesPopAge()  
##NumCountriesMvFPopAge()
##LetterCountriesPop()  




                 


        
                 
                                 
        
        
        
        

        
        
    


