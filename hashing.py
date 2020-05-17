#!/usr/bin/env python
import hashlib
import string
import random
from decimal import *
from hashing import*
import sys
SSS=string.ascii_letters
class pwd():
   @staticmethod
   def sha2(self):
       hashd  = hashlib.sha256(self.encode('UTF-8')).hexdigest()
       return hashd
   @staticmethod
   def sha1(self):
       rhash  = hashlib.sha1(self.encode('UTF-8')).hexdigest()
       return rhash
   @staticmethod
   def md5(self):
       vhashd  = hashlib.md5(self.encode('UTF-8')).hexdigest()
       return vhashd
   @staticmethod
   def sha5(self):
        mhash  = hashlib.sha512(self.encode('UTF-8')).hexdigest()
        return mhash
   @staticmethod
   def sha3(self):
        shash  = hashlib.sha384(self.encode('UTF-8')).hexdigest()
        return shash
   @staticmethod
   def shad(self):
        khash  = hashlib.sha224(self.encode('UTF-8')).hexdigest()
        return khash
   @staticmethod
   def itg(self):
        itf= int(self,16)
        return itf
   @staticmethod
   def ran(self):
       char  = ''.join(random.choice(string.ascii_letters+string.digits) for x in range(self))
       return char
   @staticmethod
   def upd(self):
       char  = ''.join(random.choice(string.ascii_uppercase) for x in range(self))
       return char
   @staticmethod
   def lod(self):
       char  = ''.join(random.choice(string.ascii_lowercase) for x in range(self))
       return char
   @staticmethod
   def rand(self):
       char  = ''.join(random.choice(string.ascii_letters) for x in range(self))
       return char   
   @staticmethod
   def rans(k2):
       SM    = pwd.ran(2)*20
       char  = ''.join(random.sample(SM,k2))
       return char    
   @staticmethod
   def num(self):
       char  = ''.join(random.choice('0123456789') for x in range(self))
       return char
   @staticmethod
   def zum(self):
       char  = ''.join(random.choice('01') for x in range(self))
       return char
   @staticmethod
   def rum(self):
       char  = ''.join(random.choice('Qr') for x in range(self))#cfgklmnosvwxyzO367
       return char
   @staticmethod
   def xum(self):
       char  = ''.join(random.choice(string.ascii_lowercase+'0123456789') for x in range(self))#cfgklmnosvwxyzO367
       return char
   @staticmethod
   def resu(k1,k2):
        feed   = k1+k2
        mhash  = hashlib.sha512(feed.encode('UTF-8')).hexdigest()
        resu   = int(mhash[:5],16) # (int(mhash[:5],16) -((int(mhash[:5],16)//100000)*100000))//1000             
        return resu
   @staticmethod
   def resuv(k1,k2):
        feed   = k1+k2
        mhash  = hashlib.sha512(feed.encode('UTF-8')).hexdigest()
        resu   = (int(mhash[:5],16) -((int(mhash[:5],16)//100000)*100000))//1000             
        return resu
   @staticmethod
   def resl(k1,k2):
        feed   = k1+k2
        mhash  = hashlib.sha512(feed.encode('UTF-8')).hexdigest()
        resu   = ''
        if len(str(int(mhash[:5],16)))<=6:
           resu=int(mhash[:5],16)
        if len(str(int(mhash[:5],16)))>6:
           resu=int(mhash[5:10],16)
        return resu
   @staticmethod
   def pgcd(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    while b!=0:
        r=a%b
        a,b=b,r
    return a
   @staticmethod
   def hex36(integer):           
       chars = '0123456789abcdefghijklmnopqrstuvwxyz'          
                  
       sign = '-' if integer < 0 else ''           
       integer = abs(integer)           
       result = ''           
       while integer > 0:
           integer, remainder = divmod(integer, 36)
           result = chars[remainder]+result

       return sign+result
   @staticmethod
   def hex62(integer):           
       chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'          
                  
       sign = '-' if integer < 0 else ''           
       integer = abs(integer)           
       result = ''           
       while integer > 0:
           integer, remainder = divmod(integer, 62)
           result = chars[remainder]+result

       return sign+result
   @staticmethod
   def flot(k):
        getcontext().prec = 77
        fl = Decimal.from_float(k)            
        return fl
   @staticmethod
   def pvm(self): 
     a= ''.join(random.choice(string.ascii_letters) for x in range(self))
     b= ''.join(random.choice('0123456789') for x in range(self))
     char=''
     for i in range(self):
       char=char+a[i]+b[i+1]
       if len(char)==self:
          break
     return char
   @staticmethod
   def pum(k1,k2): 
     a= k1
     b= k2
     char=''
     for i in range(len(a)):
       char=char+a[i]+b
     return char
   @staticmethod
   def d(self):
      a='{0:.100f}'.format(self)
      return a
   @staticmethod
   def gt(dict): 
       return dict.keys() 