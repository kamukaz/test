#!/usr/bin/env python
# encoding: CP1252

from hashing import*
from difflib import SequenceMatcher
from collections import Counter
from random import randint
import winsound
from math import log,frexp,fmod,cos,sin
from deco import*
from decimal import*

##############################################
def bix(seed,u,rrr,eee):		
       h=seed
       d=[int(h,i) for i in range(16,37)]
       F=[(bin(int(x,16)))[2:] for x in re.split(r'(\w{2})', seed) if x]
       sd=sum(d)
       md=sum(d)/len(d)
       hx=(hex(int(md)))[2:]
       ls=[]
       fff=''
       yi=2
       zi=3
       eee=randint(0,9)
       cc='0'*34
       fg = [0, 9, 10, 19, 20, 29, 30, 39, 40, 49, 50, 59, 60, 69, 70, 79, 80, 89, 90, 99]
       while True:
           lrc=[]
           z=pwd.ran(40)
           f=pwd.sha2(z)
           x=pwd.resu(f,' '*256)
           y=pwd.resu(h,' '*256)
           r=[int(h,i) for i in range(16,37)]
           sr=sum(d)
           mr=sum(d)/len(d)
           hz=(hex(int(mr)))[2:]
           # for i in range(63):
               # if h[i:i+zi]==f[i:i+zi]:
                   # lrc.append(f[i:i+zi])
           if hz[:16]==hx[:16] and f[1]==h[1]:#len(lrc)>=yi and len(lrc[0])==len(lrc[-1])==zi :#
                 ls.append(z)
                 #print(lrc)
           if len(ls)==3:
                     break
       fff=	ls[0]	
       ul=[]
       ol=[]
       while True:
            un=[]
            ov=[]
            al1=[]	   
            al2=[]	   
            unf=[]
            ovf=[]
            el = pwd.zum(7)
            lr1=[]#random.choice([pwd.rand(34),pwd.upd(34),pwd.lod(34)])#pwd.rand(34)#'0'*randint(5,34)#
            lr2=[]#random.choice([pwd.rand(34),pwd.upd(34),pwd.lod(34)])#pwd.rand(34)#'0'*randint(5,34)#
            while True:
                  lk  =pwd.lod(randint(5,34))
                  lr = pwd.sha2(lk)
                  lx = (pwd.sha2(lk))[:5]
                  lw = len([ i for i in lr[:5]+lr[-5:] if i.islower()])
                  lv = pwd.resuv(lk,'')
                  if  lw>=7 :#(lx[0]).islower() and (lx[1]).islower() and (lx[2]).islower() and
                        lr1.append(lk)
                  if len(lr1)==2:
                        break
            while True:
                  lk  =pwd.lod(randint(5,34))
                  lr = pwd.sha2(lk)
                  lx = (pwd.sha2(lk))[:5]
                  lw = len([i for i in lr[:5]+lr[-5:] if i.islower()])
                  lv = pwd.resuv(lk,'')
                  if  lw>=7 :#(lx[0]).islower() and (lx[1]).islower() and (lx[2]).islower() and
                        lr2.append(lk)
                  if len(lr2)==2:
                        break
            l1=lr1#[lr1[1],lr1[-1]]
            l2=lr2#[lr2[0],lr2[-1]]
            # lky = pwd.resu(l,'')
            # lfri = (lky - ((lky // 100000) * 100000)) // 1000
            # lzi = pwd.resu(z,l)
            # lz = (lzi - ((lzi // 100000) * 100000)) // 1000
            # ggg= pwd.resuv(seed,' '*256)
            for item in ls:
               for jtem in l1:
                  ky = pwd.resu(item,jtem)
                  fri = (ky - ((ky // 100000) * 100000)) // 1000
                  fbi=str(bin(int(item+jtem,36)))
                  if 50<=fri :#and fbi[-50:]=='1'*32:
                     ov.append(fri)
            if len(ov)>=5:##############################################################
                   for K in l1:ol.append(K)
            for itm in ls:
               for jtm in l2:
                  ky = pwd.resu(itm,jtm)
                  fri = (ky - ((ky // 100000) * 100000)) // 1000
                  fbi=str(bin(int(itm+jtm,36)))
                  if fri<50 :#and fbi[-50:]=='1'*32:
                     un.append(fri)
            if len(un)>=5:##############################################################
                   for k in l2:ul.append(k)
            # for item in ls:
               # for jtem in l1:
                  # ky = pwd.resu(item,jtem)
                  # fri = (ky - ((ky // 100000) * 100000)) // 1000
                  # fbi=str(bin(int(item+jtem,36)))
                  # if fri>=50:
                      # al1.append(fri)
            # for item in ls:
               # for jtm in l2:
                  # ky = pwd.resu(item,jtm)
                  # fri = (ky - ((ky // 100000) * 100000)) // 1000
                  # fbi=str(bin(int(item+jtm,36)))
                  # al2.append(fri)
                  # if fri<50:
                      # al2.append(fri)
            #eee=randint(0,11)#pwd.resuv(pwd.ran(64),'')
            if len(ol)>=1 and (u%8==0 or u%8==1 or u%8==3):#and u%3==0:
                  bool='over'
                  #print(ol)
                  l=random.choice(l1)
                  break
            if len(ul)>=1 and (u%8==4 or u%8==5 or u%8==7):#and (u%3==1 or u%3==2):
                  bool='under'
                  # print(ul)
                  l=random.choice(l2)
                  break
            if len(ol)>=1 and u%8==2:#and u%3==0:
                  bool='under'
                  #print(ol)
                  l=random.choice(l1)
                  break
            if len(ul)>=1 and u%8==6:#and (u%3==1 or u%3==2):
                  bool='over'
                  # print(ul)
                  l=random.choice(l2)
                  break
       return(l,bool,fff)		


##############################################
def bjx(seed,uuu,rrr,sss):		
       hs=seed
       bn=('0'*64+(bin(int(hs,16)))[2:])[:256]
       t=[x for x in re.split(r'(\w{32})', bn) if x]
       a=t[0]
       b=t[1]
       c=t[2]
       d=t[3]
       e=t[4]
       f=t[5]
       g=t[6]
       h=t[7]
       dc={}
       for i in range(32):
           j='A'+str(i)
           dc[j]=[a[i],b[i],c[i],d[i],e[i],f[i],g[i],h[i]]
       vdc=[ dc[i] for i in dc]
       tdc=[tuple(v) for v in vdc]
       while True:
           z=pwd.ran(40)
           hz=pwd.sha2(z)
           bn=('0'*64+(bin(int(hz,16)))[2:])[:256]
           t1=[x for x in re.split(r'(\w{32})', bn) if x]
           a1=t1[0]
           b1=t1[1]
           c1=t1[2]
           d1=t1[3]
           e1=t1[4]
           f1=t1[5]
           g1=t1[6]
           h1=t1[7]
           ds={}
           for i in range(32):
               j='A'+str(i)
               ds[j]=[a1[i],b1[i],c1[i],d1[i],e1[i],f1[i],g1[i],h1[i]]
           st={n: dc[n] for n in dc if n in ds and dc[n] == ds[n] }
           vds=[ ds[i] for i in ds]
           tds=[tuple(v) for v in vds]
           dcs=set(tds).intersection(tdc)
           ku=list(st)
           #print(ku)
           ku1=0
           ku2=0
           ku.sort()
           if len(ku)>=2:
               ku1=int((ku[0])[1:])
               ku2=int((ku[-1])[1:])
           if len(st)>=3:
              #€print(ku1,ku2)
              break		   
		   
       ul=[]
       ol=[]
       # ls=['auRpxTjiLTPAuYZS8leejDbbqiz2LyoFIyuhHhjR','CbABwxcrezilwnJKbpDOiBkdxQuyiji9eMpvaFb3','PHkDjqQsTX2bjgvGJHbi0hOamQTnC5jgwQwLGQis','hJILrvELZTapMVFbTWc9YJmjlGgZZAlitNEbW1Cw','fE6Q4O4exgpmxEoqRmGcyJtpTfj4cdi2cyHf5tO5','CQqzVdKeS2C3tFu1UpJNNaM8wD6g3FjJZuAiuMfR','Mil6kCvokNfBeBJfmieGt8KjbyX4nJQg9qIjrr3S','GH6NsKsyhyAtEa9fXdNI4bLk1ymt8pEKBjDNfm7f','Sx0Cgm2iuT61d2pzO6u0yyr5AxNymPcvp5yfiPkf','Q9rHnXLaUAI9FUZyv0n2MKEpeYOJIWqi6TtIyxZc']
       while True:
            un=[]
            ov=[]
            al1=[]	   
            al2=[]	   
            unf=[]
            ovf=[]
            oo=[0,11,22,33,44,55,66,77,88,99]
            ff=pwd.rum(2)
            fl=ff.lower()
            while True:
                q=pwd.ran(34)#+random.choice([pwd.num(5),pwd.zum(5),pwd.upd(5),pwd.lod(5),pwd.ran(5)])
                hq=pwd.sha2(q)
                bn=('0'*64+(bin(int(hq,16)))[2:])[:256]
                t1=[x for x in re.split(r'(\w{32})', bn) if x]
                a1=t1[0]
                b1=t1[1]
                c1=t1[2]
                d1=t1[3]
                e1=t1[4]
                f1=t1[5]
                g1=t1[6]
                h1=t1[7]
                ds={}
                for i in range(32):
                    j='A'+str(i)
                    ds[j]=[a1[i],b1[i],c1[i],d1[i],e1[i],f1[i],g1[i],h1[i]]
                st={n: dc[n] for n in dc if n in ds and dc[n] == ds[n]}
                vds=[ ds[i] for i in ds]
                tds=[tuple(v) for v in vds]
                dcs=set(tds).intersection(tdc)
                rz=pwd.resuv(z,q)
                rq=pwd.resuv(q,'')
                gu=list(st)
                #print(ku)
                gu1=0
                gu2=0
                gu.sort()
                if len(gu)>=2:
                      gu1=int((gu[0])[1:])
                      gu2=int((gu[-1])[1:])
                if  len(st)>=3:	   
                          break
            # for item in ls:
                  # ky = pwd.resu(item,q)
                  # fri = (ky - ((ky // 100000) * 100000)) // 1000
                  # fbi=str(bin(int(item+q,36)))
                  # if 50<=fri :#and fbi[-50:]=='1'*32:
                     # ov.append(fri)
            # for itm in ls:
                  # ky = pwd.resu(itm,q)
                  # fri = (ky - ((ky // 100000) * 100000)) // 1000
                  # fbi=str(bin(int(item+q,36)))
                  # if fri<50 :#and fbi[-50:]=='1'*32:
                     # un.append(fri)
            mmm= 'ªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªª'
            nnn= 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU'
            rm = pwd.resuv(mmm,q)
            rn = pwd.resuv(nnn,q)
            rl = pwd.resuv(sss,q)
            #if uuu<1:
            if 50<rz and 60<rn and 10>abs(rm==rn) and 60<rl:#and uuu%4==0:
                  bool='over'
                  l=q
                  break
            if rz<50 and rn<60 and abs(rm-rn)<10 and 40>rl:#and uuu%4==1:
                  bool='under'
                  l=q
                  break
            # if uuu>=1:
            # if 50>rz and 50>rq and rl>50 and uuu%4==2:
                  # bool='over'
                  # l=q
                  # break
            # if 50<rz and 50<rq and rl<50 and uuu%4==3 :
                  # bool='under'
                  # l=q
                  # break
       return(l,bool,z)
	   
##############################################
def bsx(seed,uuu,rrr,sss):		
       hs=seed
       while True:
           lrc=[]
           z=pwd.ran(40)
           hz=pwd.sha2(z)
           x=6
           y=3
           sh='**'
           zh='**'
           for i in range(63-x):
             if hs[i:i+x] in hz or hz[i:i+x] in hs:
                        sh=hs[i:i+x]
                        zh=hz[i:i+x]
           if zh in hs or sh in hz:#hs[:3]==hz[:3]:
              # print(hs,sh)		   		   
              # print(hz,zh)		   		   
              break		   		   
       while True:
            while True:
                q=pwd.ran(34)#+random.choice([pwd.num(5),pwd.zum(5),pwd.upd(5),pwd.lod(5),pwd.ran(5)])
                hq=pwd.sha5(q)
                rz=pwd.resuv(z,q)
                rq=pwd.resuv(q,'')
                if  hq[:2]=='cb' :	   
                          break
                if  hq[:2]=='cf' :	   
                          break
            mmm= 'ªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªª'
            nnn= 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU'
            rm = pwd.resuv(mmm,q)
            rn = pwd.resuv(nnn,q)
            if 50<rz :#and 50<rn and 50<rm:
                  bool='over'
                  l=q
                  break
            if 50>rz :#and 50>rn and 50>rm:
                  bool='under'
                  l=q
                  break

       return(l,bool,z)
