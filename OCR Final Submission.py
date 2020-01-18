#IMPORTING lIBRARIES
import numpy as np
import cv2
from tqdm import tqdm
from PIL import Image
import pytesseract
import matplotlib.pyplot as plt

#FUCTION TO EXTRACT TEXT FROM IMAGE
def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename), lang='fra')   
    return text


#lINK OF THE EDITED IMAGE FOLDER AFTER DEBLURRING CLUSTERING
input_link = 'C:\\Users\\karti\\OneDrive\\Desktop\\cvision\\Segmented Images\\segmented'

#lIST TO SAVE ALL REQUIRED CONTENTS
Regn_no =[]
Name=[]
Eng_no=[]
Mfg_date=[]
Reg_date=[]
Chas_no=[]
text_ls=[]

#EXTRACTING TEXT FROM IMAGES USING LOOP
for i in range(1,47):
    text_e = ocr_core(input_link +str(i)+'.jpg')
    ls=[]
    word =""
    for i in text_e:
        if i is not "\n":
            word =word+i
        else:
            print(word)
            ls.append(word)
            word=""
            
    #==============================================NAME========================================================
    name=""
    rem=""
    for w in ls:
        if w.startswith("NAME : "):
            print("First")
            print(w)
            name = w  
            name=name.replace("NAME : ", '')
        elif(w.startswith("NAME  : ")):
            print("Second")
            print(w)
            name = w  
            name=name.replace("NAME  : ", '')
        elif(w.startswith("NAME")):
            print("third")
            print(w)
            name = w  
            name=name.replace("NAME", '')
        elif( w.startswith("Name & Address")):
            print("Fourth")
            print(w)
            name = w  
            name=name.replace("Name & Address", '')
        elif w.startswith("Name &"):
            print("Fifth")
            print(w)
            name = w  
            name = name.replace("Name &", '')
            for i in name:
                if (i !=' '):
                    rem = rem + i
                else:
                    name = name.replace(rem,'')
                    break
        elif( w.startswith("Dealer's Name ")):
            print("Sixth")
            print(w)
            name = w  
            name=name.replace("Dealer's Name ", '')
        elif(w.find('NAME :')!= -1):
            print("Seventh")
            print(w)
            na = w
            a = w.find('NAME :')
            na=na.replace("NAME :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
        elif(w.find('NAME:')!= -1):
            print("Eighth")
            print(w)
            na = w
            a = w.find('NAME:')
            na=na.replace("NAME:", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
        elif(w.find('NAME')!= -1):
            print("Ninth")
            print(w)
            na = w
            a = w.find('NAME')
            na=na.replace("NAME", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
        elif(w.find('Name :')!= -1):
            print("Tenth")
            print(w)
            na = w
            a = w.find('Name :')
            na=na.replace("Name :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
        elif(w.find('Name:')!= -1):
            print("Eleventh")
            print(w)
            na = w
            a = w.find('Name:')
            na=na.replace("Name:", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
        elif(w.find('Name')!= -1):
            print("Twelveth")
            print(w)
            na = w
            a = w.find('Name')
            na=na.replace("Name", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
    
    
    print(name)
    Name.append(name)
    
    print(Name)
    
    
    #=========================================Regn No.=====================================================
    
    regn=""
    for w in ls:
        if w.startswith("REGN . NO : "):
            regn_no = w  
            regn_no=regn_no.replace("REGN . NO : ", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN . NO :")):
            regn_no = w  
            regn_no=regn_no.replace("REGN . NO :", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN . NO ")):
            regn_no = w  
            regn_no=regn_no.replace("REGN . NO ", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN. NO : ")):
            regn_no = w  
            regn_no=regn_no.replace("REGN. NO : ", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN. NO :")):
            regn_no = w  
            regn_no=regn_no.replace("REGN. NO :", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN. NO ")):
            regn_no = w  
            regn_no=regn_no.replace("REGN. NO ", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN. NO.")):
            regn_no = w  
            regn_no=regn_no.replace("REGN. NO.", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN. NO")):
            regn_no = w  
            regn_no=regn_no.replace("REGN. NO", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN.NO.")):
            regn_no = w  
            regn_no=regn_no.replace("REGN.NO.", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.find('tion No.')!= -1):
            regn_no = w
            a = w.find('tion No.')
            regn_no=regn_no.replace("tion No.", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            regn_no=regn_no.replace(rem, '')
        elif(w.find('tion No')!= -1):
            regn_no = w
            a = w.find('tion No')
            regn_no=regn_no.replace("tion No", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            regn_no=regn_no.replace(rem, '')
    
    print(regn_no)
    ree=""
    count=0
    for c in regn_no:
        if(c!=' '):
            ree=ree+c
            count=count+1
        else:
            if(count!=0):
                break
    print(ree)
    Regn_no.append(ree)
    print(Regn_no) 
     
    #==============================================Engine No,==============================================
    
    eng=""
    for w in ls:
        if w.startswith("ENO : "):
            print(w)
            print("First")
            eng_no = w  
            eng_no=eng_no.replace("ENO : ", '')
            flag=0
            count=0
            for i in eng_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    eng=eng+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("ENO")):
            print(w)
            print("First")
            eng_no = w  
            eng_no=eng_no.replace("ENO", '')
            flag=0
            count=0
            for i in eng_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    eng=eng+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("Engine No. : ")):
            print(w)
            print("second")
            eng_no = w  
            eng_no = eng_no.replace("Engine No. : ", '')
            print(eng_no)
            flag=0
            count=0
            for i in eng_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    eng=eng+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("Engine No. ")):
            print(w)
            print("third")
            eng_no = w  
            eng_no=eng_no.replace("Engine No. ", '')
            flag=0
            count=0
            for i in eng_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    eng=eng+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("Engine No.")):
            print(w)
            print("fourth")
            eng_no = w  
            eng_no=eng_no.replace("Engine No.", '')
            flag=0
            count=0
            for i in eng_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    eng=eng+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.find('ENO : ')!= -1):
            e_no = w
            a = w.find('ENO : ')
            e_no = e_no.replace("ENO : ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('ENO')!= -1):
            e_no = w
            a = w.find('ENO')
            e_no = e_no.replace("ENO", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('ENO')!= -1):
            e_no = w
            a = w.find('ENO')
            e_no = e_no.replace("ENO", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('Engine No. : ')!= -1):
            e_no = w
            a = w.find('Engine No. : ')
            e_no = e_no.replace("Engine No. : ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('Engine No. ')!= -1):
            e_no = w
            a = w.find('Engine No. ')
            e_no = e_no.replace("Engine No. ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('Engine No.')!= -1):
            e_no = w
            a = w.find('Engine No.')
            e_no = e_no.replace("Engine No.", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('Engine No')!= -1):
            e_no = w
            a = w.find('Engine No')
            e_no = e_no.replace("Engine No", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('EngineNo')!= -1):
            e_no = w
            a = w.find('Engine No')
            e_no = e_no.replace("EngineNo", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
    print(eng)
    Eng_no.append(eng)
    print(Eng_no)
    
    
    #====================================Chasis No.=================
    
    chasis=""
    for w in ls:
        if w.startswith("CH. NO "):
            print(w)
            chas = w  
            chas=chas.replace("CH. NO : ", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count >17):
                    flag=1
                if(ch_count>17):
                    break
        elif(w.startswith("Chasis No. : ")):
            print(w)
            chas = w  
            chas=chas.replace("Chasis No. : ", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count >17):
                    flag=1 
                if(ch_count>17):
                    break
        elif(w.startswith("Chasis No. :")):
            print(w)
            chas = w  
            chas=chas.replace("Chasis No. :", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count >17):
                    flag=1 
                if(ch_count>17):
                    break
        elif(w.startswith("Chasis No. ")):
            print(w)
            chas = w  
            chas=chas.replace("Chasis No. ", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count >17):
                    flag=1  
                if(ch_count>17):
                    break
        elif(w.startswith("Chasis No.")):
            print(w)
            chas = w  
            chas=chas.replace("Chasis No.", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count >17):
                    flag=1
                if(ch_count>17):
                    break
        elif(w.startswith("Chasis No")):
            print(w)
            chas = w  
            chas=chas.replace("Chasis No", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count > 17):
                    flag=1   
                if(ch_count>17):
                    break
        elif(w.find('CHNO : ')!= -1):
            c_no = w
            a = w.find('CHNO : ')
            c_no = c_no.replace("CHNO : ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO. :')!= -1):
            c_no = w
            a = w.find('CH. NO. :')
            c_no = c_no.replace("CH. NO. :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CHNO')!= -1):
            c_no = w
            a = w.find('CHNO')
            c_no = c_no.replace("CHNO", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO : ')!= -1):
            c_no = w
            a = w.find('CH. NO : ')
            c_no = c_no.replace("CH. NO : ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO :')!= -1):
            c_no = w
            a = w.find('CH. NO :')
            c_no = c_no.replace("CH. NO :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO')!= -1):
            c_no = w
            a = w.find('CH. NO')
            c_no = c_no.replace("CH. NO", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO : ')!= -1):
            c_no = w
            a = w.find('CH. NO : ')
            c_no = c_no.replace("CH. NO : ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO :')!= -1):
            c_no = w
            a = w.find('CH. NO :')
            c_no = c_no.replace("CH. NO :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('Chasis No. :')!= -1):
            c_no = w
            a = w.find('Chasis No. :')
            c_no = c_no.replace("Chasis No. :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('Chasis No.')!= -1):
            c_no = w
            a = w.find('Chasis No.')
            c_no = c_no.replace("Chasis No.", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('Chasis')!= -1):
            c_no = w
            a = w.find('Chasis')
            c_no = c_no.replace("Chasis", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
    
    print(chasis)
    count =0
    cha=""
    for i in chasis:
        if(i != ' '):
            count=count+1
            if(count<18):
                cha=cha+i
    print(cha)
    Chas_no.append(cha)
    print(Chas_no)
    
    
    #========================================Registration Date===========================================
    
    reg_date=""
    reg_d=""
    reg_date_num=""
    for w in ls:
        if w.startswith("REG. DT."):
            print(w)
            reg_d = w  
            reg_d=reg_d.replace("REG. DT. ", '')
            flag=0
            count=0
            for i in reg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    reg_date_num=reg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            for i in  reg_date_num:
                count1=count1+1
                if(count1<2):
                     reg_date= reg_date + i
                elif(count==2):
                    reg_date=reg_date+ '/' + i
                elif(count==3):
                    reg_date = reg_date + i + '/'
                else:
                    reg_date = reg_date + i
        elif(w.startswith("REG. DT:")):
            print(w)
            reg_d = w  
            reg_d=reg_d.replace("REG. DT:", '')
            flag=0
            count=0
            for i in reg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    reg_date_num=reg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            for i in  reg_date_num:
                count1=count1+1
                if(count1<2):
                     reg_date= reg_date + i
                elif(count==2):
                    reg_date=reg_date+ '/' + i
                elif(count==3):
                    reg_date = reg_date + i + '/'
                else:
                    reg_date = reg_date + i
        elif(w.startswith("REG. DT")):
            print(w)
            reg_d = w  
            reg_d=reg_d.replace("REG. DT", '')
            flag=0
            count=0
            for i in reg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    reg_date_num=reg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            for i in  reg_date_num:
                count1=count1+1
                if(count1<2):
                     reg_date= reg_date + i
                elif(count==2):
                    reg_date=reg_date+ '/' + i
                elif(count==3):
                    reg_date = reg_date + i + '/'
                else:
                    reg_date = reg_date + i
        elif(w.startswith("REGN DT: ")):
            print(w)
            reg_d = w  
            reg_d=reg_d.replace("REGN DT: ", '')
            flag=0
            count=0
            for i in reg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    reg_date_num=reg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            for i in  reg_date_num:
                count1=count1+1
                if(count1<2):
                     reg_date= reg_date + i
                elif(count==2):
                    reg_date=reg_date+ '/' + i
                elif(count==3):
                    reg_date = reg_date + i + '/'
                else:
                    reg_date = reg_date + i
        elif(w.startswith("REGN DT")):
            print(w)
            reg_d = w  
            reg_d=reg_d.replace("REGN DT", '')
            flag=0
            count=0
            for i in reg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    reg_date_num=reg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            for i in  reg_date_num:
                count1=count1+1
                if(count1<2):
                     reg_date= reg_date + i
                elif(count==2):
                    reg_date=reg_date+ '/' + i
                elif(count==3):
                    reg_date = reg_date + i + '/'
                else:
                    reg_date = reg_date + i
    
    reg_date=""
    count1=0
    for i in  reg_date_num:
        count1=count1+1
        if(count1<3):
            reg_date= reg_date + i
        elif(count1==3):
            reg_date=reg_date+ '/' + i
        elif(count1==4):
            reg_date = reg_date + i + '/'
        else:
            reg_date = reg_date + i
    
    print(reg_date)
    Reg_date.append(reg_date) 
    
    print(Reg_date)
    #===============================Manufacturing Date============================================
    mfg_date=""
    mfg_d=""
    mfg_date_num=""
    for w in ls:
        if w.startswith("Date of Issue"):
            print("First")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("Date of Issue", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("Six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        if w.startswith("MFG.DT. - "):
            print("second")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("MFG.DT. - ", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("MFG.DT. : ")):
            print("third")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("MFG.DT. : ", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("MFG.DT. :")):
            print("Fourth")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("MFG.DT. :", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("MFG.DT.")):
            print("Fifth")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("MFG.DT.", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("Month/ Year of Manufacture")):
            print("Sixth")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("Month/ Year of Manufacture", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("Month/ Yrof")):
            print("seventh")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("Month/ Yrof", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("Month/Yr of")):
            print("Eighth")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("Month/Yr of", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six") 
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print("eight")
                print(mfg_date)
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("MFG")):
            print(w)
            print("ninth")
            mfg_d = w  
            mfg_d=mfg_d.replace("MFG", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                 print("six")
                 for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("MEG OT")):
            print(w)
            print("ninth")
            mfg_d = w  
            mfg_d=mfg_d.replace("MEG OT", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                 print("six")
                 for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
    print(Mfg_date)
    print(mfg_date_num)
    print(mfg_date)
    Mfg_date.append(mfg_date)
###############################PNG##################################
    
for i in range(47,49):
    text_e = ocr_core(input_link +str(i)+'.jpg')
    ls=[]
    word =""
    for i in text_e:
        if i is not "\n":
            word =word+i
        else:
            print(word)
            ls.append(word)
            word=""
            
#==============================================NAME========================================================
    name=""
    rem=""
    for w in ls:
        if w.startswith("NAME : "):
            print("First")
            print(w)
            name = w  
            name=name.replace("NAME : ", '')
        elif(w.startswith("NAME  : ")):
            print("Second")
            print(w)
            name = w  
            name=name.replace("NAME  : ", '')
        elif(w.startswith("NAME")):
            print("third")
            print(w)
            name = w  
            name=name.replace("NAME", '')
        elif( w.startswith("Name & Address")):
            print("Fourth")
            print(w)
            name = w  
            name=name.replace("Name & Address", '')
        elif w.startswith("Name &"):
            print("Fifth")
            print(w)
            name = w  
            name = name.replace("Name &", '')
            for i in name:
                if (i !=' '):
                    rem = rem + i
                else:
                    name = name.replace(rem,'')
                    break
        elif( w.startswith("Dealer's Name ")):
            print("Sixth")
            print(w)
            name = w  
            name=name.replace("Dealer's Name ", '')
        elif(w.find('NAME :')!= -1):
            print("Seventh")
            print(w)
            na = w
            a = w.find('NAME :')
            na=na.replace("NAME :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
        elif(w.find('NAME:')!= -1):
            print("Eighth")
            print(w)
            na = w
            a = w.find('NAME:')
            na=na.replace("NAME:", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
        elif(w.find('NAME')!= -1):
            print("Ninth")
            print(w)
            na = w
            a = w.find('NAME')
            na=na.replace("NAME", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
        elif(w.find('Name :')!= -1):
            print("Tenth")
            print(w)
            na = w
            a = w.find('Name :')
            na=na.replace("Name :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
        elif(w.find('Name:')!= -1):
            print("Eleventh")
            print(w)
            na = w
            a = w.find('Name:')
            na=na.replace("Name:", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
        elif(w.find('Name')!= -1):
            print("Twelveth")
            print(w)
            na = w
            a = w.find('Name')
            na=na.replace("Name", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            na=na.replace(rem, '')
            name=na
    
    
    print(name)
    Name.append(name)
    
    print(Name)
    
    
    #=========================================Regn No.=====================================================
    
    regn=""
    for w in ls:
        if w.startswith("REGN . NO : "):
            regn_no = w  
            regn_no=regn_no.replace("REGN . NO : ", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN . NO :")):
            regn_no = w  
            regn_no=regn_no.replace("REGN . NO :", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN . NO ")):
            regn_no = w  
            regn_no=regn_no.replace("REGN . NO ", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN. NO : ")):
            regn_no = w  
            regn_no=regn_no.replace("REGN. NO : ", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN. NO :")):
            regn_no = w  
            regn_no=regn_no.replace("REGN. NO :", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN. NO ")):
            regn_no = w  
            regn_no=regn_no.replace("REGN. NO ", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN. NO.")):
            regn_no = w  
            regn_no=regn_no.replace("REGN. NO.", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN. NO")):
            regn_no = w  
            regn_no=regn_no.replace("REGN. NO", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("REGN.NO.")):
            regn_no = w  
            regn_no=regn_no.replace("REGN.NO.", '')
            flag=0
            count=0
            for i in regn_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    regn=regn+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.find('tion No.')!= -1):
            regn_no = w
            a = w.find('tion No.')
            regn_no=regn_no.replace("tion No.", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            regn_no=regn_no.replace(rem, '')
        elif(w.find('tion No')!= -1):
            regn_no = w
            a = w.find('tion No')
            regn_no=regn_no.replace("tion No", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            regn_no=regn_no.replace(rem, '')
    
    print(regn_no)
    ree=""
    count=0
    for c in regn_no:
        if(c!=' '):
            ree=ree+c
            count=count+1
        else:
            if(count!=0):
                break
    print(ree)
    Regn_no.append(ree)
    print(Regn_no) 
     
    #==============================================Engine No,==============================================
    
    eng=""
    for w in ls:
        if w.startswith("ENO : "):
            print(w)
            print("First")
            eng_no = w  
            eng_no=eng_no.replace("ENO : ", '')
            flag=0
            count=0
            for i in eng_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    eng=eng+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("ENO")):
            print(w)
            print("First")
            eng_no = w  
            eng_no=eng_no.replace("ENO", '')
            flag=0
            count=0
            for i in eng_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    eng=eng+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("Engine No. : ")):
            print(w)
            print("second")
            eng_no = w  
            eng_no = eng_no.replace("Engine No. : ", '')
            print(eng_no)
            flag=0
            count=0
            for i in eng_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    eng=eng+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("Engine No. ")):
            print(w)
            print("third")
            eng_no = w  
            eng_no=eng_no.replace("Engine No. ", '')
            flag=0
            count=0
            for i in eng_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    eng=eng+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.startswith("Engine No.")):
            print(w)
            print("fourth")
            eng_no = w  
            eng_no=eng_no.replace("Engine No.", '')
            flag=0
            count=0
            for i in eng_no:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    eng=eng+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
        elif(w.find('ENO : ')!= -1):
            e_no = w
            a = w.find('ENO : ')
            e_no = e_no.replace("ENO : ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('ENO')!= -1):
            e_no = w
            a = w.find('ENO')
            e_no = e_no.replace("ENO", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('ENO')!= -1):
            e_no = w
            a = w.find('ENO')
            e_no = e_no.replace("ENO", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('Engine No. : ')!= -1):
            e_no = w
            a = w.find('Engine No. : ')
            e_no = e_no.replace("Engine No. : ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('Engine No. ')!= -1):
            e_no = w
            a = w.find('Engine No. ')
            e_no = e_no.replace("Engine No. ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('Engine No.')!= -1):
            e_no = w
            a = w.find('Engine No.')
            e_no = e_no.replace("Engine No.", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('Engine No')!= -1):
            e_no = w
            a = w.find('Engine No')
            e_no = e_no.replace("Engine No", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
        elif(w.find('EngineNo')!= -1):
            e_no = w
            a = w.find('Engine No')
            e_no = e_no.replace("EngineNo", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            e_no=e_no.replace(rem, '')
            eng = e_no
    print(eng)
    Eng_no.append(eng)
    print(Eng_no)
    
    
    #====================================Chasis No.=================
    
    chasis=""
    for w in ls:
        if w.startswith("CH. NO "):
            print(w)
            chas = w  
            chas=chas.replace("CH. NO : ", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count >17):
                    flag=1
                if(ch_count>17):
                    break
        elif(w.startswith("Chasis No. : ")):
            print(w)
            chas = w  
            chas=chas.replace("Chasis No. : ", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count >17):
                    flag=1 
                if(ch_count>17):
                    break
        elif(w.startswith("Chasis No. :")):
            print(w)
            chas = w  
            chas=chas.replace("Chasis No. :", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count >17):
                    flag=1 
                if(ch_count>17):
                    break
        elif(w.startswith("Chasis No. ")):
            print(w)
            chas = w  
            chas=chas.replace("Chasis No. ", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count >17):
                    flag=1  
                if(ch_count>17):
                    break
        elif(w.startswith("Chasis No.")):
            print(w)
            chas = w  
            chas=chas.replace("Chasis No.", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count >17):
                    flag=1
                if(ch_count>17):
                    break
        elif(w.startswith("Chasis No")):
            print(w)
            chas = w  
            chas=chas.replace("Chasis No", '')
            flag=0
            count=0
            ch_count=0
            for i in chas:
                if ((flag==0) and (i!=' ')):
                    print(i)
                    ch_count=ch_count+1
                    chasis=chasis+str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' ' and ch_count > 17):
                    flag=1   
                if(ch_count>17):
                    break
        elif(w.find('CHNO : ')!= -1):
            c_no = w
            a = w.find('CHNO : ')
            c_no = c_no.replace("CHNO : ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO. :')!= -1):
            c_no = w
            a = w.find('CH. NO. :')
            c_no = c_no.replace("CH. NO. :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CHNO')!= -1):
            c_no = w
            a = w.find('CHNO')
            c_no = c_no.replace("CHNO", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO : ')!= -1):
            c_no = w
            a = w.find('CH. NO : ')
            c_no = c_no.replace("CH. NO : ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO :')!= -1):
            c_no = w
            a = w.find('CH. NO :')
            c_no = c_no.replace("CH. NO :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO')!= -1):
            c_no = w
            a = w.find('CH. NO')
            c_no = c_no.replace("CH. NO", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO : ')!= -1):
            c_no = w
            a = w.find('CH. NO : ')
            c_no = c_no.replace("CH. NO : ", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('CH. NO :')!= -1):
            c_no = w
            a = w.find('CH. NO :')
            c_no = c_no.replace("CH. NO :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('Chasis No. :')!= -1):
            c_no = w
            a = w.find('Chasis No. :')
            c_no = c_no.replace("Chasis No. :", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('Chasis No.')!= -1):
            c_no = w
            a = w.find('Chasis No.')
            c_no = c_no.replace("Chasis No.", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
        elif(w.find('Chasis')!= -1):
            c_no = w
            a = w.find('Chasis')
            c_no = c_no.replace("Chasis", '')
            rem=""
            for j in range(0,a):
                rem= rem+w[j]
            c_no=c_no.replace(rem, '')
            chasis = c_no
    
    print(chasis)
    count =0
    cha=""
    for i in chasis:
        if(i != ' '):
            count=count+1
            if(count<18):
                cha=cha+i
    print(cha)
    Chas_no.append(cha)
    print(Chas_no)
    
    
    #========================================Registration Date===========================================
    
    reg_date=""
    reg_d=""
    reg_date_num=""
    for w in ls:
        if w.startswith("REG. DT."):
            print(w)
            reg_d = w  
            reg_d=reg_d.replace("REG. DT. ", '')
            flag=0
            count=0
            for i in reg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    reg_date_num=reg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            for i in  reg_date_num:
                count1=count1+1
                if(count1<2):
                     reg_date= reg_date + i
                elif(count==2):
                    reg_date=reg_date+ '/' + i
                elif(count==3):
                    reg_date = reg_date + i + '/'
                else:
                    reg_date = reg_date + i
        elif(w.startswith("REG. DT:")):
            print(w)
            reg_d = w  
            reg_d=reg_d.replace("REG. DT:", '')
            flag=0
            count=0
            for i in reg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    reg_date_num=reg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            for i in  reg_date_num:
                count1=count1+1
                if(count1<2):
                     reg_date= reg_date + i
                elif(count==2):
                    reg_date=reg_date+ '/' + i
                elif(count==3):
                    reg_date = reg_date + i + '/'
                else:
                    reg_date = reg_date + i
        elif(w.startswith("REG. DT")):
            print(w)
            reg_d = w  
            reg_d=reg_d.replace("REG. DT", '')
            flag=0
            count=0
            for i in reg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    reg_date_num=reg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            for i in  reg_date_num:
                count1=count1+1
                if(count1<2):
                     reg_date= reg_date + i
                elif(count==2):
                    reg_date=reg_date+ '/' + i
                elif(count==3):
                    reg_date = reg_date + i + '/'
                else:
                    reg_date = reg_date + i
        elif(w.startswith("REGN DT: ")):
            print(w)
            reg_d = w  
            reg_d=reg_d.replace("REGN DT: ", '')
            flag=0
            count=0
            for i in reg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    reg_date_num=reg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            for i in  reg_date_num:
                count1=count1+1
                if(count1<2):
                     reg_date= reg_date + i
                elif(count==2):
                    reg_date=reg_date+ '/' + i
                elif(count==3):
                    reg_date = reg_date + i + '/'
                else:
                    reg_date = reg_date + i
        elif(w.startswith("REGN DT")):
            print(w)
            reg_d = w  
            reg_d=reg_d.replace("REGN DT", '')
            flag=0
            count=0
            for i in reg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    reg_date_num=reg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            for i in  reg_date_num:
                count1=count1+1
                if(count1<2):
                     reg_date= reg_date + i
                elif(count==2):
                    reg_date=reg_date+ '/' + i
                elif(count==3):
                    reg_date = reg_date + i + '/'
                else:
                    reg_date = reg_date + i
    
    reg_date=""
    count1=0
    for i in  reg_date_num:
        count1=count1+1
        if(count1<3):
            reg_date= reg_date + i
        elif(count1==3):
            reg_date=reg_date+ '/' + i
        elif(count1==4):
            reg_date = reg_date + i + '/'
        else:
            reg_date = reg_date + i
    
    print(reg_date)
    Reg_date.append(reg_date) 
    
    print(Reg_date)
    #===============================Manufacturing Date============================================
    mfg_date=""
    mfg_d=""
    mfg_date_num=""
    for w in ls:
        if w.startswith("Date of Issue"):
            print("First")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("Date of Issue", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("Six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        if w.startswith("MFG.DT. - "):
            print("second")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("MFG.DT. - ", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("MFG.DT. : ")):
            print("third")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("MFG.DT. : ", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("MFG.DT. :")):
            print("Fourth")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("MFG.DT. :", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("MFG.DT.")):
            print("Fifth")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("MFG.DT.", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("Month/ Year of Manufacture")):
            print("Sixth")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("Month/ Year of Manufacture", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("Month/ Yrof")):
            print("seventh")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("Month/ Yrof", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print(mfg_date)
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("Month/Yr of")):
            print("Eighth")
            print(w)
            mfg_d = w  
            mfg_d=mfg_d.replace("Month/Yr of", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                print("six") 
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print("eight")
                print(mfg_date)
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("MFG")):
            print(w)
            print("ninth")
            mfg_d = w  
            mfg_d=mfg_d.replace("MFG", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                 print("six")
                 for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
        elif(w.startswith("MEG OT")):
            print(w)
            print("ninth")
            mfg_d = w  
            mfg_d=mfg_d.replace("MEG OT", '')
            flag=0
            count=0
            for i in mfg_d:
                if ((flag==0) and (i!=' ') and i.isdigit()):
                    print(i)
                    mfg_date_num = mfg_date_num + str(i)
                if(i!=' '):
                    count=1
                if(count==1 and i==' '):
                    flag=1
            count1=0
            if(len(mfg_date_num)==6):
                 print("six")
                 for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<2):
                         mfg_date = mfg_date + i
                    elif(count1==3):
                        mfg_date = mfg_date+ '/' + i
                    else:
                        mfg_date = mfg_date + i
            
            elif(len(mfg_date_num)==8):
                print("eight")
                for i in  mfg_date_num:
                    count1=count1+1
                    if(count1<3):
                        mfg_date= mfg_date + i
                    elif(count1==3):
                        mfg_date=mfg_date+ '/' + i
                    elif(count1==4):
                        mfg_date = mfg_date + i + '/'
                    else:
                        mfg_date = mfg_date + i
    print(Mfg_date)
    print(mfg_date_num)
    print(mfg_date)
    Mfg_date.append(mfg_date)

#========================
print(Name)
print(Mfg_date)
print(Reg_date)
print(Regn_no)
print(Eng_no)
print(Chas_no)       

import pandas as pd
Names = pd.DataFrame(Name)
Mfg_dates = pd.DataFrame(Mfg_date)
Reg_dates = pd.DataFrame(Reg_date)
Regn_nos = pd.DataFrame(Regn_no)
Eng_nos = pd.DataFrame(Eng_no)
Chas_nos = pd.DataFrame(Chas_no)

data = pd.concat([Names,Mfg_dates,Reg_dates,Regn_nos,Eng_nos,Chas_nos],axis=1) 
data.shape

data.columns = ['Name', 'Manufacturing Date', 'Registration Date','Registration No.','Engine No.','Chassis No.']

data.to_csv('text1.csv')

