blocksPower = k = 0
blocks = 1

crossRoads = 0

sideBySide = 0
endToEnd = 0 
shiftedSideBySide = 0
endToSide = 0

"""
while True:
	blocksPower += 1
	blocks = 4**blocksPower
	
	oldSideBySide = sideBySide
	oldEndToEnd = endToEnd
	oldShiftedSideBySide = shiftedSideBySide
	oldEndToSide = endToSide

	
	sideBySide = blocks
	endToSide = 4*blocks
	endToEnd = 0
	shiftedSideBySide = 0

	crossRoads += oldSideBySide
	endToEnd += 2*oldSideBySide
	sideBySide += oldSideBySide
	shiftedSideBySide += 0
	endToSide += 0
	
	endToSide += oldEndToSide
	shiftedSideBySide += oldEndToSide
	sideBySide += 0
	endToEnd += 0
	
	sideBySide += oldEndToEnd
	
	crossRoads += oldShiftedSideBySide
	endToSide += 2*oldShiftedSideBySide
"""
crN = "crossroads = "
cr = ""
sbsN = "sideBySide = "
sbs = ""
etsN = "endToSide = "
ets = ""
eteN = "endToEnd = "
ete = ""
ssbsN = "shiftedSideBySide = "
ssbs = ""
"""	
while blocksPower < 4:
        blocks = 4**blocksPower

        oldSideBySide = sideBySide
        oldEndToEnd = endToEnd
        oldShiftedSideBySide = shiftedSideBySide
        oldEndToSide = endToSide


        crossRoads += 2*oldSideBySide + oldShiftedSideBySide

        sideBySide = pow(4,k) + oldSideBySide + oldEndToEnd
        endToSide = pow(4,k+1) + oldEndToSide + 2*oldShiftedSideBySide
        endToEnd = 2*oldSideBySide
        shiftedSideBySide = oldEndToSide

        ocr = cr
        osbs = sbs
        oets = ets
        oete = ete
        ossbs = ssbs


        if k > 0:
                cr = "2*({})".format(osbs)
        if k > 1:
                cr += " + {}".format(ossbs)
        if k > 1:
                cr += " + {}".format(ocr)

        sbs = "pow(4,{})".format(k)
        if k > 0:
                sbs += " + {}".format(osbs)
        if k > 1:
                sbs += " + {}".format(oete)

        ets = "pow(4,{})".format(k+1)
        if k > 0:
                ets += " + {}".format(oets)
        if k > 1:
                ets += " + 2*({})".format(ossbs)

        if k > 0:	
                ete = "2*({})".format(osbs)

        ssbs = oets 

	
        print "k = {}".format(k)
        print "crossRoads = {} = ".format(crossRoads) + cr
        print "sideBySide = " + sbs
        print "endToSide = " + ets
        print "endToEnd = " + ete
        print "shiftedSideBySide = " + ssbs
        print ""

        blocksPower += 1
        k = blocksPower
"""

oldSideBySide = 0
oldEndToSide = 0

sideBySide = 0#pow(4,0)
endToSide = 0#pow(4,1)

blocksPower = k = 0

while blocksPower < 6:
        blocks = 4**blocksPower

        oldOldSideBySide = oldSideBySide
        oldOldEndToSide = oldEndToSide

        oldSideBySide = sideBySide
        oldEndToEnd = endToEnd
        oldShiftedSideBySide = shiftedSideBySide
        oldEndToSide = endToSide


        """
        crossRoads += 2*oldSideBySide + oldShiftedSideBySide
        sideBySide = pow(4,k) + oldSideBySide + oldEndToEnd
        endToSide = pow(4,k+1) + oldEndToSide + 2*oldShiftedSideBySide
        endToEnd = 2*oldSideBySide
        shiftedSideBySide = oldEndToSide
        """

        
        crossRoads += 2*oldSideBySide + oldOldEndToSide
        sideBySide = pow(4,k) + oldSideBySide + 2*oldOldSideBySide
        endToSide = pow(4,k+1) + oldEndToSide + 2*oldOldEndToSide
        endToEnd = oldSideBySide
        shiftedSideBySide = oldEndToSide
        
        """
        crossRoads += 2*oldSideBySide + oldOldEndToSide
        sideBySide = pow(4,k) + pow(4,k-1) + 3*oldOldSideBySide
        endToSide = pow(4,k+1) + pow(4,k) + 3*oldOldEndToSide
        endToEnd = oldSideBySide
        shiftedSideBySide = oldEndToSide
        """

        ocr = cr
        osbs = sbs
        oets = ets
        oete = ete
        ossbs = ssbs


        if k > 0:
                cr = "2*({})".format(osbs)
        if k > 1:
                cr += " + {}".format(ossbs)
        if k > 1:
                cr += " + {}".format(ocr)

        sbs = "pow(4,{})".format(k)
        if k > 0:
                sbs += " + {}".format(osbs)
        if k > 1:
                sbs += " + {}".format(oete)

        ets = "pow(4,{})".format(k+1)
        if k > 0:
                ets += " + {}".format(oets)
        if k > 1:
                ets += " + 2*({})".format(ossbs)

        if k > 0:	
                ete = "2*({})".format(osbs)

        ssbs = oets 

	
        print "k = {}".format(k)
        print "crossRoads = {} = ".format(crossRoads) + cr
        print "sideBySide = {} = ".format(sideBySide) + sbs
        print "endToSide = {} = ".format(endToSide) + ets
        print "endToEnd = " + ete
        print "shiftedSideBySide = " + ssbs
        print ""

        blocksPower += 1
        k = blocksPower
	

#k = 1
#sideBySide = pow(4,1)
#endToSide = pow(4,2)
	
#k = 2
#crossRoads = pow(4,1)
#sideBySide = pow(4,2) + pow(4,1)
#endToSide = pow(4,3) + pow(4,2)
#endToEnd = 2*pow(4,1)
#shiftedSideBySide = pow(4,2)

#k = 3
#crossRoads = (pow(4,2) + pow(4,1)) + (pow(4,2)) + pow(4,1)
#crossRoads = 
