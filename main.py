
name_en="global_en.ini"
name_fr="global_fr.ini"

def parsing_file(name_file):  
      
    with open (name_file,"r",encoding='utf-8-sig') as file:
        all_row=file.readlines()
        
    list_file=[]
    i=0
    for row in all_row:
        i=i+1
        item,trad=row.split("=",1)
        list_file.append([i,item.upper(),trad])
        
    return list_file



en_list=parsing_file(name_en)
fr_list=parsing_file(name_fr)



def find_diff(list1,list2):
    diff={}
    listeref=[]
    for row in list2:
        listeref.append(str(row[1]))
    #print(listeref)
    
    for row in list1:
        if str(row[1]) not in listeref:
                diff[row[0]]=row[1]
                print(row[0],row[1])
    #print(diff)
    print(len(diff))

find_diff(en_list,fr_list)

#def trouver_differences(list1, list2):
    #dico_list1={}
    #dico_list2={}
    #
    #for row in list1:
    #    dico_list1[row[0]]=row[1]
    #
    #for row in list2:
    #    dico_list2[row[0]]=row[1]

    

    #diff=set(dico_list1.values()).difference(set(dico_list2.values()))
    #print(type(diff))
    



