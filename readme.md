# **Projekto tkslas**
Šio projekto tikslas yra naudojant RAG (Retrieval-Augmented Generation) sukurti web aplikaciją kurioje klientas gali atlikti šiuos veiksmus:
- Pateikęs PDF formato dokumentą aplikacijai, gali pateikti užklausas ir gauti atsakymus susijusius su pateiktu dokumentu.
- Filmų rekomendavimo sistema. Joje klientas parašęs kokio tipo filmą jis nori pasižiūrėti, sistema jam parenka 3 filmus labiausiai atitnkančius pagal pateikta užklausą. 

## **Trumpas kiekvieno projekto aprašymas**
### **Filmų rekomendavimo sistema**
Klientas gali pateikti savo failą su filmais, tačiau jis turi atitikti standartizuotą struktūrą. Priimamų failų plėtiniai yra `.csv, .xlsx, .docx`.\
Failas yra nuskaitomas ir išsaugomas `FAISS` duomenų bazėje.\
Kai failas yra nuskaitytas ir išsaugotas, galima pateikti užklausas ir gauti rekomendacijas.\
Jei failas nėra pateikiamas galima naudotis prieš tai išsaugota informacija. Viskas yra atliekama taip pat rašant užklausas tam skirtame lange.\
Duomenys yra paimti iš viešai pasiekiamo šaltinio `https://www.kaggle.com/`

### **PDF failo užklausų sistema** 
Klientas įkelia pdf dokumentą į web aplikaciją. Aplikacija jį suskaldo į duomenų dalis ir paverčia vektoriais kuriuos įrašo į duomenų bazę.\
Šiame projekte naudojamas `llama3.2:3b` modelis atsakymams generuoti.\
Vartotojo užklausa yra apdorojama ir grąžinamas atsakymas. 

## **Kaip pradėti projektą**
Čia bus paaiškita, kai inicijuoti projektą.
1. Rekomenduotija sukurti virtualią aplinką. Terminale veskite `python -m venv .venv`. Taip pat galite rinkstis kitą alternatyvą. 
2. Instaliuokite reikalingas bibliotekas, tai galite padaryti terminale vesdami `pip install -r requirements.txt`. 
3. Kai viskas yra suinstaliuota paleidžiame aplikaciją, terminale vedame `streamlit run main.py`

Po šios komados terminale atsiras nuorodos ir interneto naršyklėje atsiras naujas langas su aplikacija. Jei naršyklėje neatsiranda aplikacija terminale paspauskite su pelyte ant nuorodos. 
