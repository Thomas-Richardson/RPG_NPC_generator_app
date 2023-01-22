# RPG_NPC_generator_app
A streamlit applet that I use in my Sci-Fi RPG games. It gives me quick inspiration for non player characters (NPCs) by generating random combinations of physical and personality traits, as well as names, nicknames, and interesting flavours (e.g. "secretly rich" or "heavily cybered up") to make them memorable. 

A video demo can be found here: https://github.com/Thomas-Richardson/RPG_NPC_generator_app/blob/main/S%26V%20NPC%20creator%20demo.mov

I run it locally from my laptop during sessions (just open a terminal, navigate to the folder and type `streamlit run app.py`).

I have come up with custom lists of personality traits, physical traits, clothing and such from scratch. These are txt files that are imported into the app. In theory you could use your own or modify mine to tailor the generator to your own campaign.

It also has an export to markdown function that I use to write NPCs to a markdown file in my personal note system. If the players like a character and I sense they'll make a reappeance, the export button appends them to a file of NPCs in my notes. I can then 

If you think this is cool and want help using it for your games, or have improvements, let me know!

## How to use this app for your own roleplay games

- Download and unzip the folder, or `clone` the repo

- If you're on Windows, install python if you haven't already: https://www.python.org/downloads/

- Open a command prompt if on windows, or a terminal on Mac (if you've never done this, don't be scared!) and type `pip install streamlit` to install streamlit, which is the python software package to build and run apps. then install `dotenv` by typing `pip install python-dotenv` which allows you to specify where to save your NPCs to. 

- Inside the terminal/command prompt (henceforth, terminal), use the `cd` command to navigate to inside the `RPG_NPC_GENERATOR_APP` folder (you may have to look this up)

- Once inside, type into the terminal: `streamlit run app.py`

- The web app will open in a browser window and is ready to use! Note even though it opens in a browser, it doesn't use the internet and will work offline.

- Play around!

- If you export a character it will be exported to a file called "S&V_generated_NPCs.md" in the same folder as the app. 

- If you want it somewhere else, create a file called `.env` and put inside it `EXPORT_LOCATION='filepath'` but replace filepath with the actual file path to where you want it saved. then re-run the app.

- To stop the app, close the browser window **but also go back to the terminal, click on the terminal and press control + C. it will say "Stoppping"**

### Changing the personalities, physical traits and flavours etc.

- Simply go into the `RPG_NPC_GENERATOR_APP` folder, go into the data_files folder and find the relevant .txt file. 

- Change the file to remove things you don't want, or add things you do want. **Crucially, different items should only have a space between them, not commas. Also, if your item has multiple words, they should have dashes between them. e.g. "hard-working"**.
