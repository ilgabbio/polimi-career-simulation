# ARGOVision × POLIMI: anomaly detection in industria

In questo workshop andremo ad esplorare una tecnica molto nota in letteratura, nota come `PatchCore`, per risolvere il task di anomaly detection in un contesto industriale.

## Sommario

1. [Requisiti](#requisiti)
1. [Setup workspace](#setup-workspace)
1. [Descrizione workspace](#descrizione-workspace)
1. [Informazioni utili](#informazioni-utili)
1. [Tasks](#tasks)

## Requisiti

E' necessario:

- Installare `docker` e `docker-compose`
- Scaricare il dataset da [questo link](https://www.mydrive.ch/shares/38536/3830184030e49fe74747669442f0f282/download/420938113-1629952094/mvtec_anomaly_detection.tar.xz) oppure dal [sito ufficiale](https://www.mvtec.com/company/research/datasets/mvtec-ad) (seguendo la prodecura di registrazione).
- Scaricare i modelli pre-trainati (uno per categoria) da questo [link](https://drive.google.com/file/d/1vhuN7mZi19arK6WB6Ri3lvDGax4I14WS/view?usp=share_link)

## Setup workspace

0. Verificare l'installazione di `docker` e `docker-compose`:

    ```sh
    docker --version
    docker compose version
    ```

1. Copiare il dataset (una volta estratto) nella folder `work`

1. Buildare ed avviare l'immagine docker tramite il comando:

    ```sh
    docker compose up
    ```

    Il `docker-compose.yaml` definisce ed espone un servizio `jupyter` al quale è possibile accedere per interagire con la macchina docker e il codice del repository.

    NOTA: nel caso vi fossero errori durante la fase di creazione dell'environement (tramite `pipenv`), è necessario installare l'environment da zero anzichè syncarlo solamente. Per fare ciò, sono sufficienti le seguenti modifiche:

    - Modificare il file `Dockerfile`, sostituendo:

        ```
        COPY Pipfile Pipfile.lock .
        ...
        RUN pipenv sync
        ```

        con 

        ```
        COPY Pipfile .
        ...
        RUN pipenv install
        ```
1. Copiare i modelli pre-trainati (una volta estratti) nella folder `work`

1. Copiare ed incollare il link di accesso al servizio `jupyter` su un browser a scelta

    Il link corretto da selezionare è quello che punta a `localhost` (es., `http://127.0.0.1:8888/tree?token=XXXX`)

## Descrizione workspace

Una volta conclusa la parte di setup dell'environment, avrete a disposizione la folder `work` (montata come *volume*) per interagire con il repository di anomaly detection PatchCore (`patchcore-inspection`) risolvendo i task descritti nella sezione successiva.

## Informazioni utili

Gli script del repository di PatchCore (definiti dentro la folder `bin`) utilizzano di default una GPU.
Dal momento che l'immagine docker non ha accesso a GPU, per lanciare gli esperimenti sfruttando solamente la CPU è sufficiente modificare il parametro `--gpu` degli script interessati, impostando come default una lista vuota (`[]`).

### Utility

Per rendere più semplice l'esecuzione di script python dal jupyter notebook, è possibile utilizzare le utility definite in `/work/utils.py`.

- Esempio 1: eseguire un training

    ```python
    from bin.run_patchcore import main as trainer

    with commandline_args(*get_train_args(...)):
        try:
            trainer()
        except SystemExit:
            print("Done.")
    ```

- Esempio 2: eseguire una valutazione

    ```python
    from bin.load_and_evaluate_patchcore import main as evaluator

    with commandline_args(*get_evaluate_args(...)):
        try:
            evaluator()
        except SystemExit:
            print("Done.")
    ```

Inoltre, è consigliato iniziare dal notebook `workshop.ipynb`, il quale definisce già alcune facilitazioni.

## Tasks

1. Effettuare un training (o fitting) con l'algoritmica di `PatchCore` scegliendo un numero arbitrario di categorie di oggetti e dimensione dell'immagine*

1. Effettuare una valutazione (tramite l'apposito script) con l'algoritmica di `PatchCore` partendo dai modelli ottenuti dal training precedente

1. Produrre una distribuzione sugli score di tutte le classi disponibili
    - Utilizzare i risultati (`results.csv`) del modello `step1/0000` all'interno della folder `experiments`
    - I modelli sono stati fittati utilizzando una dimensione dell'immagine pari a 224x224

1. Analizzare le maschere di anomalia che vengono prodotte sulle immagini di test su una categoria a scelta:
    - Modificare il codice affinchè lo script di *evaluate* salvi predizioni, ground-truth (sia pixelwise che imagewise), 
      nome delle immagini e threshold di anomalia per ogni categoria scelta
    - Effettuare una valutazione utilizzando il corrispondente modello pre-trainato, estraendo i dati sopra riportati
    - Produrre degli istogrammi sugli score pixelwise e imagewise dove si confrontano gli score relativi a immagini con difetti e senza
        - Per il caso pixelwise, aggiungere al plot la soglia ottima di anomalia scelta dall'algoritmo

1. Identificare la categoria con le performance peggiori, utilizzando i risultati del modello pre-trainato sopra indicato
    - Ordinare gli esempi della peggiore categoria in base ad una metrica di riferimento tra quelle disponibili
    - Identificare gli N esempi peggiori, con N a piacere*
    - Plottare gli N esempi peggiori, mostrando: immagine originale, anomaly mask, anomaly mask binarizzata, e ground-truth

1. Ripetere il punto precedente, questa volta prendendo la categoria e gli N esempi migliori.

1. Trainare dei modelli di anomaly detection variando la dimensione dell'immagine in input in un range a piacere*
    - Scegliere un numero arbitrario di categorie*
    - Produrre un grafico che metta a confronto le performance al variare della dimensione dell'immagine, scegliendo una metrica di riferimento

\* In base al tempo computazionale e alle risorse di calcolo a disposizione
