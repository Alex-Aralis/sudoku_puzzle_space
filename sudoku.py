
SL = []

for a in range(1, 10):
    for b in range(a, 10):
        for c in range(b, 10):
            if a != b != c != a:
                SL.append((a, b, c))

print(SL)
print(len(SL))

SLBN = {}

for a in range(1, 10):
    SLBN[a] = set()
    for isl, sl in enumerate(SL):
        for n in sl:
            if n == a:
                SLBN[a].add(isl)


print(SLBN)
print(len(SLBN[1]))

for isl in SLBN[8]:
    print(SL[isl])

DSL = []

for ia, sla in enumerate(SL):
    DSL.append(set())

    for ib, slb in enumerate(SL):
        if set(sla).isdisjoint(set(slb)):
            DSL[ia].add(ib)

    DSL[ia] = frozenset(DSL[ia])
     

print(DSL)

print(DSL[0].intersection(DSL[65]))


L = []


for sla, dsl in enumerate(DSL):
    for slb in sorted(dsl):
        if slb > sla:
            for slc in sorted(dsl.intersection(DSL[slb])):
               if slc > slb:
                   L.append((sla, slb, slc))


print(L)
print(len(L))

LBSL = []

for ia, sla in enumerate(SL):
    LBSL.append(set())
    for ib, lb in enumerate(L):
        if ia in lb:
            LBSL[ia].add(ib)

print(LBSL)
print(len(LBSL))

LBSLS = {}

for ia in range(0, len(SL)):
    LBSLS[ia] = {}
    for ib in range(ia, len(SL)):
        LBSLS[ia][ib] = {}

for il, l in enumerate(L):
    for ia in range(0, len(SL)):
        if l[0] == ia:
            for ib in range(ia, len(SL)):
                if l[1] == ib:
                    for ic in range(ib, len(SL)):
                        if l[2] == ic:
                            LBSLS[ia][ib][ic] = il
                            print(ia, ib, ic)
                            
print(LBSLS)
print(LBSLS[10][12])

print(SL[10])
print(SL[12])
print(SL[35])

print(LBSL[10])
print(LBSL[12])
print(LBSL[35])

print(DSL[10])
print(DSL[12])
print(DSL[35])

#for ia in range(0, len(SL)):
#    for ib in range(ia, len(SL)):
##        if sl[0:1] == (ia)
#        for ic in range(ib, len(SL)):
#            for isl, sl in enumerate(SL):
#                if (ia, ib, ic) == sl:
                    

#for ia, la in L:
#    for ib, sla in la:
        

#for ia, dsla in enumerate(DSL):
#    LBSLS[ia] = {}
#    for ib in dsla:
#        LBSLS[ia][ib] = {}
#        for ic in dsla.intersection(DSL[ib]):
#            for l in LBSL[ia].intersection(LBSL[ib]).intersection(LBSL[ic]):
#                LBSLS[ia][ib][ic] = l
            

#for ia, sla in enumerate(SL):
#    LBSLS[ia] = {}
#    for ib in LBSL[ia]:
#        LBSLS[ia][ib] = {}
#        for ic in LBSL[ia].intersection(LBSL[ib]):
#            LBSLS[ia][ib][ic] = ic


XL = []


for il, l in enumerate(L):
    XL.append(set())
    for inaa, naa in enumerate(SL[l[0]]):
        for inab, nab in enumerate(SL[l[1]]):
            for inac, nac in enumerate(SL[l[2]]):
                for inba, nba in enumerate(SL[l[0]]):
                    if inba != inaa:
                        for inbb, nbb in enumerate(SL[l[1]]):
                            if inbb != inab:
                                for inbc, nbc in enumerate(SL[l[2]]):
                                    if inbc != inac:
                                       for inca, nca in enumerate(SL[l[0]]):
                                           if inca != inba and inca != inaa:
                                               for incb, ncb in enumerate(SL[l[1]]):
                                                   if incb != inbb and incb != inab:
                                                       for incc, ncc in enumerate(SL[l[2]]):
                                                           if incc != inac and incc != inbc:
                                                              xsla, xslb, xslc = sorted(((SLBN[naa]&SLBN[nab]&SLBN[nac]).pop(), (SLBN[nba]&SLBN[nbb]&SLBN[nbc]).pop(), (SLBN[nca]&SLBN[ncb]&SLBN[ncc]).pop())) 

                                                              XL[il].add(LBSLS[xsla][xslb][xslc])

print(XL)


#for ia, la in enumerate(L):
#    XL.append(set())
#
#    for ib, lb in enumerate(L):
#        test = True
#        for sla in la:
#            for slb in lb:
#                if len(SL[sla].intersection(SL[slb])) != 1:
#                    test = False
#
#        if test:
#            XL[ia].add(ib)
#
#    XL[ia] = frozenset(XL[ia])
#
#print(XL)
#print(len(XL))

print(len(XL))
print(XL[180])
print(XL[166])
print(len(XL[180]))


#IL = []
#
#for ia, la in enumerate(L):
#    IL.append(set())
#    for ib, lb in enumerate(L):
#        if len(la.intersection(lb)) > 0:
#            IL[ia].add(ib)
#    IL[ia] = frozenset(IL[ia])

#print(IL)
#print(len(IL))


#BL = []


#for ia, la in L:
#    for ib in la:
#        for ic in LBSL[ib]:
#            LBSL


#QDL = []

#for ia, la in enumerate(L):
#    for ib, lb in enumerate(L):
#        for sla in la:
#            for slb in DSL[sla]:
#                for slc in DSL[sla].intersection(DSL[slb]):
                    
                
#for ia, la in enumerate(L):
#    QDL.append(set())
#
#    sla = list(la)
#    for qdsla in DSL[sla[0]]:
#        for qdslb in DSL[sla[1]].intersection(DSL[qdsla]):
#            for qdslc in DSL[sla[2]].intersection(DSL[qdsla]).intersection(DSL[qdslb]):
#                for qdl in LBSL[qdsla].intersection(LBSL[qdslb]).intersection(LBSL[qdslc]):
#                    QDL[ia].add(qdl)
#
#    QDL[ia] = frozenset(QDL[ia])


#print(QDL)
#print(len(QDL))


#print("0")
#for sl in L[0]:
#    print(SL[sl])
#
#print("131")
#for sl in L[131]:
#    print(SL[sl])
#
#print(QDL[0].intersection(QDL[131]))
#
#print("printing qdl intersections")
#for qdla in QDL[0].intersection(QDL[131]):
#    print(QDL[qdla].intersection(QDL[0]).intersection(QDL[131]))
#
#for ia, la in enumerate(L):
#    for ib in QDL[ia]:
        

def printl(l):
    if type(l) is int:
        l = L[l]

    for sl in l:
        print(SL[sl])


BL = set()


def lineBySLs(ia, ib, ic):
    for l in LBSL[ia].intersection(LBSL[ib]).intersection(LBSL[ic]):
        return l

FBL = set()



for isla1 in range(0, len(SL)):
    for ila in LBSL[isla1]:
        for il1 in LBSL[isla1]:
            for isla2 in L[ila]:
                if isla2 != isla1:
                    for islb1 in L[il1]:
                        if isla1 != islb1:
                            for il2 in LBSL[isla2]:
                                for ilb in LBSL[islb1]:
                                    for islb22 in L[il2]:
                                        if islb22 != isla2:
                                            for islb2b in L[ilb]:
                                                if islb2b != islb1:
                                                    if islb2b == islb22:
                                                        islb2 = islb2b
                                                        for isla3 in L[ila]:
                                                            if isla3 != isla1 and isla3 != isla2:
                                                                for islb3 in L[ilb]:
                                                                    if islb3 != islb1 and islb3 != islb2:
                                                                        if isla3 != islb3: 
                                                                            for il3 in LBSL[isla3]&LBSL[islb3]:
                                                                                for islc1 in L[il1]:
                                                                                    if islc1 != isla1 and islc1 != islb1: 
                                                                                        for islc2 in L[il2]:
                                                                                            if islc2 != isla2 and islc2 != islb2:
                                                                                                if islc1 != islc2: 
                                                                                                    for ilc in LBSL[islc1]&LBSL[islc2]:
                                                                                                        for islc33 in L[il3]:
                                                                                                            if islc33 != isla3 and islc33 != islb3: 
                                                                                                                for islc3c in L[ilc]:
                                                                                                                    if islc3c != islc1 and islc3c != islc2:
                                                                                                                        if islc33 == islc3c:
                                                                                                                            islc3 = islc33
                                                                                                                            #isla1, isla2, isla3 = sorted((isla1, isla2, isla3))
                                                                                                                            #islb1, islb2, islb3 = sorted((islb1, islb2, islb3))
                                                                                                                            #islc1, islc2, islc3 = sorted((islc1, islc2, islc3))
                                                                                                                            FBL.add(tuple(sorted((ila, ilb, ilc))))


FBL = sorted(FBL)
print(FBL)                                                                            
print(len(FBL))

#for iaa in range(0, len(SL)):
#    for iab in DSL[iaa]:
#        for iba in DSL[iab]:
#            for ibb in DSL[iab]&DSL[iba]:
#                for iac in DSL[iaa]&DSL[iab]:
#                    for ica in DSL[iaa]&DSL[iba]:
#                        for ibc in DSL[iba]&DSL[ibb]&DSL[iac]:
#                            for icb in DSL[iab]&DSL[ibb]&DSL[ica]:
#                                for icc in DSL[iac]&DSL[ica]&DSL[ibc]&DSL[icb]:
#                                    iaa, iab, iac = sorted((iaa, iab, iac))
#                                    i
#                                    print(LBSLS[aa][])
#                


#for ia, sla in enumerate(DSL):
#    for ib in sla:
#        for ic in sla.intersection(DSL[ib]):
#            for ig in DSL[ia]:
#                for ih in DSL[ib].intersection(DSL[ig]):
#                    for ii in DSL[ic].intersection(DSL[ig]).intersection(DSL[ih]):
#                        for ik in DSL[ia].intersection(DSL[ig]):
#                            for il in DSL[ib].intersection(DSL[ih]).intersection(DSL[ik]):
#                                for im in DSL[ic].intersection(DSL[ii]).intersection(DSL[ik]).intersection(DSL[il]):
#                                    print(frozenset(((frozenset((frozenset((ia,ib,ic)), frozenset((ig,ih,ii)), frozenset((ik,il,im)))), frozenset((frozenset((ia,ig,ik)), frozenset((ib,ih,il)), frozenset((ic,ii,im))))))))
#
#                                    print(LBSLS[ic][ib][ia])
#                                    for a in frozenset(((frozenset((frozenset((ia,ib,ic)), frozenset((ig,ih,ii)), frozenset((ik,il,im)))), frozenset((frozenset((ia,ig,ik)), frozenset((ib,ih,il)), frozenset((ic,ii,im))))))):
#                                        print(a)
#                                        for b in a:
#                                            print(b)
#                                            for c in b:
#                                                print(SL[c])
#
#                                    BL.add(((frozenset((frozenset((ia,ib,ic)), frozenset((ig,ih,ii)), frozenset((ik,il,im)))), frozenset((frozenset((ia,ig,ik)), frozenset((ib,ih,il)), frozenset((ic,ii,im)))))))
#                                    print("BL start")
#                                    ia, ib, ic = sorted((ia,ib,ic))
#                                    ig, ih, ii = sorted((ig,ih,ii))
#                                    ik, il, im = sorted((ik,il,im))
#                                    print(ia, ib, ic)
#                                    print(ig, ih, ii)
#                                    print(DSL[ig])
#                                    print(DSL[ih])
#                                    print(DSL[ii])
#                                    print(ik, il, im)
#                                    print(LBSLS[ia][ib][ic])
#                                    print(LBSLS[ig][ih][ii])
#                                    print(LBSLS[ik][il][im])
#                                    FBL.add(tuple(sorted((LBSLS[ia][ib][ic], LBSLS[ig][ih][ii], LBSLS[ik][il][im]))))



#FBL = sorted(FBL)
#
#print(FBL)
#print(len(FBL))

#for ia, fbla in enumerate(FBL):
#    tmp = None
#    if len(fbla) == 1:
#        tmp = list(fbla)
#        tmp = [tmp[0],tmp[0],tmp[0]]
#    else:
#        tmp = list(fbla)    
#    
#    FBL[ia] = tmp
#
#
#print(FBL)
#print(len(FBL))

#BLBL = []
#
#for ia, la in enumerate(L):
#    BLBL.append(set())
#    for ib, bl in enumerate(FBL):
#        if ia in bl:
#            BLBL[ia].add(ib)

BLBL = []

for bli in range(0,3):
    BLBL.append([])
    for il, la in enumerate(L):
        BLBL[bli].append(set())
        for ibl, bl in enumerate(FBL):
            if il == bl[bli]:
                BLBL[bli][il].add(ibl)

print(BLBL)
print(BLBL[0][9]&BLBL[1][9])


#print(BLBL)
#print(len(BLBL))

#770 268
print(FBL[770])


def printS(s):
    print(s)
    for ps in s:
        print("ps: " + str(ps))
        for bl in ps:
            print("FBL["+str(bl)+"]: " + str(FBL[bl]))
            for l in FBL[bl]:
                print("L["+str(l)+"]: " + str(L[l]))
                printl(l)


#def checkS(s):
#    s = list(s)
#    
#    for bl1 in s[0]:
#        for l1 in bl1:
#            for 



S = set()
S2 = set()

def delL(bl, dl):
    bl = list(bl)
    di = -1
    for i, l in enumerate(bl):
        if l == dl:
            di = i
            break 

    del(bl[di])
    return bl



#for ia, bla in enumerate(FLB):
#    for ib, blb in enumerate(FBL): 
#        for ic, blc in enumerate(FBL):
#            for la in bla:
#                for lb in blb:
#                    for lc in blc: 
#                        for xla in XL[la]: 
#                            for xlb in XL[lb]:
#                                for xlc in XL[lx]:
                                    



#for ia, bla in enumerate(FBL):
#    for la0 in bla:
#        for xla0 in XL[la]:
#            for ie in BLBL[xla0]:
#                ble0 = delL(FBL[ie], xla0)
#                for le0 in ble0:
#                    for xle0 in XL[le0]:
#                        for ib in BLBL[xle0]:
#                            blb0 = delL(FBL[ib], xle0)
#                            for lb0 in blb0:
#                                for 


def rtuple(rlist):
    memberList = []
    for member in rlist:
        if type(member) is list:
           member = rtuple(member)

        memberList.append(member)

    return tuple(memberList)
        

counter1 = 0
counter2 = 0
testSDict = {}



for ibla, bla in enumerate(FBL):
    for lae in set(bla):
        rbla2 = delL(bla, lae)
        usedAes = set()
        usedEas = set()
        for xlae in XL[lae]:
            usedAes.add((lae, xlae))
            usedEas.add((xlae, lae))
            for ible in (BLBL[0][xlae]|BLBL[1][xlae]|BLBL[2][xlae]):
                compiblg = set()
                rble2 = delL(FBL[ible], xlae)
                for leb in set(rble2):
                    rble1 = delL(rble2, leb)
                    usedEbs = set() 
                    usedBes = set()
                    for xleb in XL[leb]:
                        usedEbs.add((leb, xleb))
                        usedBes.add((xleb, leb))
                        for iblb in (BLBL[0][xleb]|BLBL[1][xleb]|BLBL[2][xleb]):
                            rblb2 = delL(FBL[iblb], xleb)
                            for lbg in set(rblb2):
                                rblb1 = delL(rblb2, lbg)
                                usedBgs = set() 
                                usedGbs = set() 
                                for xlbg in XL[lbg]:
                                    Bg = (lbg, xlbg)
                                    if Bg in usedBes: continue
                                    usedBgs.add(Bg)
                                    usedGbs.add((xlbg, lbg))
                                    for iblg in (BLBL[0][xlbg]|BLBL[1][xlbg]|BLBL[2][xlbg]):
                                        print("iblg", iblg, counter1, counter2)
                                        rblg2 = delL(FBL[iblg], xlbg)
                                        for lga in set(rblg2):
                                            rblg1 = delL(rblg2, lga)
                                            usedAgs = set()
                                            usedGas = set()
                                            for xlga in XL[lga]&set(rbla2):
                                                Ag = (xlga, lga)
                                                Ga = (lga, xlga)
                                                if Ag in usedAes: continue
                                                if Ga in usedGbs: continue
                                                usedAgs.add(Ag)
                                                usedGas.add(Ga)
                                                rbla1 = delL(rbla2, xlga)
                                                for lec in rble1:
                                                    for lgc in rblg1:
                                                        spblceg = set()
                                                        opblcegDict = {}
                                                        usedCes = set()
                                                        for xlec in XL[lec]:
                                                            if (lec, xlec) in usedEas|usedEbs: continue
                                                            usedCes.add((xlec, lec))
                                                            usedCgs = set()
                                                            usedGcs = set()
                                                            for xlgc in XL[lgc]:
                                                                Cg = (xlgc, lgc)
                                                                if Cg in usedCes: continue
                                                                if (lgc, xlgc) in usedGas|usedGbs: continue
                                                                usedCgs.add(Cg)
                                                                tblceg = (xlec, xlgc)
                                                                stblceg = tuple(sorted(tblceg)) 
                                                                spblceg.add(stblceg)        
                                                                if not stblceg in opblcegDict:
                                                                    opblcegDict[stblceg] = []
                                                                opblcegDict[stblceg].append((tblceg, usedCgs))
                                                        compiblc = set()
                                                        for pblceg in spblceg:
                                                            for iblc in (BLBL[0][pblceg[0]]&BLBL[1][pblceg[1]]|BLBL[0][pblceg[0]]&BLBL[2][pblceg[1]]|BLBL[1][pblceg[0]]&BLBL[2][pblceg[1]]):
                                                                print("iblc", iblc, len(S), counter1)
                                                                rblc1 = delL(delL(FBL[iblc], pblceg[0]), pblceg[1])
                                                                for lah in rbla1:
                                                                    for lbh in rblb1:
                                                                        for lch in rblc1:
                                                                            spblhabc = set()
                                                                            opblhabcDict = {}
                                                                            usedHas = set()
                                                                            for xlah in XL[lah]:
                                                                                if (lah, xlah) in usedAes|usedAgs: continue
                                                                                usedHas.add((xlah, lah))
                                                                                usedHbs = set()
                                                                                for xlbh in XL[lbh]:
                                                                                    Hb = (xlbh, lbh)
                                                                                    if (lbh, xlbh) in usedBes|usedBgs: continue
                                                                                    if Hb in usedHas: continue
                                                                                    usedHbs.add(Hb) 
                                                                                    for xlch in XL[lch]:
                                                                                        if (lch, xlch) in usedCes|opblcegDict[pblceg][0][1]: continue
                                                                                        if (xlch, lch) in usedHas|usedHbs: continue
                                                                                        tblhabc = (xlah, xlbh, xlch)
                                                                                        stblhabc = tuple(sorted(tblhabc))
                                                                                        spblhabc.add(stblhabc)
                                                                                        if not stblhabc in opblhabcDict:
                                                                                            opblhabcDict[stblhabc] = []
                                                                                        opblhabcDict[stblhabc].append(tblhabc)
                                                                            for pblhabc in spblhabc:
                                                                                for iblh in (BLBL[0][pblhabc[0]]&BLBL[1][pblhabc[1]]&BLBL[2][pblhabc[2]])-(compiblc|compiblg):
                                                                                    if iblh == iblg: print(iblg) #compiblg.add(iblg)
                                                                                    #print("=================================================================================")
                                                                                    #print(len(opblcegDict[pblceg]))
                                                                                    #print(len(opblhabcDict[pblhabc]))
                                                                                    for opblceg in opblcegDict[pblceg]:       
                                                                                        for opblhabc in opblhabcDict[pblhabc]:
                                                                                            #print(opblceg, opblhabc)
                                                                                            #prenews = ((((lae, xlae),        (xlga, lga),        (lah, opblhabc[0])),
                                                                                            #(  (xleb, leb),        (lbg, xlbg),        (lbh, opblhabc[1])),
                                                                                            #(  (opblceg[0][0], lec),  (opblceg[0][1], lgc),  (lch, opblhabc[2]))),
                                                                                            #( ((xlae, lae),        (leb, xleb),        (lec, opblceg[0][0]) ),
                                                                                            #(  (lga, xlga),        (xlbg, lbg),        (lgc, opblceg[0][1]) ),
                                                                                            #(  (opblhabc[0], lah), (opblhabc[1], lbh), (opblhabc[2], lch))))
                                                                                            
                                                                                            
                                                                                            counter1 += 1 
                                                                                            S.add(tuple(sorted((tuple(sorted((tuple(sorted(((lae, xlae), (xlga, lga), (lah, opblhabc[0])))),
                                                                                            tuple(sorted(((xleb, leb), (lbg, xlbg), (lbh, opblhabc[1])))),
                                                                                            tuple(sorted(((opblceg[0][0], lec), (opblceg[0][1], lgc), (lch, opblhabc[2]))))))),
                                                                                            tuple(sorted((tuple(sorted(((xlae, lae), (leb, xleb), (lec, opblceg[0][0])))), 
                                                                                            tuple(sorted(((lga, xlga), (xlbg, lbg), (lgc, opblceg[0][1])))), 
                                                                                            tuple(sorted(((opblhabc[0], lah), (opblhabc[1], lbh), (opblhabc[2], lch)))))))))))
                                                                                            
                                                                                            #if not news in testSDict:
                                                                                            #    testSDict[news] = []
                                                                                            #    testSDict[news].append((prenews, ibla, iblb, iblc, ible, iblg, iblh))
                                                                                            #else:
                                                                                            #    testSDict[news].append((prenews, ibla, iblb, iblc, ible, iblg, iblh))
                                                                                            #    counter2 += 1
                                                                                            #    print("--------------------------------------------------------------------------------")
                     # 
                     #                                                                           for ts in testSDict[news]:
                     #                                                                               print(ts)
                     #                                                                           print("compiblg", compiblg)
                     #                                                                           print("compiblc", compiblc)
                     #                                                                           print("opblceg", opblceg[0])
                     #                                                                           print("opblhabc", opblhabc)
                     #                                                                           print("--------------------------------------------------------------------------------")
                                                                                            
                                                                                            #print("--------------------------------------------------------------------------------")
                                                                                            #S.add(news)
                                                                                            #print(len(S), counter1, news)
                                                                                    #print("=================================================================================")
                                                                                    #compiblh.add(iblh)    
                                                                compiblc.add(iblc)                    
                                        compiblg.add(iblg)                                            
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    











compibla = set()
for ibla, bla in enumerate(FBL):
    for lae in set(bla):
        possibleAegs = set()
        rbla2 = delL(bla, lae)
        possibleEabs = set()
        for xlae in XL[lae]:
            compible = set(compibla)
            for ible in (BLBL[0][xlae]|BLBL[1][xlae]|BLBL[2][xlae])-compibla:
                rble2 = delL(FBL[ible], xlae)
                for leb in set(rble2):
                    rble1 = delL(rble2, leb)
                    possibleBegs = set()
                    for xleb in XL[leb]:
                        possibleEab = tuple(sorted(((xlae, lae), (leb, xleb))))
                        if possibleEab in possibleEabs: continue
                        possibleEabs.add(possibleEab)
                        compiblb = set(compibla)
                        for iblb in (BLBL[0][xleb]|BLBL[1][xleb]|BLBL[2][xleb])-compiblb:
                            print("iblb: ", iblb)
                            rblb2 = delL(FBL[iblb], xleb)
                            for lbg in set(rblb2):
                                rblb1 = delL(rblb2, lbg)
                                compiblg = set(compible|compiblb)
                                possibleGabs = set()
                                for xlbg in XL[lbg]:
                                    possibleBeg = tuple(sorted(((xleb, leb), (lbg, xlbg))))
                                    if possibleBeg in possibleBegs: continue
                                    possibleBegs.add(possibleBeg)
                                    for iblg in (BLBL[0][xlbg]|BLBL[1][xlbg]|BLBL[2][xlbg])-compiblg:
                                        print("iblg :", ibla, iblb, ible, iblg, compiblg, counter2, counter1)
                                        rblg2 = delL(FBL[iblg], xlbg)
                                        for lga in set(rblg2):
                                            rblg1 = delL(rblg2, lga)
                                            for xlga in XL[lga]&set(rbla2):
                                                possibleAeg = tuple(sorted(((lae, xlae), (xlga, lga))))
                                                if possibleAeg in possibleAegs: continue
                                                possibleAegs.add(possibleAeg)
                                                possibleGab = tuple(sorted(((lga, xlga),(lbg, xlbg))))
                                                if possibleGab in possibleGabs: continue
                                                possibleGabs.add(possibleGab)
                                                rbla1 = delL(rbla2, xlga)
                                                for lec in rble1:
                                                    for lgc in rblg1:
                                                        spblceg = set()
                                                        opblcegDict = {}
                                                        possibleCegs = set()
                                                        possibleEabcs = set()
                                                        for xlec in XL[lec]:
                                                            possibleEabc = tuple(sorted(((xlae, lae), (leb, xleb), (lec, xlec))))
                                                            if possibleEabc in possibleEabcs: continue
                                                            possibleEabcs.add(possibleEabc)
                                                            possibleGabcs = set()
                                                            for xlgc in XL[lgc]:
                                                                possibleGabc = tuple(sorted(((lga, xlga), (xlbg, lbg), (lgc, xlgc))))
                                                                if possibleGabc in possibleGabcs: continue
                                                                possibleGabcs.add(possibleGabc)
                                                                possibleCeg = tuple(sorted(((xlec, lec), (xlgc, lgc))))
                                                                if possibleCeg in possibleCegs: continue
                                                                possibleCegs.add(possibleCeg)
                                                                tblceg = (xlec, xlgc)
                                                                stblceg = tuple(sorted(tblceg)) 
                                                                spblceg.add(stblceg)        
                                                                if not stblceg in opblcegDict:
                                                                    opblcegDict[stblceg] = []
                                                                opblcegDict[stblceg].append(tblceg)
                                                        compiblc = set(compiblb)
                                                        for pblceg in spblceg:
                                                            for iblc in (BLBL[0][pblceg[0]]&BLBL[1][pblceg[1]]|BLBL[0][pblceg[0]]&BLBL[2][pblceg[1]]|BLBL[1][pblceg[0]]&BLBL[2][pblceg[1]])-compiblc:
                                                                compiblh = set(compiblg|compiblc)
                                                                #print("iblc", iblc, compiblc)
                                                                rblc1 = delL(delL(FBL[iblc], pblceg[0]), pblceg[1])
                                                                for lah in rbla1:
                                                                    possibleAeghs = set()
                                                                    for lbh in rblb1:
                                                                        possibleBeghs = set()
                                                                        for lch in rblc1:
                                                                            spblhabc = set()
                                                                            opblhabcDict = {}
                                                                            possibleHabcs = set()
                                                                            for xlah in XL[lah]:
                                                                                possibleAegh = tuple(sorted(((lae, xlae), (xlga, lga), (lah, xlah))))
                                                                                if possibleAegh in possibleAeghs: continue 
                                                                                possibleAeghs.add(possibleAegh)
                                                                                for xlbh in XL[lbh]:
                                                                                    possibleBegh = tuple(sorted(((xleb, leb), (lbg, xlbg), (lbh, xlbh))))
                                                                                    if possibleBegh in possibleBeghs: continue
                                                                                    possibleBeghs.add(possibleBegh)
                                                                                    possibleCeghs = set()
                                                                                    for xlch in XL[lch]:
                                                                                        possibleHabc = tuple(sorted(((xlah, lah), (xlbh, lbh), (xlch, lch))))
                                                                                        if possibleHabc in possibleHabcs: continue
                                                                                        possibleHabcs.add(possibleHabc)
                                                                                        possibleCegh = tuple(sorted(((pblceg[0], lec), (pblceg[1], lgc), (lch, xlch))))
                                                                                        if possibleCegh in possibleCeghs: continue
                                                                                        possibleCeghs.add(possibleCegh)
                                                                                        tblhabc = (xlah, xlbh, xlch)
                                                                                        stblhabc = tuple(sorted(tblhabc))
                                                                                        spblhabc.add(stblhabc)
                                                                                        if not stblhabc in opblhabcDict:
                                                                                            opblhabcDict[stblhabc] = []
                                                                                        opblhabcDict[stblhabc].append(tblhabc)
                                                                            for pblhabc in spblhabc:
                                                                                for iblh in (BLBL[0][pblhabc[0]]&BLBL[1][pblhabc[1]]&BLBL[2][pblhabc[2]])-compiblh:
                                                                                    #print("=================================================================================")
                                                                                    #print(len(opblcegDict[pblceg]))
                                                                                    #print(len(opblhabcDict[pblhabc]))
                                                                                    for opblceg in opblcegDict[pblceg]:       
                                                                                        for opblhabc in opblhabcDict[pblhabc]:
                                                                                            #print(opblceg, opblhabc)
                                                                                            prenews = ((((lae, xlae),        (xlga, lga),        (lah, opblhabc[0])),
                                                                                            (  (xleb, leb),        (lbg, xlbg),        (lbh, opblhabc[1])),
                                                                                            (  (opblceg[0], lec),  (opblceg[1], lgc),  (lch, opblhabc[2]))),
                                                                                            ( ((xlae, lae),        (leb, xleb),        (lec, opblceg[0]) ),
                                                                                            (  (lga, xlga),        (xlbg, lbg),        (lgc, opblceg[1]) ),
                                                                                            (  (opblhabc[0], lah), (opblhabc[1], lbh), (opblhabc[2], lch))))
                                                                                            
                                                                                            
                                                                                            counter1 += 1 
                                                                                            news = tuple(sorted((tuple(sorted((tuple(sorted(((lae, xlae), (xlga, lga), (lah, opblhabc[0])))),
                                                                                            tuple(sorted(((xleb, leb), (lbg, xlbg), (lbh, opblhabc[1])))),
                                                                                            tuple(sorted(((opblceg[0], lec), (opblceg[1], lgc), (lch, opblhabc[2]))))))),
                                                                                            tuple(sorted((tuple(sorted(((xlae, lae), (leb, xleb), (lec, opblceg[0])))), 
                                                                                            tuple(sorted(((lga, xlga), (xlbg, lbg), (lgc, opblceg[1])))), 
                                                                                            tuple(sorted(((opblhabc[0], lah), (opblhabc[1], lbh), (opblhabc[2], lch))))))))))
                                                                                            
                                                                                            if not news in testSDict:
                                                                                                testSDict[news] = []
                                                                                                testSDict[news].append(prenews)
                                                                                            else:
                                                                                                testSDict[news].append(prenews)
                                                                                                counter2 += 1
                                                                                                print("--------------------------------------------------------------------------------")
                      
                                                                                                for ts in testSDict[news]:
                                                                                                    print(ts, ibla, iblb, iblc, ible,  iblg, iblh)
                                                                                                print("--------------------------------------------------------------------------------")
                                                                                            
                                                                                            #print("--------------------------------------------------------------------------------")
                                                                                            #S.add(news)
                                                                                            #print(len(S), counter1, news)
                                                                                    #print("=================================================================================")
                                                                                    #compiblh.add(iblh)   
                                                                compiblc.add(iblc)                            
                                        compiblg.add(iblg)                                                    
                compible.add(ible)                                                                                
    compibla.add(ibla)                                                                                        
                                                                                            
def nestingbreak(counter):
    if ilgc != ilga and ilgc != ilgb:
        print("ilgc: ", ilgc)
        for ilec, lec in enumerate(FBL[ie]):
            if ilec != ilea and ilec != ileb:
                print("ilec: ", ilec)
                for xlgc in XL[lgc]:
                    print("->xlgc: ", xlgc, len(S), counter[0])
                    for xlec in XL[lec]:
                        for ilce, BLBLce in enumerate(BLBL):
                            for ilcg, BLBLcg in enumerate(BLBL):
                                if ilce != ilcg:
                                    #print("ilce: ", ilce)
                                    #print("ilcg: ", ilcg)
                                    for ic in BLBLce[xlec]&BLBLcg[xlgc]:
                                        for ilbh, lbh in enumerate(FBL[ib]):
                                            if ilbh != ilbe and ilbh != ilbg:
                                                for ilch, lch in enumerate(FBL[ic]):
                                                    if ilch != ilce and ilch != ilcg:
                                                        for xlah in XL[lah]:
                                                            for xlbh in XL[lbh]:
                                                                for xlch in XL[lch]:
                                                                    for ilha, BLBLha in enumerate(BLBL):
                                                                        for ilhb, BLBLhb in enumerate(BLBL):
                                                                            if ilha != ilhb:
                                                                                for ilhc, BLBLhc in enumerate(BLBL):
                                                                                    if ilhc != ilhb and ilhc != ilha:
                                                                                        for ih in BLBLha[xlah]&BLBLhb[xlbh]&BLBLhc[xlch]:
                                                                                             d0 = tuple(sorted((ia, ib, ic))) 
                                                                                             d1 = tuple(sorted((ie, ig, ih)))     
                                                                                                 
                                                                                             sbls = tuple(sorted((d0, d1)))
                                                                                              
                                                                                             if sbls[0] == d0:
                                                                                                 id0 = 0
                                                                                                 id1 = 1
                                                                                             else:
                                                                                                 id0 = 1
                                                                                                 id1 = 0                       
                                                                                             
                                                                                             #((FBL[ia][ilae], FBL[ie][ilea]), (FBL[ia][ilag], FBL[ig][ilga]), (FBL[ia][ilah], FBL[ih][ilha]))
                                                                                             #((FBL[ib][ilbe], FBL[ie][ileb]), (FBL[ib][ilbg], FBL[ig][ilgb]), (FBL[ib][ilbh], FBL[ih][ilhb]))
                                                                                             #((FBL[ic][ilce], FBL[ie][ilec]), (FBL[ic][ilcg], FBL[ig][ilgc]), (FBL[ic][ilch], FBL[ih][ilhc]))
                                                                                             
                                                                                             
                                                                                             #sbls[0][0][0] = (d0[0][0], d1[][]
                                                                                             
                                                                                             
                                                                                             iia, iib, iic = (-1, -1, -1)
                                                                                             for id0ibl ,d0ibl in enumerate(sbls[id0]):
                                                                                                 if ia == d0ibl and iia == -1:
                                                                                                     iia = id0ibl
                                                                                                 elif ib == d0ibl and iib == -1:
                                                                                                     iib = id0ibl 
                                                                                                 elif ic == d0ibl and iic == -1:
                                                                                                     iic = id0ibl
                                                                                             
                                                                                             iie, iig, iih = (-1, -1, -1)
                                                                                             for id1ibl ,d1ibl in enumerate(sbls[id1]):
                                                                                                 if ie == d1ibl and iie == -1:
                                                                                                     iie = id1ibl
                                                                                                 elif ig == d1ibl and iig == -1:
                                                                                                     iig = id1ibl 
                                                                                                 elif ih == d1ibl and iih == -1:
                                                                                                     iih = id1ibl
                                                                                             
                                                                                             
                                                                                             gnl[id0][iia][iie] = ilae
                                                                                             gnl[id0][iia][iig] = ilag
                                                                                             gnl[id0][iia][iih] = ilah
                                                                                             gnl[id0][iib][iie] = ilbe
                                                                                             gnl[id0][iib][iig] = ilbg
                                                                                             gnl[id0][iib][iih] = ilbh
                                                                                             gnl[id0][iic][iie] = ilce
                                                                                             gnl[id0][iic][iig] = ilcg
                                                                                             gnl[id0][iic][iih] = ilch
                                                                                             gnl[id1][iie][iia] = ilea
                                                                                             gnl[id1][iie][iib] = ileb
                                                                                             gnl[id1][iie][iic] = ilec
                                                                                             gnl[id1][iig][iia] = ilga
                                                                                             gnl[id1][iig][iib] = ilgb
                                                                                             gnl[id1][iig][iic] = ilgc
                                                                                             gnl[id1][iih][iia] = ilha
                                                                                             gnl[id1][iih][iib] = ilhb
                                                                                             gnl[id1][iih][iic] = ilhc
                                                                                             
                                                                                             s = []
                                                                                             for iid0 in range(0,3):
                                                                                                 s.append([])
                                                                                                 for iid1 in range(0,3):
                                                                                                     s[iid0].append([])
                                                                                                     s[iid0][iid1] = (FBL[sbls[0][iid0]][gnl[0][iid0][iid1]], FBL[sbls[1][iid1]][gnl[1][iid1][iid0]])
                                                                                                 s[iid0] = tuple(s[iid0])
                                                                                             
        
                                                                                             print(len(S), len(S2), counter[0], tuple(s))
                                                                                             counter[0] += 1
                                                                                             S.add(tuple(s))
                                                                                             
                                                                                             S2.add((sbls, tuple(s)))
                                                                                             #print(len(S), (sbls, rtuple(gnl)))
                                                                                             
                                                                                              
                                                                                             #print(ilea, ileb, ilec)
                                                                                             #print(ilga, ilgb, ilgc)
                                                                                             #print(ilha, ilhb, ilhc)
                                                                                              
                                                                                             #print(ilae, ilag, ilah)
                                                                                             #print(ilbe, ilbg, ilbh)
                                                                                             #print(ilce, ilcg, ilch)
                                                                                             #FBL[ie][ilea], 
                                                                                             #print(ia, ib, ic, ie, ig, ih)
                                                                                             #s.add(frozenset(((ia, (ilae, ilag, ilah)), (ib, (ilbe, ilbg, ilbh)), (ic, (ilce, ilcg, ilch)))))
                                                                                             #s.add(frozenset((frozenset(()), frozenset(()))))
        
counter = [0]

ilae, ilag, ilah = (0,1,2)
gnl = [[[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]], [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]]
for ia, bla in enumerate(FBL):
    lae, lag, lah = bla
    for xlae in XL[lae]:
        for ilea, BLBLea in enumerate(BLBL):
            for ie in BLBLea[xlae]:
                for ileb, leb in enumerate(FBL[ie]):
                    if ileb != ilea:
                        for xleb in XL[leb]:
                            for ilbe, BLBLbe in enumerate(BLBL):
                                for ib in BLBLbe[xleb]:
                                    for ilbg, lbg in enumerate(FBL[ib]):
                                        if ilbg != ilbe:
                                            print("ilbe, ilbg", ilbe, ilbg)
                                            for xlag in XL[lag]:
                                                for xlbg in XL[lbg]:
                                                    for ilga, BLBLga in enumerate(BLBL):
                                                        for ilgb, BLBLgb in enumerate(BLBL):
                                                            if ilga != ilgb:
                                                                for ig in BLBLga[xlag]&BLBLgb[xlbg]:
                                                                    print("-->ig: ", ig)
                                                                    print("-->ig: ", xlag, xlbg)
                                                                    for ilgc, lgc in enumerate(FBL[ig]):
                                                                        print("ilgc: ", ilga, ilgb, ilgc)
                                                                        nestingbreak(counter)


#        for ie in BLBL[0][xlae]|BLBL[1][xlae]|BLBL[2][xlea]:
#            for ileb, leb in enumerate(FBL[ie]):
#                if leb != xlae:
#                    for xleb in XL[leb]:
#                        for ib in BLBL[0][xleb]|BLBL[1][xleb]|BLBL[2][xleb]:
#                            for ilbg, lbg in enumerate(FBL[ib]):
#                                if lbg != xleb:
#                                    for xlbg in XL[lbg]:
#                                        if bla[1] != xlbg:
#                                            spblg = sorted((bla[1], xlbg))
#                                            for ig in BLBL[0][spblg[0]]&BLBL[1][spblg[1]]|BLBL[0][spblg[0]]&BLBL[2][spblg[1]]|BLBL[1][spblg[0]]&BLBL[2][spblg[1]]:
#                                                for 
                                    


exit()

for ia, bla3 in enumerate(FBL):
    for xbla30 in XL[bla3[0]]:
        for ie in BLBL[xbla30]:
            ble2 = delL(FBL[ie], xbla30)
            for xble20 in XL[ble2[0]]:
                for ib in BLBL[xble20]:
                    blb2 = delL(FBL[ib], xble20)
                    for xbla31 in XL[bla3[1]]:
                        for xblb20 in XL[blb2[0]]:
                            for ig in BLBL[xbla31]&BLBL[xblb20]:
                                blg1 = delL(delL(FBL[ig], bla3[1]), xblb20)
                                if set(FBL[ig]) == set((xbla31, xblb20, blg1[0])):
                                    counter1 += 1
                                    for xblg10 in XL[blg1[0]]:
                                        for xble21 in XL[ble2[1]]:
                                            for ic in BLBL[xblg10]&BLBL[xble21]:
                                                blc1 = delL(delL(FBL[ic], xblg10), xble21)
                                                if set(FBL[ic]) == set((xblg10, xble21, blc1[0])):
                                                    counter2 += 1
                                                    print(len(S), counter1, counter2)
                                                    for xbla32 in XL[bla3[2]]:
                                                        for xblb21 in XL[blb2[1]]:
                                                            for xblc10 in XL[blc1[0]]:
                                                                for ih in BLBL[xbla32]&BLBL[xblb21]&BLBL[xblc10]:
                                                                     if set(FBL[ih]) == set((xbla32, xblb21, xblc10)):
                                                                     #   S.add([[[bla3[0], xbla30], [bla3[1], xbla31], [bla3[2], xbla32]], [[xble20, ble2[0]], [blb2[0], xblb20], [blb2[1], xblb21]], [[xble21, ble2[1]], [xblg10, blg1[0]], [blc1[0], xblc10]]])
                                                                         bla = sorted((bla3[0], bla3[1], bla3[2]))
                                                                         blb = sorted((xble20, blb2[0], blb2[1]))
                                                                         blc = sorted((xble21, xblg10, blc1[0]))
                                                                         
                                                                         ble = sorted((xbla30, xbla31, xbla32))
                                                                         blg = sorted((ble2[0], xblb20, xblb21))
                                                                         blh = sorted((ble2[1], blg1[0], xblc10))

                                                                         
                                                                         abc = (((bla3[0], xbla30), (bla3[1], xbla31), (bla3[2], xbla32)), ((xble20, ble2[0]), (blb2[0], xblb20), (blb2[1], xblb21)), ((xble21, ble2[1]), (xblg10, blg1[0]), (blc1[0], xblc10)))
                                                                         egh = (((xbla30, bla3[0]), (xbla31, bla3[1]), (xbla32, bla3[2])), ((ble2[0], xble20), (xblb20, blb2[0]), (xblb21, blb2[1])), ((ble2[1], xble21), (blg1[0], xblg10), (xblc10, blc1[0])))
                                                                         S.add(frozenset((abc, egh)))
#                                                                         print(FBL[ia], FBL[ib], FBL[ic])
#                                                                         print(FBL[ie], FBL[ig], FBL[ih])
#                                                                         print(FBL[ih])
    #                                                                    print(counter1, counter2, bla3, blb2, blc1, ble2, blg1)
    #                                                                    print(counter, ia, ib, ic, ie, ig, ih)


for ia, bla in enumerate(FBL):
    for ixla0 in XL[bla[0]]:
        for ixla1 in XL[bla[1]]:
            for ixla2 in XL[bla[2]]:
                for ie in BLBL[ixla0]:
                    ble = delL(FBL[ie], ixla0)
                    for ig in BLBL[ixla1]:
                        blg = delL(FBL[ig], ixla1)
                        for ih in BLBL[ixla2]:
                            blh = delL(FBL[ih], ixla2)
                            print("--------------------------------------")
                            for le in ble:
                                for lg in blg:
                                    for lh in blh:
                                        for xle in XL[le]:
                                            for xlg in XL[lg]:
                                                for xlh in XL[lh]:
                                                    for ib in BLBL[xle]&BLBL[xlg]&BLBL[xlh]:
                                                        print(ia, ib)
                                                        print(len(S))
                                                        print(counter)
                                                        ble2 = delL(ble, xle)
                                                        blg2 = delL(blg, xlg)
                                                        blh2 = delL(blh, xlh)
                                                        for xle2 in XL[ble2[0]]:
                                                            for xlg2 in XL[blg2[0]]:
                                                                for xlh2 in XL[blh2[0]]:
                                                                    for ic in BLBL[xle2]&BLBL[xlg2]&BLBL[xlh2]:
                                                                        S.add(frozenset((frozenset((ia,ib,ic)),frozenset((ie,ig,ih)))))
                                                                        counter += 1
                            
                
#for ia, bla in enumerate(FBL):
#    for ib, blb in enumerate(FBL):
#        ic in blc in enumerate(FBL):
#            for la in bla:
#                for lb in blb:
#                    for lc in blc:
#                        for xla in XL[la]:
#                            for xlb in XL[lb]:
#                                for xlc in XL[lc]:
#                                    for         
#
#
#for ia, bl in enumerate(FBL):
#    for ib in XL[bl[0]]:
#        for ic in BLBL[ib]:
#            fblc = list(set(FBL[ic]) - {ib})
#            if len(fblc) == 0:
#                fblc = (ib, ib)
#            for ie in XL[fblc[0]]:
#                for ig in BLBL[ie]:
#                    fblg = list(set(FBL[ig]) - {ie})
#                    if len(fblg) == 0:
#                        fblg = (ie, ie)
#                    for ih in BLBL[bl[1]] & BLBL[fblg[0]]:
#                        fblh = list(set(FBL[ih]) - {bl[1],fblg[0]})
#                        if len(fblh) == 0:
#                            fblh = (bl[1],)
#                        for io in XL[fblh[0]]:
#                            for ip in BLBL[fblc[1]] & BLBL[io]:
#                                fblp = list(set(FBL[ip]) - {fblc[1],io})
#                                if len(fblp) == 0:
#                                    fblp = (io,)
#                                    for iq in XL[fblp[0]]:
#                                        for ir in BLBL[bl[2]] & BLBL[fblg[1]] & BLBL[iq]:
#                                            S.add(frozenset((frozenset((ic,ih,ir)),frozenset((ia,ig,ip)))))
#                                            printS(frozenset((frozenset((ic,ih,ir)),frozenset((ia,ig,ip)))))
#                                            
#
#
#
##                    for ih in XL[bl[1]]:
##                        for ii in  XL[fblg[0]]:
##                            for ij in  BLBL[ih] & BLBL[ii]:
##                                fblj = list(set(FBL[ij]) - {ih,ii})
##                                if len(fblj) == 0:
##                                    fblj = list(set(FBL[ij]))
##                                    print("fblj")
##                                    print(ih,ii)
##                                    print(fblj)
##                                for ik in BLBL[fblc[1]] & BLBL[fblj[0]]:
##                                    print(FBL[ik])
##                                    print(fblc[1],fblj[0])
##                                    fblk = list(set(FBL[ik]) - {fblc[1],fblj[0]})
##                                    if len(fblk) == 0:
##                                        fblk = list(set(FBL[ik]))
##                                        print(fblk)
##                                    print((ia,ig,ik))
##                                    for il in XL[fblk[0]]:
##                                        for im in BLBL[bl[1]] & BLBL[fblg[1]] & BLBL[il]:
##                                            S.add(frozenset((frozenset((ic,ij,im)),frozenset((ia,ig,ik)))))
##                                            printS(frozenset((frozenset((ic,ij,im)),frozenset((ia,ig,ik)))))

        

#for ia, la in enumerate(L):
#    for blbla in BLBL[ia]:
#        for ib in FBL[blbla]:
#            for blblb in BLBL[ia]|BLBL[ib]
            
#DL = []
#
#for ia, la in enumerate(L):
#    DL.append(set())
#    for blb in BLBL[ia]:
#        DL[ia] |= set(FBL[blb])
#
#
#print(DL)
#print(len(DL))
#
#print(DL[0].intersection(DL[270]))

#    for ib, blb in enumerate(BLBL[ia]):
#        for lc in blb:
#          
#
#
#for ia, la in enumerate(L):
#    for ib, lb in enumerate(BLBL[la]):

#tBL = list(BL)

#import copy

#PBL = []

#for ia, bla in enumerate(tBL):
#    pbl = []
#    
#    for l in bla:
#        pbl.append(list(l))
#        
#    if
#
#    if len(bl[0]) == 1:
#
#        t = bla.pop()
#        pbl = (t,t,t)
#
#    for 
#    PBL.append



#print(BL)
#print(len(BL))

#BLBL = []
#
#for ia, bl in enumerate(BL):
#    bl[0]

#                for ig in L[bl[0]i]:
#                    for ih in DSL[ig]:
#                        for ij in DSL[

#for ia, qdla in enumerate(QDL):
#    for ib in qdla:
#        for ic in QDL[ib]:
#            if ia in QDL[ic]:
#                for sla in L[ia]:
#                    found = False
#                    for slb in L[ib]:
#                        for slc in L[ic]:
#                            if len(LBSL[sla].intersection(LBSL[slb]).intersection(LBSL[slc])) == 1:
#                                BL.add(frozenset((ia,ib,ic)))
#                                found = True
#                                break
#                        if found:
#                            break
#                    if not found:
#                        break



#
#            for ie in QDL[ic]:
#                if ia == ie:
#                
#
#
#    for qdlb in QDL:
#        for qdlc in QDL:
#            
#
#for ia, qdla in enumerate(QDL):
#    fina.add(ia)
#    for ib in qdla.difference(fina):
#        for ic in qdla:
#            for ie in QDL[ic]:
#                if ie == ib:
#                    BL.add(frozenset((ia, ib, ic)))
#                    if len(frozenset((ia,ib,ic))) < 3:
#                        print((ia, ib, ic))
#                        printl(ia)
#                        printl(ib)
#                        printl(ic)
#                    

#print(BL)
#print(len(BL))


#for bl in BL:
#    print(bl)
#    for l in bl:
#        printl(l)

#        for ic, qdlc in enumerate(QDL):
#            for ie in qdlc:
#                for ig in QDL[ie]:
#                    
#
#    for ib in QDL[ia]:
#        
#
##
##    for qdlb in QDL[qdla]:
##        if QDL[qdlb].intersection(QDL[qdla]):
#            print(qdla)
#
#
#    print(qdla)
#    for sl in L[qdla]:
#        print(SL[sl])


#    for sla in la:
#        list(sla)
#        for qdslb in DSL[sla]:
#            for slb in la.difference(set((sla))):
#                
#        DSL[qdslb].intersection(DSL[la.difference(set((sla))])
#            for dslc in 
#for ia, la in enumerate(L):
#    for ib in IL[ia]:
#        if ib >= ia:
#            for ic in IL[ia].intersection(IL[ib]):
#                if ic >= ib:
#                    BL.append(frozenset((ia, ib, ic)))
            

#print(BL)
#print(len(BL))

#def box_matches (l1):
#    matches = set()
#
#    for l2 in L:
#        test = True
#        for sl1 in l1:
#          for sl2 in l2:
#              if len(sl1.difference(sl2)) != 2:
#                  test = False
#        if test:
#            matches.add(l2)
#
#    return matches

def l_by_sl(sl):
    matches = set()

    for i, l in enumerate(L):
        if sl in l:
            matches.add(i)

    return matches

#for ia, la in enumerate(L):
#    for sl in la:
#        for lb in l_by_sl(sl)
            


#for sl in SL: 
#    print(sl)
#    print(len(l_by_sl(sl)))
#    print(l_by_sl(sl))

BL = set()

#for la in L:
#    for lb in L:
#        testa = True
#
#        for sla in la:
#            testb = False
# 
#            for slb in lb:
#                if sla.isdisjoint(slb):
#                    testb = True
#            if not testb:
#                testa = False
#                
#        if testa:
#            for lc in L:
#            
#                for sla in la:
#                    for slb in lb:
#                        for slc in lc:
#                            if frozenset((sla,slb,slc)) in L:
#                                BL.add(frozenset((la,lb,lc)))


for la in L:
    for lb in L:
        for lc in L:
            testa = True
            for sla in la:
                testb = False
                for slb in lb:
                    for slc in lc:
                        if frozenset((sla, slb, slc)) in L:
                            testb = True
                    
                if not testb:
                    testa = False
                    
            if testa:
                BL.add(frozenset((la,lb,lc)))
    break

#print(BL)
#print(len(BL))

#for l in L:
 #   print(l)
  #  m = matches(l)
#    print(len(m))
 #   print(m)
