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
        
for level in range(len(educations)):
    networths=0
    for networth in educations[level]:
        networths+=networth
        avrnetworth = networths/len(educations[level])
    final.append(avrnetworth)
    educationLevels[level] += "(" + str(len(educations[level])) + " People)"

plt.rcParams["figure.figsize"] =[16,6]

fig, ax = plt.subplots(1, 1)
a = ax.bar([1,3,5,7,9,11,13], final, align="center")
ax.set_title('Average Wealth of Richest People\n('+str(len(data)-1)+" People)")
plt.xticks([1,3,5,7,9,11,13], educationLevels)
ax.set_xlabel('Education Level')
ax.set_ylabel('Net Worth (Billion $)')
fig.savefig("main.png")
