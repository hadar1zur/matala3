# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:37:50 2021

@author: hadar
"""
def read_file()->str:
    file=open('my_chat.txt','r', encoding='utf-8')
    return(file)

def phon_dictionary():
    id_phon=dict()
    id_count=1  
    file=str()
    file=read_file()               
    for line in file:
        idst=line.find("-")
        idend=line.find(":",idst)
        if line.count(':')>=2:
            num_phon=line[idst+1:idend]
            if not num_phon in id_phon:
                id_phon [num_phon]=id_count
                id_count=id_count+1
    return(id_phon)
    
def find_data():
    id_data='' 
    id_text=''
    id_name='' 
    fileList=list()
    data=dict() 
    all_data=dict()
    id_phon=phon_dictionary()
    file=str()
    file=read_file()   
    for line in file:
       if 'נוצרה על ידי' in line:
           dataend=line.find("-",0)
           gruop_data=line[0:dataend]
           namest=line.find(' "')
           nameend=line.find('" ' ,namest)
           name_gruop=line[namest+2:nameend-2]
           num_gruopst=line.find('+')
           num_gruopend=line.find('ה', num_gruopst)
           num_gruop=line[num_gruopst:num_gruopend-2]
           data={"chat_name":name_gruop,"creation_date":gruop_data, "num_of_purtic":len(id_phon), "creator":num_gruop} 
       if line.count(':')==0:
           text=line.rstrip()
           id_text=id_text+text
           fileList[len(fileList)-1]=({"datetime":id_data,"id":id_name, "text":id_text},)
       if line.count(':')>=2:
           dataend=line.find("-",0)
           id_data=line[0:dataend]
           phonst=line.find("-")
           phonend=line.find(":",phonst)
           num_phon=line[phonst+1:phonend]
           id_name=id_phon[num_phon]
           textst=line.find(":")
           text=line.rstrip()[textst+1:]
           textst=text.find(":")
           id_text=text[textst+1:]
           fileList.append({"datetime":id_data,"id":id_name, "text":id_text},)
    all_data={'massages':fileList,'metadata':data}
    return(all_data)
import json
all_data=dict
all_data=find_data() 
print(all_data) 
name=all_data['metadata']  
 
data_string=name['chat_name']+".txt"
with open(data_string, 'w', encoding='utf8') as data_string:
    json.dump(all_data, data_string, ensure_ascii=False)







