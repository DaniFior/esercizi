import os

root = input("Inserisci la root directory: ")
stringadacercare = input("Inserisci la stringa da cercare: ")
outdir = input("Inserisci la dir di output: ")

        

def cercastringainfilename(file, stringa):
    return False

def cercastringainfilecontent(filepathcompleto, string):
    return False


numfiletrovati = 0
for root, dirs, files in os.walk(root):
    toprint = "dir corrente {0} contenente {1} subdir e {2} files".format(root, len(dirs), len(files))
    print(toprint)
    for filename in files:
        ret = cercastringainfilename(filename, stringadacercare)
        if(ret != True):
            filepathcompleto = os.path.join(root,filename)
            ret = cercastringainfilecontent(filepathcompleto, stringadacercare)
        if(ret == True):
            print(f"Trovato file: {filename}")
<<<<<<< HEAD:Pyhton5_6/cercastringa.py
            numfiletrovati = numfiletrovati + 1
=======
            numfiletrovati = numfiletrovati + 1





            
        

        
>>>>>>> 02a6f688541c8170d791552a77e7144f484ca0b8:Python5_6/cercastringa.py
