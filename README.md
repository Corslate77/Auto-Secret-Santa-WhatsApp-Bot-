# 🎅 Auto Secret Santa (WhatsApp Bot)

An automated Python script that randomly pairs participants for a Secret Santa gift exchange and privately messages them their assigned person via WhatsApp.

## 🌟 How It Works
The script uses a "Circle Method" (shuffling the list and assigning each person to the next) to ensure that:
1. No one draws themselves.
2. No one gets left out or creates an infinite loop.
3. Everything remains 100% anonymous (even the person running the script won't know the pairings if they don't look at the console).

It leverages the `pywhatkit` library to open WhatsApp Web and send the automated messages dynamically.

- You must be logged into [WhatsApp Web](https://web.whatsapp.com/) on your default browser.

Install the required library:
pip install pywhatkit
