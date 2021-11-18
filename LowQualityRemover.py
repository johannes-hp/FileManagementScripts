def low_quality_remover():
  
  import os
  import pathlib
  from datetime import datetime
  basepath = pathlib.Path(__file__).parent.resolve() #finds current directory
  
  for entry in os.listdir(basepath): #loops over subentries in cd
    if os.path.isdir(os.path.join(basepath, entry)): #checks if entry is a directory
      if "RECYCLE" in os.path.join(basepath, entry): #skips bin
        continue
      else:
        for file in os.scandir(str(basepath) + "\\" + entry):
          if datetime.fromtimestamp(file.stat().st_mtime) < datetime.strptime("01/01/07 00:00:00", "%d/%m/%y %H:%M:%S") and file.stat().st_size < 1000000: #checks if size below 1000KB and modification date before 2007
            print(file.path, str(int(file.stat().st_size / 1024)) + "KB", "last modified", datetime.fromtimestamp(file.stat().st_mtime), "deleted")
            os.remove(os.path.join(basepath, entry, file)) #deletes file
            with open ("LowQualityRemoverOutput.txt", "a") as fout: #open output file
              fout.write(str(file.path) + " " + str(file.stat().st_size) + "KB last modified " + str(datetime.fromtimestamp(file.stat().st_mtime)) + " deleted\n") #writes to output file
              
low_quality_remover()
