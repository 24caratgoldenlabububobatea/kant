# Akademiet Kantine Nettside

## Prosjektbeskrivelse

Dette prosjektet er en nettside for Akademiet VGS sin skolekantine.  
Nettsiden lar brukere se hva som serveres i kantina hver dag, hvilke faste varer som alltid er tilgjengelige, og inneholder kontaktinformasjon til kantinen.

Nettsiden er bygget ved hjelp av Flask (Python) på backend og HTML, CSS og Jinja2 på frontend. Flask brukes til å vise riktig meny basert på hvilken dag det er, mens HTML og CSS håndterer utseende og struktur.

### Viktige funksjoner

- Automatisk visning av dagens meny basert på ukedag  
- Viser faste varer som alltid er tilgjengelige  
- Egen side med kontaktinformasjon til kantinen  
- Bilder av matvarer vises dynamisk via Jinja2  
- Enkel og tydelig visuell profil i tråd med Akademiet

---

## Hvordan kjøre programmet

1. Installer Python 3.10 eller nyere.  
2. Installer Flask: pip install flask  
3. Start prosjektet: flask run  
4. Åpne nettleseren og gå til: http://127.0.0.1:5000

Merk: Prosjektet bruker bilder fra static/bilder og CSS fra static/css. Disse må ligge i samme mappe som app.py for at alt skal fungere.

---

## Filstruktur

Hovedfiler og mapper:

- app.py – Flask-backend med ruting og logikk  
- /static/css/ – Stilark for hele nettsiden  
- /static/bilder/ – Bildefiler brukt på nettsiden  
- /templates/base.html – Grunnlayout for alle sider  
- /templates/meny.html – Dagens meny  
- /templates/varer.html – Faste varer og ukens retter  
- /templates/kontakt.html – Kontaktinformasjon  

---

## Litteraturliste / Kildeliste

- Flask-dokumentasjon (https://flask.palletsprojects.com/)  
- W3Schools HTML og CSS (https://www.w3schools.com/)  
- Bennett Feely Clippy (https://bennettfeely.com/clippy/) – brukt til å lage CSS-former  
- ChatGPT – brukt til forklaringer, strukturering av kode og feilsøking  
- Stack Overflow – brukt ved enkelte små feilrettinger

Bilder:  
Alle bilder brukt på nettsiden er enten eid av Akademiet eller merket som Creative Commons og kan brukes fritt.

---

## Brukertesting og tilbakemeldinger

Nettsiden ble testet av elever ved Akademiet VGS for å sikre at innholdet var lett å finne og at menyer fungerte på mobil og PC.  
Tilbakemeldingene var at designet var oversiktlig og at menyen var lett å forstå.  
Etter testing ble mellomrom, tekstjustering og bildeplassering forbedret.

---

## Sikkerhetsprinsipper

- Ingen brukerinndata lagres eller sendes videre  
- Flask brukes kun til å vise statisk informasjon; prosjektet samler ikke personopplysninger  
- Filstier brukes via Flask sin url_for-funksjon for å unngå hardkodede lenker  
- Ingen eksterne skript som kan påvirke sikkerheten lastes inn

---

Laget av: [Ditt navn]  
For: Akademiet VGS  
© 2025 – Alle rettigheter forbeholdt.
