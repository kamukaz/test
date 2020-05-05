#!/usr/bin/env python
# encoding: CP1252

from hashing import*
from difflib import SequenceMatcher
from collections import Counter
from random import randint
from math import log,frexp,fmod,cos,sin
from decimal import*

class cota():
    def lesto(seed):
        bool=''
        hs=seed
        kr=int(hs,16)
        ar=re.sub("\d", "x", hs)
        br=re.sub("[a-f]","y",ar)
        tr=re.sub("[0-9,a,b,d-f]","y",hs)
        lns=int(hs,16)
        lnss=str(int(hs,16))
        mr,nr=divmod(kr,64)
        cx,cy=frexp(kr)
        rmk=[]
        y=2
        z=3
        while True:
           lrt=[]
           lrc=[]
           hr =str(kr)
           b=pwd.ran(40)
           hc=pwd.sha2(b)
           lnb=int(hc,16)
           lnbs=str(int(hc,16))
           # kx=int(hc,16)
           # vx,vy=frexp(kx)
           # p  = pwd.resu(b,'')
           # dp = (p -((p//100000)*100000))//1000
           # ax=re.sub("\d", "x", hc)
           # bx=re.sub("[a-f]","y",ax)
           # tx=re.sub("[0-9,a,b,d-f]","y",hc)
           # mx,nx=divmod(kx,64)
           # for i in range(63):
            # if str(hc)[i:i+z]==str(hs)[i:i+z]:
              # lrc.append(str(hc)[i:i+z])
           if len(lnss)==len(lnbs) :#and lnss[:3]==lnbs[:3]:#len(lrc)>=y and len(lrc[0])==len(lrc[-1])==z :
                  break
        #print('ok')
        while True:
            l=pwd.ran(randint(5,34))
            hl=pwd.sha2(l)
            lky = pwd.resu(l,'')
            bk  =str(lky)
            lfri = (lky - ((lky // 100000) * 100000)) // 1000
            lnc=int(hl,16)
            lncs=str(int(hl,16))
            ky = pwd.resu(b,l)
            fri = (ky - ((ky // 100000) * 100000)) // 1000
        #########################
            if fri>50 and len(lnss)==len(lncs) and len(bk)>6 and bk.count('0')>=2:
                       bool='over'
                       break
            if fri<50 and len(lnss)==len(lncs) and len(bk)<5 and bk.count('0')>=2:
                       bool='under'
                       break 					   
        return(l,bool)
##############################################
    def ltt(seed):
        bool=''
        hs=seed
        while True:
            ts=randint(5,34)
            f=pwd.ran(randint(30,50))
            hc=pwd.sha2(f)
            hcm=pwd.sha2(hc)
            hcm1=pwd.sha2(hcm)
            hl=pwd.sha2(hs)
            hl1=pwd.sha2(hl)
            l=pwd.ran(ts)
            rs=pwd.resu(f,l)
            rss= (rs - ((rs // 100000) * 100000)) // 1000
            res=pwd.resu(l,'')
            ress= (res - ((res // 100000) * 100000)) // 1000
            clf=str(res)
            lcl=[int(i) for i in clf]
            lcl.sort()
            if  hc[:2]==hs[:2] :#and len(str(rs))==6 and len(str(res))==6:#and hcm[1]==hl[1] :#and len(str(rs))==6 and len(str(res))==6:#hc[1]==hs[1] and hcm[1]==hl[1] and hcm1[1]==hl1[1]
                if rss>=51 and ress>=51:
                       bool='over'
                       break 					   
                if rss<49 and ress<=49:
                       bool='under'
                       break 					   
        return(l,bool,f)
##############################################
    def lto(seed):
        bool=''
        hs=seed
        while True:
            ts=randint(5,34)
            f=pwd.ran(randint(30,40))
            hc=pwd.sha2(f)
            hcm=pwd.sha2(hc)
            hcm1=pwd.sha2(hcm)
            hl=pwd.sha2(hs)
            hl1=pwd.sha2(hl)
            l=pwd.ran(ts)
            rs=pwd.resu(f,l)
            rss= (rs - ((rs // 100000) * 100000)) // 1000
            res=pwd.resu(l,'')
            ress= (res - ((res // 100000) * 100000)) // 1000
            clf=str(res)
            lcl=[int(i) for i in clf]
            lcl.sort()
            if hc[:2]==hs[:2] :#and len(str(rs))==6 and len(str(res))==6:#and hcm[1]==hl[1] :#and len(str(rs))==6 and len(str(res))==6:
                if rss>=51 and lcl[1]>=4 and (lcl[0]==0 or lcl[0]>=4):#and ress>=51:
                       bool='over'
                       break 					   
				   
        return(l,bool,f)
##############################################
    def ltu(seed):
        bool=''
        hs=seed
        while True:
            ts=randint(5,34)
            f=pwd.ran(randint(30,40))
            hc=pwd.sha2(f)
            hcm=pwd.sha2(hc)
            hcm1=pwd.sha2(hcm)
            hl=pwd.sha2(hs)
            hl1=pwd.sha2(hl)
            l=pwd.ran(ts)
            rs=pwd.resu(f,l)
            rss= (rs - ((rs // 100000) * 100000)) // 1000
            res=pwd.resu(l,'')
            ress= (res - ((res // 100000) * 100000)) // 1000
            clf=str(res)
            lcl=[int(i) for i in clf]
            lcl.sort()
            if hc[:2]==hs[:2] :#and len(str(rs))==6 and len(str(res))==6:#and hcm[1]==hl[1] :#and len(str(rs))==6 and len(str(res))==6:					   
                if rss<49 and 0<lcl[-1]<=6:#and ress<=49:
                       bool='under'
                       break 
					   
        return(l,bool,f)
##############################################
    def ltw(seed):
        bool=''
        hs=seed
        fs=str(int(hs,16))
        bs=(bin(int(fs)))[2:]
        while True:
            f=pwd.ran(40)
            hc=pwd.sha2(f)
            fc=str(int(hc,16))
            bc=(bin(int(fc)))[2:]
            if  bc[:4]==bs[:4] and bc[-4:]==bs[-4:] and hc[0]==hs[0] and hc[-1]==hs[-1] :#and hc[0]==hs[0] and hc[-1]==hs[-1]:
                break
        while True:
            l=random.choice([pwd.rand(random.choice([8,16,24])),pwd.ran(random.choice([8,16,24])),pwd.num(random.choice([8,16,24]))])
            rs=pwd.resu(f,l)
            rss= rs//1000#(rs - ((rs // 100000) * 100000)) // 1000
            res=pwd.resu(l,'')
            ress= res//1000#(res - ((res // 100000) * 100000)) // 1000
            clf=str(res)
            lcl=[int(i) for i in clf]
            lcl.sort()
            #and fc[0]==fs[0] and fc[-1]==fs[-1] 
            if rss>=750 and ress>=750 and ress%100>=50:
                       bool='over'
                       break 					   
            if rss<399 and ress<=399 and ress%100<=50:
                       bool='under'
                       break 					   
        return(l,bool,f)		

##############################################
    def ltn(seed):
        bool=''
        hs=seed
        lhs=list(dict.fromkeys(list(hs)))
        bhs=''.join([i for i in lhs])
        fs=str(int(hs,16))
        bs=(bin(int(fs)))[2:]
        while True:
            f=pwd.ran(40)
            hc=pwd.sha2(f)
            lfs=list(dict.fromkeys(list(hc)))
            bfs=''.join([i for i in lfs])
            fc=str(int(hc,16))
            bc=(bin(int(fc)))[2:]
            kl=list(f)
            kls=list(dict.fromkeys(kl))
            cc=SequenceMatcher(None,bhs,bfs)	  
            fs=cc.ratio()
            bb=SequenceMatcher(None,bfs,bhs)	  
            js=bb.ratio()
            if  js>=0.4 and fs>=0.4 and hc[0]==hs[0] and hc[-1]==hs[-1] :#and len(clt)<=34 :#and hc[0]==hs[0] and hc[-1]==hs[-1]: and hc[0]==hs[0] and hc[-1]==hs[-1]bc[:8]==bs[:8] and bc[-8:]==bs[-8:] len(bfs)==len(bhs) and 
                #â‚¬print(fs)
                # print(bhs)
                # print(hc)
                # print(bfs)
                break
        while True:
            N='NxPzHXMgYKAEajWrFLwViRstdBTDlOeChpIbkSUyvfuoqcZnQmGJ'
            l=pwd.ran(34)#''.join(random.sample(N,14))#random.choice([pwd.rand(random.choice([8,16,24])),pwd.ran(random.choice([8,16,24])),pwd.num(random.choice([8,16,24]))])
            hl=pwd.sha2(l)
            ll=list(l)
            lls=list(dict.fromkeys(ll))
            ll=SequenceMatcher(None,lls,bhs)	  
            gs=bb.ratio()
            rs=pwd.resu(f,l)
            rss= (rs - ((rs // 100000) * 100000)) // 1000
            res=pwd.resu(l,'')
            ress= (res - ((res // 100000) * 100000)) // 1000
            clf=str(res)
            lcl=[int(i) for i in clf]
            lcl.sort()
            #and fc[0]==fs[0] and fc[-1]==fs[-1] 
            if rss>=50  and gs>=0.4:
                       bool='over'
                       # print(gs,js)
                       break 					   
            if rss<50  and gs>=0.4:
                       bool='under'
                       # print(gs,js)
                       break 					   
        return(l,bool,f)		




##############################################
    def ltp(seed,ttt):
        bool=''
        hs=seed
        khs=str(hash(hs))
        lhs=list(dict.fromkeys(list(hs)))
        bhs=''.join([i for i in lhs])
        fs=str(int(hs,16))
        bs=(bin(int(fs)))[2:]
        ih=int(hs,36)
        kb=ih
        s1=''
        s2=''
        i=0
        for x in range(64):
             kb=int(kb/52399113452444.84)
             kr=pwd.hex62(kb)
             i=i+1
             if i==1 :
                s1=kr
             if i ==2:
                s2=kr
             if i==3 :
                s3=kr
             if i ==4:
                s4=kr
             if i ==5:
                s5=kr
             if i ==6:
                s6=kr
             if i ==7:
                s7=kr
        # while True:
            # s3=pwd.ran(40)
            # hc=pwd.sha2(s3)
            # khc=str(hash(hc))
            # if  khc[-3:]==khs[-3:] and hc[-1]==hs[-1]:
                # break
        while True:
             l=pwd.ran(34)
             ll=l.lower()
             hh=pwd.sha2(l)
             #khh=str(hash(hc))
             rs1=pwd.resu(s1,l)
             rss1= (rs1 - ((rs1 // 100000) * 100000)) // 1000
             rs2=pwd.resu(s2,l)
             rss2= (rs2 - ((rs2 // 100000) * 100000)) // 1000
             rs3=pwd.resu(s3,l)
             rss3= (rs3 - ((rs3 // 100000) * 100000)) // 1000
             rs4=pwd.resu(s4,l)
             rss4= (rs4 - ((rs4 // 100000) * 100000)) // 1000
             rs5=pwd.resu(s5,l)
             rss5= (rs5 - ((rs5 // 100000) * 100000)) // 1000
             rs6=pwd.resu(s6,l)
             rss6= (rs6 - ((rs6 // 100000) * 100000)) // 1000
             rs7=pwd.resu(s7,l)
             rss7= (rs7 - ((rs7 // 100000) * 100000)) // 1000
             rsl=pwd.resu(l,'')
             rssl= (rsl - ((rsl // 100000) * 100000)) // 1000
             lss=[rss1,rss2,rss3,rss4,rss5,rss6,rss7]
             lss.sort()
             rd=pwd.resuv(seed,' '*256)
             # lhh=[i for i in hh if i.islower()]
             if  lss[0]>50 and rssl>=50 :#and rd>=50:
                # print(rrd,rssl,rss3)
                # print(rs2,l)
                bool='over'
                break
             if  lss[-1]<50 and rssl<=48 :#and rd<50:
                # print(rrd,rssl,rss3)
                # print(rs2,l)
                bool='under'
                break
				
        return(l,bool,s1)		

##############################################
    def ltx(seed,ttt):
        bool=''
        hs=seed
        ih=int(hs,16)
        xh=int(hs,36)
        khs=str(hash(hs))
        lhs=list(dict.fromkeys(list(hs)))
        bhs=''.join([i for i in lhs])
        fs=str(int(hs,16))
        bs=(bin(int(fs)))[2:]
        ih=int(hs,36)
        kb=ih
        s1=''
        s2=''
        i=0
        a= pwd.hex36(xh>>120)
        b=(pwd.hex36(xh>>121)).upper()
        c= pwd.hex36(xh>>122)
        d=(pwd.hex36(xh>>123)).upper()
        e= pwd.hex36(xh>>124)
        while True:
            kk=pwd.lod(randint(1,2))+pwd.num(randint(1,2))
            l=pwd.ran(34)  #''.join(random.choice(pwd.ran(40)) for x in range(34))
            hc=pwd.sha2(l)
            lr=pwd.resuv(l,'')
            ar=pwd.resuv(a,l)
            br=pwd.resuv(b,l)
            cr=pwd.resuv(c,l)
            dr=pwd.resuv(d,l)
            er=pwd.resuv(e,l)
            hr=pwd.resuv(hs,' '*256)
            tt=[ar,br,cr,dr,er]
            tt.sort()
            if fabs(br-dr)<5 and br>55 and fabs(ar-er)<5 and ar>55  and hr>=50:
                  bool='over'  
                  break				  
            if fabs(br-dr)<5 and br<55 and fabs(ar-er)<5 and ar<55  and hr<50:
                  bool='under'
                  break				  
	  
        return(l,bool,c)		
##############################################
    def bun(seed,u):
        bool=''
        hs=seed
        yy=[16,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,36]
        ll=[4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108,112, 116,120, 124, 128,132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188, 192, 196, 200, 204, 208, 212, 216,220, 224, 228, 232, 236, 240, 244, 248, 252]
        fg = [0, 9, 10, 19, 20, 29, 30, 39, 40, 49, 50, 59, 60, 69, 70, 79, 80, 89, 90, 99]#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        ls=[]
        # for i in yy:
           # for x in range(1,128,1):
              # ih=int(hs,i)
              # ff=ih>>x
              # z=pwd.hex62(ff)
              # hz=pwd.sha2(z)
              # if len(z)==40:
                 # ls.append(z)
        while True:
           s  = pwd.ran(40)
           h  = pwd.sha2(s)
           r  = pwd.resu(s,'')
           e  = (r - ((r // 100000) * 100000)) // 1000
           if e in fg and hs[0]==h[0] and len(str(e))<=6:
                ls.append(s)
                fg.remove(e)
           if len(fg)==0:
                #print('ok',rmk,sbd)
                break
        while True:
            un=[]
            ov=[]
            unf=[]
            ovf=[]
            if u>=3:
                uno=['0111110','0111110','0111110','0111110','0111110','011111','0111110','0111110','0111110','0111110','0111110']
                ovo=list(pwd.zum(28)) 
                all=ovo+uno+['1000','10001000','100010001000','10001','00010001000','10001000100010001000','1000']
                ful='1'+''.join(random.sample(all,len(all)))
                full=int(ful,2)
                lll=pwd.hex36(full)
                k=[x for x in range(len(lll))]
                k=random.sample(k,randint(5,int((len(k)-1)/2)))
                for i in k:
                  lll=lll.replace(lll[i],(lll[i]).upper())
                  l=pwd.ran(1)+lll#
            if u<3:
                  l=pwd.ran(34)#pwd.rand(1)+lll#
            # if u>=6:
                  # l=pwd.num(34)#pwd.rand(1)+lll#
            lky = pwd.resu(l,'')
            lfri = (lky - ((lky // 100000) * 100000)) // 1000
            ggg= pwd.resuv(seed,' '*256)
            for item in ls:
                  ky = pwd.resu(item,l)
                  fri = (ky - ((ky // 100000) * 100000)) // 1000
                  fbi=str(bin(int(item+l,36)))
                  if 50<=fri :#and fbi[-50:]=='1'*32:
                     ov.append(fri)
            for itm in ls:
                  ky = pwd.resu(itm,l)
                  fri = (ky - ((ky // 100000) * 100000)) // 1000
                  fbi=str(bin(int(item+l,36)))
                  if fri<50 :#and fbi[-50:]=='1'*32:
                     un.append(fri)
            if len(ov)>=10:#   and lfri<10 and ggg>=50:
                  bool='over'
                  break
            if len(un)>=10:#  and lfri>90 and ggg<50:
                  bool='under'
                  break
				  
        return(l,bool,ls[0])		

##############################################
    def buh(seed,ttt):
        bool=''
        hs=seed
        ls=[]
        ih=int(hs,17)
        ff=ih>>180
        z=pwd.hex62(ff)
        while True:
            l= ''.join(random.choice('01') for x in range(34))#pwd.zum(1)*randint(5,34)
            rl=pwd.resuv(seed,l)
            rz=pwd.resuv(z,l)
            if 70<=rz :
                  bool='over'
                  break
            if rz<30 :
                  bool='under'
                  break
				  
        return(l,bool,z)		
##############################################
    def box(seed,u):		
       h=seed
       d=[int(h,i) for i in range(16,37)]
       F=[(bin(int(x,16)))[2:] for x in re.split(r'(\w{2})', seed) if x]
       sd=sum(d)
       md=sum(d)/len(d)
       hx=(hex(int(md)))[2:]
       ls=[]
       fff=''
       cc='0'*34
       fg = [0, 9, 10, 19, 20, 29, 30, 39, 40, 49, 50, 59, 60, 69, 70, 79, 80, 89, 90, 99]
       if u<=2:
         while True:
           z=pwd.ran(40)
           f=pwd.sha2(z)
           r=[int(h,i) for i in range(16,37)]
           sr=sum(d)
           mr=sum(d)/len(d)
           hz=(hex(int(mr)))[2:]
           if hz[:16]==hx[:16] and f[:1]==h[:1]:
                 ls.append(z)
                 #print('z:',z,pwd.resu(z,cc))
                 if len(ls)==10:
                     break
       if u>2:
         while True:
             cr=[]
             z=pwd.ran(40)
             hb=pwd.sha2(z)
             G=[(bin(int(x,16)))[2:] for x in re.split(r'(\w{2})', hb) if x]
             for i in G:
                for x in F:
                    rrd=SequenceMatcher(None,i,x)	  
                    ffs=rrd.ratio()
                    if ffs>=1:#abs(x-i)<=10000 and h[32]==b[32]:
                       cr.append(ffs)
             if len(cr)>=8:
                   break
       while True:
            un=[]
            ov=[]
            unf=[]
            ovf=[]
            # if u>2:#u>=3:
                # uno=['0111110','0111110','0111110','0111110','0111110','011111','0111110','0111110','0111110','0111110','0111110']
                # ovo=list(pwd.zum(28)) 
                # all=ovo+uno+['1000','10001000','100010001000','10001','00010001000','10001000100010001000','1000']
                # ful='1'+''.join(random.sample(all,len(all)))
                # full=int(ful,2)
                # lll=pwd.hex36(full)
                # k=[x for x in range(len(lll))]
                # k=random.sample(k,randint(5,int((len(k)-1)/2)))
                # for i in k:
                  # lll=lll.replace(lll[i],(lll[i]).upper())
                  # l=pwd.ran(1)+lll#
            if u>2:
                  l=pwd.lod(randint(17,34))#random.choice([pwd.num(randint(5,17)),pwd.lod(randint(17,34))])
            if u<=2:
                  l=pwd.rans(randint(5,34))#'0'*randint(5,34)#pwd.rans(randint(5,34))#'0'*randint(17,34)#pwd.lod(34)
            lky = pwd.resu(l,'')
            lfri = (lky - ((lky // 100000) * 100000)) // 1000
            lzi = pwd.resu(z,l)
            lz = (lzi - ((lzi // 100000) * 100000)) // 1000
            ggg= pwd.resuv(seed,' '*256)
            if u<=2:
              for item in ls:
                  ky = pwd.resu(item,l)
                  fri = (ky - ((ky // 100000) * 100000)) // 1000
                  fbi=str(bin(int(item+l,36)))
                  if 50<=fri :#and fbi[-50:]=='1'*32:
                     ov.append(fri)
              for itm in ls:
                  ky = pwd.resu(itm,l)
                  fri = (ky - ((ky // 100000) * 100000)) // 1000
                  fbi=str(bin(int(item+l,36)))
                  if fri<50 :#and fbi[-50:]=='1'*32:
                     un.append(fri)
            if u<=2:
               fff=ls[0]
               # if len(ov)==7  and lfri in fg and u<=3:#and ggg>=50:
                  # bool='over'
                  # break
               if len(un)>=6 and lfri in fg :#  and lfri>90 and ggg<50:
                  bool='under'
                  break
            if u>2:
               fff=z
               if  lz>=50:# and lfri>95 :#and ggg>=50:
                  bool='over'
                  break
               # if lz<50:# and lfri<5 :#and ggg<50:
                  # bool='under'
                  # break
       return(l,bool,fff)		
		
		
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
            if 50<rz and uuu%2==0:#60<rn and 10>abs(rm==rn) and 60<rl:#and uuu%4==0:
                  bool='over'
                  l=q
                  break
            if rz<50 and uuu%2==1:# rn<60 and abs(rm-rn)<10 and 40>rl:#and uuu%4==1:
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
    def bsx(seed,ttt,rrr,ooo,uuu,ic,u):		
       hs=seed
       while True:
           lrc=[]
           z=pwd.ran(40)
           hz=pwd.sha2(z)
           rz=pwd.resuv(z,'')
           rh=pwd.resuv(hz,' '*256)
           x=4
           y=3
           sh='**'
           zh='**'
           # for i in range(63-x):
             # if hs[i:i+x] in hz or hz[i:i+x] in hs:
                        # sh=hs[i:i+x]
                        # zh=hz[i:i+x]
           if hs[:3]==hz[:3] :#hs[:3]==hz[:3]: zh in hs or sh in hz:
              # print(hs,sh)		   		   
              # print(hz,zh)		   		   
              break		   		   
       while True:
            bs=5
            while True:
                ql=random.choice([list(pwd.upd(35))+['Cfj','cC'],list(pwd.lod(35))+['CH','ch9']])
                random.shuffle(ql)
                q  =''.join([i for i in ql])#random.choice([pwd.num(ts),pwd.zum(ts),pwd.upd(ts),pwd.lod(ts),pwd.ran(ts)])
                hq =pwd.sha5(q)
                hq2=pwd.sha2(q)
                car=len([i for i in hq2 if i.islower()])
                rz=pwd.resuv(z,q)
                qhash  = hashlib.sha512(q.encode('UTF-8')).hexdigest()
                #rq     = (int(qhash[:5],16) -((int(qhash[:5],16)//100000)*100000))//1000   
                rq=pwd.resuv(q,'')
                break
                # if rq<50 and ic%2==0:   
                          # break
                # if  rq>50 and ic%2==1:	   
                          # break
            mmm= 'ªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªªª'
            nnn= 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU'
            rm = pwd.resuv(mmm,q)
            rn = pwd.resuv(nnn,q)
            # if ic%2==0:
            fhash = hashlib.sha512((z+q).encode('UTF-8')).hexdigest()
            rf    =int(fhash[:5],16)
            if  rz>50 and rq>50 and rn>50 and rm>50 and car>=31 and hq2[0]=='0' and 'CH' in q:
                  bool='over'
                  l=q
                  break
            if  rz<50 and rq<50 and rn<50 and rm<50 and car<=20 and hq2[0]=='f' and 'cC' in q:
                  bool='under'
                  l=q
                  break
            # if ic%2==1:
               # if 65<rz<85 and 65<rn<85 and 'CH' in q  and 65<rq<85 and ttt%2==0:#and 50<rq :#and uuu%2==1:#and 50<rn and 50<rm:
                  # bool='over'
                  # l=q
                  # break
               # if 15<rz<35 and 15<rn<35 and 'CH' in q  and 15<rq<35 and ttt%2==1:#if rz<round(uuu,0):#and 50>rn and 50>rm:
                  # bool='under'
                  # l=q
                  # break

       return(l,bool,z)
