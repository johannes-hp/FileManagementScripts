FileRemover.py kan slette filer, der er lagt ind som en undermappe til FileRemover. FileRemover.py sletter ikke tif, zip, jpg, eller tmp-filer.

FileRemover's output printes til terminalen samt skrives ud til en output-tekstfil. Programmet tilføjer til denne tekstfil for hver kørsel, så det kan være en idé, at slette output-filen engang imellem.

FileRemover kan køres ved at navigere ned til rodmappen og køre "python FileRemover.py" i terminalen

Mappestrukturen vil se sådan ud, efter programmet er kørt:

FileRemover
|
|-FileRemover.py
|
|-FileRemoverOutput.txt
|
|-ReadMe.md
|
|-DinFolder
    |
    |-text.txt (slettet)
    |
    |-billede.png (slettet)
    |
    |-billede.tif (ikke slettet)
    |
    |-billede.jpg (ikke slettet)
    |
    |-mappe.zip (ikke slettet)
    |
    |-fil.tmp (ikke slettet)

ARemover.py fungerer på samme måde som FileRemover.py, men sletter blot filer, hvis navne slutter på "a".

Mappestrukturen vil se sådan ud, efter programmet er kørt:

FileRemover
|
|-ARemover.py
|
|-ARemoverOutput.txt
|
|-ReadMe.md
|
|-DinFolder
    |
    |-text.txt (ikke slettet)
    |
    |-billede.png (ikke slettet)
    |
    |-billedea.tif (slettet)
