import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

datafile = open('Comp Sci Data - Sheet1.csv','r')
data = datafile.readlines()

final = []
educations=[[],[],[],[],[],[],[]]
educationLevels=['High school DO\r\n', 'College DO\r\n', 'Bachelors\r\n', 'Masters of Arts\r\n', 'Masters of Science\r\n', 'Masters of Business\r\n', 'Juris Doctor\r\n']

for line in data[1:]:
    name, networth, education = line.split(',')
    if education != "N/A\r\n":
        num = educationLevels.index(education)
        educations[num].append(float(networth))
    
plt.rcParams["figure.figsize"] =[8,7]

for level in range(len(educations)):
    plt.figure()
    plt.boxplot(educations[level], 0, "rs", 0)
    plt.title(str(educationLevels[level])+"\n"+str(len(educations[level]))+" People")
    plt.xlabel("Net Worth (Billion $)")
    plt.yticks([1],["Education"])
    plt.savefig("whiskeyPlot"+str(level)+".png")
