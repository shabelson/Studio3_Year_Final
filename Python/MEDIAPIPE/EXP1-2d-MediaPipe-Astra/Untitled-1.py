f = open("./MEDIAPIPE/EXP1-2d-MediaPipe-Astra/hands.csv",'r')
f2 = open("./MEDIAPIPE/EXP1-2d-MediaPipe-Astra/hands_fix.csv",'w')

for line in f:

   l =line.split("=")
   
   for ln in l:
       ls = ln.split("_")
       if len(ls)>1:
           print (ls[1],"\n")
           f2.write(ls[1])
           f2.write('\n')

f.close()
f2.close()

