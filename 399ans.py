from math import sqrt

gRatio = (1+sqrt(5))/2

ans = 1

power = (130771793)
power2 = 130772672

a = power


#Gratio in 1000 power
thou = 9.719417773591144
thouPow = 208

thou100 = 5.807978471287593
thou100Pow = thouPow * 100 + 98


#Gratio in 1000*200 power
thou200 = 3.3732613922940165
thou200Pow = thouPow*1000+197

#Gratio in 1000*200*200 power
thou40000 = 4.0737948041819607
thou40000Pow = thou200Pow*200+105

fi1 = 6.760790054060699
fiPow1 = thou40000Pow*3+1

fi2 = 9.697276407051078
fiPow2 = thou200Pow*53+23

#Left 10571793

fi3 = 1.669647443596891
fiPow3 = thou100Pow*105+80

#left 71793

fi4 = 1.3257381334798798
fiPow4 = thouPow * 71 + 70

#left 793

fi5 = 5.335789870508275
fiPow5 = 165

complete = fi1*fi2*fi3*fi4*fi5
completePow = fiPow1+fiPow2+fiPow3+fiPow4+fiPow5

print complete
print completePow

(pow(pow((pow(pow(pow(gRatio,1000)/(pow(10,208)),200)/(pow(10,197)),200)/pow(10,105)),3),1.089764941666666)/sqrt(5))*pow(10,0.06736625)

((((208*200)+197)*200)+105)*3.26929825

