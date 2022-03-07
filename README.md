# Slack_App
### Bot Slack per la compilazione della richiesta di ferie attraverso l'interfaccia della famosa app di messaggistica

## Steps di Creazione dell'Applicativo

1) Creare e registrare l’app su https://api.slack.com/apps/

2) Installare l'app appena creata sul workspace Slack di riferimo attraverso la procedura guidata

3) Registrare i token nell'ambiente in modo da poter comunicare via API

4) L’applicativo vero e proprio nella sua fase di sviluppo, utilizza il modulo Flask e ngrok per fare rerouting dell’host su un proxy server e creare endpoint sui quale fare richieste di GET e POST, che vengono usati per comunicare con l'API di Slack.

5) Indicare i seguenti “Scopes” per l’app sul sito di slack in modo che abbia autorizzazione in lettura, scrittura, eventi sulle reazioni e slash commands. <br>
<img width="782" alt="Screenshot 2020-12-29 at 10 44 52" src="https://user-images.githubusercontent.com/76904889/156947237-c56218fc-989e-4a89-9357-6481d1b6db3d.png">

6) Definire sempre sul sito slack uno slash command "/time-off", indicando come URL per una POST request, un endpoint custom, del tipo http://****.ngrok.io/time-off

7) Dichiarare su Flask l’endpoint custom in modo tale da far comunicare i due sistemi. In questo modo, se su Slack viene eseguito il comando "/time-off", viene mandata automaticamente una richiesta di POST sull'endpoint, ritornando un JSON con le info di chi ha eseguito il comando, su che canale lo ha eseguito ecc…

8) Aggiungere l’app al canale di riferimento nel workspace Slack (es: #app-bot-slack)

9) Definire un funzione Python che ad ogni "/time-off", manda una richiesta POST di ritorno all'API Slack con un PAYLOAD, ovvero un JSON che in sostanza contiene le informazioni su come mostrare determinati elementi HTML di grafica come il selettore date, il testo semplice e il bottone da cliccare

10) Sul sito slack nella sezione Interactivity e Shortcuts, registrare un altro endpoint custom in modo da avere un POST in entrata ogni volta che viene effettuata un'interazione con elementi grafici di Slack che prevedono un'azione

11) Definire il collegamento su Python e scrivere una funzione che va a leggere le informazioni delle date selezionate, stabilendo delle condizioni minime per evitare di selezionare date incongruenti o incoerenti

12) Aggiungere una condizione che al click del bottone aggiorna il PAYLOAD mandato in precedenza con il messaggio “Request processed!“. In questo modo le date non saranno più cliccabili e la scelta non potrà più essere modificata

13) Al click del bottone, aggiungere contemporaneamente un "send message" ad un utente amministratore del workspace (nel caso specifico il referente di progetto). Il PAYLOAD ricevuto dall'utente prevede nella sua versione di sviluppo, solo due bottoni uno “YES”e uno “NO”. Se cliccati, mandano un messaggio sul canale collegato (es: #app-bot-slack) informando che la richiesta é stata accettata o rifutata a seconda della scelta dell'utente amministratore.
