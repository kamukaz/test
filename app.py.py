#!/usr/bin/env python
# encoding: utf-8

from cota import*
import time


betV=0.00000100
bet =float('{0:.9f}'.format(betV))
bal=0.00117943
bals=('{0:.9f}'.format(bal))
w='v'
i=0
u=0
o=0
ttt=0
tuu=0
hi=0
lw=0
tc=[0,1,2]
ic=0
ci=0
#ts=0
keed=string.ascii_letters+string.digits
lbb=[0,0,0,0,0,0,0,0,0]
lcc=0
bb=''
ki=0
ooo =50.399
uuu =49.600
mmm =1
eel =[0,1,2,3,4,5,6,7]
eet =[0,1,2,3,4,5,6,7]
last=['0']
while True:
  if u==1:
       ci=ci+1
  if ttt%15==0:
       ic=ic+1
  # time.sleep(1)
  #keed=pwd.rum(1)+pwd.zum(1)
  i=i+1
  ki=ki+1
  if ki==63:
     ki=0
  k1=ki
  k2=ki+3
  if len(tc)==0:
     tc=[0,1,2]
  # if ci%2==0:
  ts=random.choice(tc)
  tc.remove(ts)
  if len(eel)==0:
     eel=[0,1,2,3,4,5,6,7]
  # if ci%2==0:
  eee=random.choice(eel)
  eel.remove(eee)
  if len(eet)==0:
     eet=[0,1,2,3,4,5,6,7]
  # if ci%2==0:
  ee=random.choice(eet)
  eet.remove(ee)
  s   = pwd.ran(40)
  seed= pwd.sha2(s)
  #print(s,i,ts)
  m=randint(0,2)
  n=randint(0,2)
  if len(last)==3:
     last.remove(last[0])
     last.remove(last[1])
  while True:
    if w=='v':
        betV=bal*0.0005#0.00000050#bal*0.0005
        bet =float('{0:.8f}'.format(betV))
    if w=='l' :#and u%2==1:#and ii<4:
        betV=betV*2
        bet =float('{0:.8f}'.format(betV))
        ooo =50.399
        uuu =49.600
        mmm =1
    # if ttt%8==0: betV=0.00000050
    # if ttt%8==1: betV=0.00000100
    # if ttt%8==2: betV=0.00000200
    # if ttt%8==3: betV=0.00000400
    # if ttt%8==4: betV=0.00000800
    # if ttt%8==5: betV=0.00000400
    # if ttt%8==6: betV=0.00000200
    # if ttt%8==7: betV=0.00000100
    # bet =float('{0:.8f}'.format(betV))
    # ooo =60.319
    # uuu =39.680
    # mmm =1.5
    clt=''
    bool=''
    dd=''
    trr=(int(ttt//500))%2
    if bb=='o':next='u'
    if bb=='u':next='o'
    sss=last[-1]
    if i%2==0:
           rrr=25
    if i%2==1:
           rrr=34
    clt,bool,dd=cota.bsx(seed,ttt,u,sss)
    # if 1==1:
          # if u<2 :
             # clt,bool,dd=cota.bjx(seed,ttt,rrr)
          # if u>=2 :
             # clt,bool,dd=cota.bix(seed,ttt,rrr)
          # if ts==2:
             # clt,bool,dd=cota.box(seed,u)
    # boool='overunder'
    # booool='overunder'
    # # if ci%6<=4 :
    # if eee>4:
         # bool=boool.replace(bool,'')
    # if eee<=4:
        # bool=bool
    # if ci%6>4 :
        # bool=bool
    cl = pwd.resu(clt,'')
    fll=(cl -((cl//100000)*100000))//10000
    cll=(cl -((cl//100000)*100000))/1000
    rn=pwd.resl(s,clt)
    dn=(rn -((rn//100000)*100000))/1000
    rdn=pwd.resl(dd,clt)
    ddn=(cl -((cl//100000)*100000))/10000
    clf=str(cl)
    lcl=[int(i) for i in clf]
    lcl.sort()
    # if o>=4:bool=booool.replace(bool,'')
    if bool=='over' :#and len(str(clt))!=lcc  :#and fll not in lbb:#and len(str(clt))!=lcc :#and len(clt)!=lbb:
           lbb.append(fll)
           del lbb[0]
           lcc=len(str(clt))
           ttt=ttt+1
           hi=hi+1
           lw=0
           bb='o'
           if dn>ooo:
                 o=o+1
                 u=0
                 w='v'
                 bal=bal+(bet*mmm)
                 bals=('{0:.8f}'.format(bal))
                 print('okkkkkkkkk','ov',ttt,'/',tuu,s,'   ',clt,(' '*(39-len(clt))),dn,cll,bals,'*',int(bet*10**8),'*')
                 break
           elif dn<=ooo:
                 tuu=tuu+1
                 u=u+1
                 o=0
                 w='l'
                 bal=bal-bet
                 bals=('{0:.8f}'.format(bal))
                 print('noooo----'+str(u),'ov',ttt,'/',tuu,s,'   ',clt,(' '*(39-len(clt))),dn,cll,bals,'*',int(bet*10**8),'*')
                 last.append(s)
                 break
    if bool=='under':# and len(str(clt))!=lcc  :#and fll not in lbb :#and len(str(clt))!=lcc :#and len(clt)!=lbb:
           lbb.append(fll)
           del lbb[0]
           lcc=len(str(clt))
           ttt=ttt+1
           lw=lw+1
           hi=0
           bb='u'
           if dn<=uuu:
                 o=o+1
                 u=0
                 w='v'
                 bal=bal+(bet*mmm)
                 bals=('{0:.8f}'.format(bal))
                 print('okkkkkkkkk','un',ttt,'/',tuu,s,'   ',clt,(' '*(39-len(clt))),dn,cll,bals,'*',int(bet*10**8),'*')
                 break
           elif dn>uuu:
                 tuu=tuu+1
                 u=u+1
                 o=0
                 w='l'
                 bal=bal-bet
                 bals=('{0:.8f}'.format(bal))
                 print('noooo----'+str(u),'un',ttt,'/',tuu,s,'   ',clt,(' '*(39-len(clt))),dn,cll,bals,'*',int(bet*10**8),'*')
                 last.append(s)
                 break
				 
  if bal<=betV:
          break	
  # if u==9:
     # break