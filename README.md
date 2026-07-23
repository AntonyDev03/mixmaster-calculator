# MixMaster DIY - E-Liquid Calculator 🧪

Un'applicazione web Full-Stack per il calcolo preciso delle miscele di liquidi fai-da-te, progettata per gestire calcoli di diluizione complessi e prevenire input fisicamente impossibili.

## 🎯 Obiettivo del Progetto
Questo progetto nasce per risolvere un problema matematico e logico reale nel mondo del mixing fai-da-te: calcolare i millilitri esatti di base neutra, aroma e nicotina necessari per ottenere una specifica concentrazione finale. 

Oltre al calcolo base, l'applicazione integra un sistema di validazione per proteggere l'utente dai "casi limite" (es. richiedere concentrazioni di nicotina o aroma che superano il volume fisico della boccetta).

## 🛠️ Tecnologie Utilizzate
- **Backend:** Python, Django (strutturazione API RESTful)
- **Frontend:** Vanilla JavaScript (ES6), HTML5
- **Styling:** Tailwind CSS (UI moderna e pienamente responsiva)
- **Comunicazione:** Fetch API (gestione asincrona delle richieste)

## 🚀 Funzionalità Tecniche Principali

1. **Comunicazione Asincrona (Single Page Application feel):**
   L'interfaccia utente comunica con il backend Django tramite chiamate `fetch` asincrone. I risultati vengono renderizzati manipolando il DOM dinamicamente, senza mai ricaricare la pagina web, garantendo un'esperienza utente fluida.

2. **Validazione Logica Client-Side (Edge Cases):**
   Prima di inoltrare la richiesta al server, un algoritmo JavaScript analizza gli input per verificare che la matematica di base sia fisicamente realizzabile. Se la somma degli ingredienti richiesti supera lo spazio nel contenitore, il sistema blocca la chiamata API e restituisce un alert formattato, risparmiando risorse lato server.

3. **Backend API Custom:**
   Il calcolo intensivo è delegato alla logica di business in Python (`logic.py`), esposta tramite un endpoint dedicato in Django che riceve parametri `GET` e restituisce i risultati formattati in JSON.

## 💡 Cosa ho imparato da questo progetto
Questo progetto mi ha permesso di consolidare le competenze pratiche sul dialogo tra Frontend e Backend. In particolare, mi sono focalizzato su:
* La gestione delle `Promise` in JavaScript (`.then`, `.catch`).
* L'isolamento della logica di business dal routing in Django.
* La gestione degli errori preventivi per migliorare la UX.