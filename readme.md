# **RAG PROJEKTAS**

## **Projekto tikslas**
Sukurti veikiantį RAG (retrieval-augmented-generation) sprendimą, leidžianti užduoti klausimus ir gauti atsakymus rementis pateiktais PDF dokumentais. 

## **Projekto eigos planas**
1. Nuskaityti dokumentus 
2. 


## **Projekto aprašymas**
Šiam projektui naudosime mokslinį straipsnį iš `researchgate.net` svetainės.\ 
Straipsnyje yra aprašyta `Tick Tock` aplikacijos daroma žala. 

The_Impact_of_College_Students_Using_TikTok_on_Th

Pateiktą straipsnį nuskaitome 



# **Pasiaiskinti** 
Kodel split = text_spit.split_text("\n\n".join(pdf_text)) kai pridejau join dali suveike??

Kuo skiriasi dockument ir text vector_db = Chroma.from_documents(documents=split, embedding=embedding)


# **Duomenų valymo darbai**
1. Overwiev - paziureti kiek yra maziausi simboliu kiekiai ir juos istrinti 
2. Patikrinti metus ir jei nera nurodytu istrinti eilute, taip pat paziureti nuo maziausiu iki didžiausiu 
3. 