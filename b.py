
blocks = 1

orthogonal = 0
sideBySide = 0
endToEnd = 0
shiftedSideBySide = 0
crossroadCount = 0


for i in xrange(4):
    sideBySideOld = sideBySide
    orthogonalOld = orthogonal
    endToEndOld = endToEnd
    shiftedSideBySideOld = shiftedSideBySide

    sideBySide = blocks
    blocks *= 4
    orthogonal = blocks

    #sidebysideold
    sideBySide += sideBySideOld
    endToEnd = 2*sideBySideOld
    crossroadCount += 2*sideBySideOld

    #orthogonalold
    orthogonal += orthogonalOld
    shiftedSideBySide = orthogonalOld

    #endtoendold
    sideBySide += endToEndOld

    #shiftedsidebysideold
    orthogonal += 2*shiftedSideBySideOld
    crossroadCount += shiftedSideBySideOld

print crossroadCount

"""
blocks = 1

orthogonal = 0
sideBySide = 0
endToEnd = 0
shiftedSideBySide = 0
crossroadCount = 0


while True:
    sideBySideOld = sideBySide
    orthogonalOld = ortohognal
    endToEndOld = endToEnd
    shiftedSideBySideOld = shiftedSideBySide

    sideBySide = blocks
    blocks *= 4
    orthogonal = blocks

    #sidebysideold
    sideBySide += sideBySideOld
    endToEnd = 2*sideBySideOld
    crossroadCount += 2*sideBySideOld

    #orthogonalold
    orthogonal += orthogonalOld
    shiftedSideBySide = orthogonalOld

    #endtoendold
    sideBySide += endToEndOld

    #shiftedsidebysideold
    orthogonal += 2*shiftedSideBySideOld
    crossroadCount += shiftedSideBySideOld
"""
