#!/usr/bin/env python
# encoding: utf-8

from cota import*
import time


betV=0.00000001
bet =float('{0:.8f}'.format(betV))
bal  =0.00017000
bals=float('{0:.8f}'.format(bal))
Gbal =0.00000000
Gbals=float('{0:.8f}'.format(Gbal))
w='v'
i=0
u=0
o=0
ttt=0
tuu=0
hi=0
lw=0
tc=[0,1,2,3]
ic=0
ci=0
ts=0
keed=string.ascii_letters+string.digits
lbb=[0,0,0,0,0,0,0,0,0]
lcc='U'*40
bb=''
ki=0
ooo =50.399
uuu =49.600
mmm =1
eel =[0,1,2,3,4,5,6,7]
eet =[0,1,2,3,4,5,6,7]
last=[]
eq=[0.00000100]
ep=0.00000100
leq=0
pay=2
sjm=[1.00000100]
smm=0.00000001
ti=0
wag=0
ww=[]
poz=0
while True:
  if u>1 and u%2==0:
       ci=ci+1
  if u==1:
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
     tc=[0,1,2,3]
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
  zzz = cota.bsim(seed,ttt)
  #print(s,i,ts)
  m=randint(0,2)
  n=randint(0,2)
  #print(ep[-1]<eq[-1],ep[-1],eq[-1])
  ####################
  eq.append(round(bal,8))
  eq.sort()
  if len(eq)==3:
     eq.remove(eq[0]) 
  if ep>=(eq[-1]):
      betV=bal*0.0002
      poz=3
      ti=0
      mid=''
  con=ww.count('l')
  if w=='l' :#and ep[-1]<eq[-1]:#and u%2==1:#and ii<4:
    pay =3#round(2+(0.1*u),2)
    betV=betV+((betV*ti)/3)#(sum(sjm)*(1/(pay-1)))
    bet =float('{0:.8f}'.format(betV))
    sjm.append(bet)
    ti=0
    bett=betV
  if w=='v' :#and ep[-1]<eq[-1]:#and u%2==1:#and ii<4:
    pay =3#round(2+(0.1*u),2)
    betV=betV+((betV*ti)/3)#(sum(sjm)*(1/(pay-1)))
    bet =float('{0:.8f}'.format(betV))
    sjm.append(bet)
    ti=0
  if len(ww)==2 and con>=1:#and con>3 :
    #tm  =abs(((eq[-1]*0.98)-ep[-1])/(betV*con))
    ti=ti+1
    betV=round(((eq[-1])-ep)*1.1,8)#(betV*con)
    bet =float('{0:.8f}'.format(betV))
    pay =2
    ts  ='jj'
    #print(bet)
  if len(ww)>=2:
     ww=[]
  # if u>=3 :#and ep[-1]<eq[-1]:#and u%2==1:#and ii<4:
    # pay =2#round(2+(0.1*u),2)
    # betV=round(((eq[-1])-ep)*0.55,8)#(sum(sjm)*(1/(pay-1)))
    # bet =float('{0:.8f}'.format(betV))
    # sjm.append(bet)
    # ti=0
      #print('ok')
  #print(ep,(eq[-1]))
  if bal<betV  :
          print(('{0:.8f}'.format(wag)))
          break	
  #####################
  while True:
    clt=''
    bool=''
    dd=''
    trr=(int(ttt//500))%2
    if bb=='o':next='u'
    if bb=='u':next='o'
    if i%2==0:
           rrr=randint(5,15)
    if i%2==1:
           rrr=randint(30,40)
##########
    if pay<2:
         ooo =round(100-(((100/pay)/100)*99.2),3)
         uuu =round(((100/pay)/100)*99.2,3)
         mmm =round(abs(pay-1),2)
    if pay==2:
         ooo =50.399
         uuu =49.600
         mmm =round(abs(pay-1),2)
    if pay>2:
         ooo =round(100-(((100/pay)/100)*99.2),3)
         uuu =round(((100/pay)/100)*99.2,3)
         mmm =round(abs(pay-1),2)
    clt,bool,dd=cota.brx(seed,ttt,u,last,ic,ts,ti,lcc,zzz)#bun(seed,ttt,u)#
    # if u>=6:
       # bool='over'
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
    wag=wag+betV
    # if bal>=0.00003000:
          # Gbal=Gbal+(bal-0.00001000)
          # Gbals=('{0:.8f}'.format(Gbal))
          # bal =0.00001000
    # if bal<betV and Gbal>0.00001000:
           # bal =0.00001000
           # Gbal=Gbal-bal
           # Gbals=('{0:.8f}'.format(Gbal))
    #print('lcc',lcc)
    if bool=='over' :#and fll not in lbb:#and len(str(clt))!=lcc :#and len(clt)!=lbb:
           lbb.append(fll)
           del lbb[0]
           lcc=clt
           ttt=ttt+1
           hi=hi+1
           lw=0
           bb='o'
           if dn>ooo:
                 o=o+1
                 u=0
                 w='v'
                 #ww.append(w)
                 bal=bal+(bet*mmm)
                 ep=round(bal,8)
                 bals=('{0:.8f}'.format(bal))
                 betC=('{0:.8f}'.format(betV))
                 print('okkkkkkkkk','ov',ttt,'/',tuu,s,' ',clt,(' '*(39-len(clt))),dn,ooo,bals,'*',betC,'*',Gbals)
                 last=[]
                 break
           if dn<=ooo:
                 tuu=tuu+1
                 u=u+1
                 o=0
                 w='l'
                 ww.append(w)
                 bal=bal-bet
                 ep=round(bal,8)
                 bals=('{0:.8f}'.format(bal))
                 betC=('{0:.8f}'.format(betV))
                 print('noooo----'+str(u),'ov',ttt,'/',tuu,s,' ',clt,(' '*(39-len(clt))),dn,ooo,bals,'*',betC,'*',Gbals)
                 last.append(clt)
                 break
    if bool=='under'   :#and fll not in lbb :#and len(str(clt))!=lcc :#and len(clt)!=lbb:
           lbb.append(fll)
           del lbb[0]
           lcc=clt
           ttt=ttt+1
           lw=lw+1
           hi=0
           bb='u'
           if dn<=uuu:
                 o=o+1
                 u=0
                 w='v'
                 #ww.append(w)
                 bal=bal+(bet*mmm)
                 ep=round(bal,8)
                 bals=('{0:.8f}'.format(bal))
                 betC=('{0:.8f}'.format(betV))
                 print('okkkkkkkkk','un',ttt,'/',tuu,s,' ',clt,(' '*(39-len(clt))),dn,uuu,bals,'*',betC,'*',Gbals)
                 last=[]
                 break
           if dn>uuu:
                 tuu=tuu+1
                 u=u+1
                 o=0
                 w='l'
                 ww.append(w)
                 bal=bal-bet
                 ep=round(bal,8)
                 bals=('{0:.8f}'.format(bal))
                 betC=('{0:.8f}'.format(betV))
                 print('noooo----'+str(u),'un',ttt,'/',tuu,s,' ',clt,(' '*(39-len(clt))),dn,uuu,bals,'*',betC,'*',Gbals)
                 last.append(clt)
                 break
  if bal<betV  :
          print(('{0:.8f}'.format(wag)))
          break		  
  # if u==9:
     # break
	 
