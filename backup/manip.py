# import re

# file = open("cleaned.csv", 'w', encoding='utf-8')
# file.write("PID,Player,Team,Apps,Minutes,Goals,Assists,xG,xA,xG90,xA90\n")

# for line in open("test.txt", encoding='utf-8'):
# 	#line = line.replace("\+\d.\d\d\s"," ")
# 	line = re.sub(r"\+\d.\d\d\s", " ", line)
# 	line = re.sub(r"\-\d.\d\d\s", " ", line)
# 	if len(line)>43:
# 		line = line.replace(" ", ",", 1)

# 		line = line.replace(" Arsenal",",Arsenal")
# 		line = line.replace(" Bournemouth",",Bournemouth")
# 		line = line.replace(" Brighton",",Brighton")
# 		line = line.replace(" Burnley",",Burnley")
# 		line = line.replace(" Chelsea",",Chelsea")
# 		line = line.replace(" Crystal Palace",",Crystal Palace")
# 		line = line.replace(" Everton",",Everton")
# 		line = line.replace(" Huddersfield",",Huddersfield")
# 		line = line.replace(" Leicester",",Leicester")
# 		line = line.replace(" Liverpool",",Liverpool")
# 		line = line.replace(" Manchester City",",Manchester City")
# 		line = line.replace(" Manchester United",",Manchester United")
# 		line = line.replace(" Newcastle United",",Newcastle United")
# 		line = line.replace(" Southampton",",Southampton")
# 		line = line.replace(" Stoke",",Stoke")
# 		line = line.replace(" Swansea",",Swansea")
# 		line = line.replace(" Tottenham",",Tottenham")
# 		line = line.replace(" Watford",",Watford")
# 		line = line.replace(" West Bromwich Albion",",West Bromwich Albion")
# 		line = line.replace(" West Ham",",West Ham")

# 		line = line.replace(" 0",",0")
# 		line = line.replace(" 1",",1")
# 		line = line.replace(" 2",",2")
# 		line = line.replace(" 3",",3")
# 		line = line.replace(" 4",",4")
# 		line = line.replace(" 5",",5")
# 		line = line.replace(" 6",",6")
# 		line = line.replace(" 7",",7")
# 		line = line.replace(" 8",",8")
# 		line = line.replace(" 9",",9")		
# 		line = line.replace("-",",-")
# 		line = line.replace("+",",+")

# 		line = line.replace("n,-","n-")
# 		line = line.replace("o,-","o-")
# 		line = line.replace("g,-","g-")
# 		line = line.replace("u,-","u-")
# 		line = line.replace("s,-","s-")
# 		line = line.replace("d,-","d-")
# 		line = line.replace("r,-","r-")
# 		line = line.replace("e,-","e-")
# 		line = line.replace("t,-","t-")

# 		file.write(line)



import pandas as pd

df = pd.read_csv('cleaned.csv')

print(df)