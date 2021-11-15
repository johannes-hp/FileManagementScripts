def ARemover():
    import os
    import pathlib
    basepath = pathlib.Path(__file__).parent.resolve() #finds current directory

    for entry in os.listdir(basepath): #loops over subentries in cd
        if os.path.isdir(os.path.join(basepath, entry)): #checks if entry is a directory
            if "RECYCLE" in os.path.join(basepath, entry):
                continue
            else:
                for file in os.listdir(str(basepath) + "\\" + entry): #loops over files in subdirectory
                    if "a." in file.lower():
                        print(file, 'deleted') #prints to terminal
                        os.remove(os.path.join(basepath, entry, file)) #deletes file
                        with open('ARemoverOutput.txt', 'a') as fout: #opens output file
                            fout.write(os.path.join(basepath, entry, file) + ' deleted\n') #writes to output file

ARemover()
