import os
import shutil
from smtplib import OLDSTYLE_AUTH
#current directory
from_path = os.getcwd()
into_path = r"C:\\Users\Alexandre\\Games\Age of Empires 2 DE\\2535458961098920\\mods\\local"



lst_dir_from = []
lst_dir_into = []
  

#fonction qui vérifie si les dossiers présent dans from_path sont dans into_path
def check_dir(from_path):
    for root, dirs, files in os.walk(from_path):
        if not os.path.exists(into_path + root[len(from_path):]):
            #on copy les dossier et leur contenu dans into_path 
            shutil.copytree(root, into_path + root[len(from_path):])
            print("folder", root, "has been added")



def lst_dir(from_path, into_path):
    global lst_dir_from
    global lst_dir_into
    for root, dirs, files in os.walk(from_path):
        lst_dir_from.append(root)
    for root, dirs, files in os.walk(into_path):
        lst_dir_into.append(root)

#function which compare the content of two files
def compare(fic1_path, fic2_path):
    fic1 = open(fic1_path, "r")
    fic2 = open(fic2_path, "r")
    #on compare les deux fichiers
    if fic1.read() == fic2.read():
        return True
    else:
        #on prend le contenu qui à été modifié
        print("file",fic1_path.split("\\")[-1], "has been modified")
        return False


#function who push file into into_path
def push(from_path, into_path):
    content_added = False
    for root, dirs, files in os.walk(from_path):
        for file in files:
            #si les files sont en .per
            if file.endswith(".per"):
                #on compare les fichiers
                if compare(root + "\\" + file, into_path + root[len(from_path):] + "\\" + file) == False:
                    #on copie le fichier dans into_path
                    shutil.copy(root + "\\" + file, into_path + root[len(from_path):] + "\\" + file)
                    print("file", root + "\\" + file, "has been added")
                    content_added = True
    if content_added == False:
        print("no content added")
    return content_added


#check(from_path)


check_dir(from_path)
lst_dir(from_path, into_path)
push(from_path, into_path)
