#!/usr/bin/env python3

# FIXME: getting two bits
# 00_40 31_46
# Can we find instance where they are not aliased?
WA7USED = 0

from prjxray.segmaker import Segmaker

segmk = Segmaker("design.bits")

print("Loading tags")
'''
module,loc,c31,b31,a31
my_NDI1MUX_NI_NMC31,SLICE_X12Y100,1,1,0
my_NDI1MUX_NI_NMC31,SLICE_X12Y101,1,1,1
my_NDI1MUX_NI_NMC31,SLICE_X12Y102,1,1,1
'''
f = open('params.csv', 'r')
f.readline()
for l in f:
    l = l.strip()
    module, loc, c31, b31, a31 = l.split(',')
    c31 = int(c31)
    b31 = int(b31)
    a31 = int(a31)
    segmk.add_site_tag(loc, "ALUT.DI1MUX.AI", 1 ^ a31)
    segmk.add_site_tag(loc, "BLUT.DI1MUX.BI", 1 ^ b31)
    segmk.add_site_tag(loc, "CLUT.DI1MUX.CI", 1 ^ c31)

segmk.compile()
segmk.write()
