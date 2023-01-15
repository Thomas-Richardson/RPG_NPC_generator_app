import streamlit as st
import pandas as pd
import random as rd
import datetime as dt
st.set_page_config(layout="wide")

# =========== Material ====================================

personality_traits_list = ['Kind', 'rude/Obnoxious','loud','annoyed','arrogant, braggart', 'overconfident', 'timid', 'postitive', 'Gloomy', 'anxious', 'apologetic', 'pampered','grim', 'people pleaser', 'unreliable', 'wise','friendly', 'stiff, emotionless','ambitious' ,'busy', 'forceful','curious', 'logical','vain', 'hedonistic', 'absent-minded', 'sarcastic', 'intimidating', 'protective over friends', 'quick to anger', 'wise cracking', 'dramatic','slow', 'mysterious', 'reckless', 'liar', 'organised', 'disorganised']

physical_traits_list = ['attractive','tall','fat','short','thin','muscular','ugly','bulbous nose','thin serpentine lips', 'thick lips','long nose','curly hair','bald','long hair', 'styled hair', 'pale skin','swarthy skin','scar','large eyes','high cheekbones','strong jawline', 'old','young', 'tall forehead','crooked teeth', 'obvious cybernetic',]

clothing_list = ['tattoos','make up','cultural dress','rings','piercings','necklace','punk clothing','suit','armour','torn clothing','fashionable clothing', 'colourful clothing', 'moustache','beard', 'Long coat','Hood or veil','Short cloak','Leathers','']

flavour_list = ['laughs a lot','patriotic: homeworld','piercing eyes of unusual colour', 'double down on one physical trait','double down one personality trait','double down one clothing trait', 'cultural dress','hair dyed a strange colour', 'androgenous', 'blind','wheelchair', 'glowing', 'missing limb, eye or ear', 'urbot', 'religious','anarchist', 'Yaru Clone','secretly rich', 'Working for another faction (click button below)', "former slave", "former soldier", "trademark weapon", "proud of their race",'mask', 'Has an alien pet','graceful','highly educated', 'ostentatious','touchy touchy', 'family oriented']

male_names_list = ['Tobias Jann', 'Fafnir Breton', 'Ferris Zechiel', 'Monty Centrich', 'Thane Bucanan','Ivan Ryant','Brom Carthen','Sterling Quintan','Jaeger Wasrous','Gareth Catlow', 'Ursa Simril','Darius Paulsen','Vidar Allen','Derra Vale','Khan Inas','Jame Bibble','Shin Braze']

female_names_list = ['Eveyln Wynter','Winona Thoran','Felicia Berrett','Freya Mattix','Trinity Sarrat','Lexi Lockley','Derra Vale','Grona Tillo','Nyree Alorr','Jane Dangir', 'Zena Cardinal', 'Miley Nafan','Tala Kale','Lora Halcyon','Jameela Brumen','Mira Das','Ayla Tane','Anillia Brando']

aliases_list = ['Ace', 'Agony', 'Apex', 'Athena', 'Badger', 'Bingo', 'Black', 'Bolt', 'Brakes','Shatter', 'Carrot', 'Cash', 'Cosmo', 'Dash', 'Devil', 'Dipper', 'Echo','Eight', 'Elbows', 'Falcon', 'Fireball', 'Flex', 'Game', 'Gargoyle', 'Gear', 'Gonzo', 'Guns', 'Hammer', 'Headhunter', 'Helo', 'Hex', 'Highball', 'Hyper', 'Intake', 'Iris', 'Iron', 'Juggler', 'Juice', 'Junior', 'Karma', 'Lasher', 'Legend', 'Link', 'Loco', 'Mooch', 'Nails', 'Nemesis', 'Nova', 'Owl', 'Phoenix', 'Quirk', 'Raider', 'Razor', 'Rash', 'Skulls', 'Snaps', 'Snitch', 'Stinger', 'Syndrome', 'Tank', 'Tax', 'Titan', 'Tread', 'Under', 'Vandal', 'Vapor', 'Wraith', 'X-Ray', 'Yellow', 'Zen', 'Zenith', 'Zipper']

race_list = ['white','black','east asian','indo asian', 'black-white mixed']

factions_list = ['Guild of Engineers','Church of Stellar Flame','Counters Guild','Starless Veil','51st Legion','House Malklaith','Isotropa Max Secure', 'Starsmiths Guild', 'Cult of the Seekers',' Hegemonic News Network', 'Yaru (Makers Guild)', 'Concordiat Knights','Lost Legion', 'Scarlet Wolves', 'Vorex', 'Ashen Knives', 'Borniko Syndicate', 'Draxler’s Raiders', 'The Maelstrom', 'Echo Wave Riders', 'Janus Syndicate', 'Turner Society', 'Cobalt Syndicate', 'Dyrinek Gang', 'Wreckers', 'Sah’iir', 'Suneaters',' The Agony', 'Ashtari Cult',' Vignerons', 'Ghosts', 'Mendicants', 'Nightspeakers', 'Acolytes of Brashkadesh', 'Conclave 01', 'Vigilance']

# =========== Functions ====================================

def generate_NPC():
    
    sex = rd.sample(['male','female'],1)[0]    
    
    if sex == 'male':
        names = rd.sample(male_names_list,2)
    elif sex == 'female':
        names = rd.sample(female_names_list,2)
    
    alias = rd.sample(aliases_list,1)[0]    
    physical_appearance = rd.sample(physical_traits_list,2)
    clothing = rd.sample(clothing_list,1)[0]
    race = rd.sample(race_list,1)[0]
    personality = rd.sample(personality_traits_list,2)
    flavour = rd.sample(flavour_list,1)[0]
    
    description  = f"""\n
    NAME OPTIONS: {names}.\n
    ALIAS: {alias}.\n
    PHYSICAL APPEARANCE: {[physical_appearance,sex, race]}.\n
    CLOTHING: {clothing}.\n
    PERSONALITY: {personality}. \n
    FLAVOUR: {flavour}. \n
    OCCUPATION: . \n
    GOALS: .\n
    FACTION: .\n
    RESOURCES: . \n
    NOTES FROM PLAYER INTERACTIONS: .\n
    CREATED DATE: {dt.datetime.now().strftime("%Y-%m-%d %H:%M")}. \n
    """
    return description

def select_faction():
    faction = rd.sample(factions_list,1)
    return faction

def generate_extra_flavour():
    new_flavour = rd.sample(flavour_list,1)
    return new_flavour

# ========== APP =============================

"# Scum and Villainy NPC creator"

create_character_button = st.button("Create NPC")

if create_character_button:
    description = generate_NPC()
    st.session_state['character_description'] = description

# This is so the description you generate doesn't disappear if you click other buttons
if 'character_description' in st.session_state:
    st.markdown(st.session_state['character_description']) # basically, if you generated an NPC, print that NPC

# Button for giving you a random extra flavour
generate_flavour_button = st.button("Give me an extra flavour")

if generate_flavour_button:
    new_flavour = generate_extra_flavour()
    st.session_state['generated_flavour'] = new_flavour[0]
    st.session_state['generated_flavour']
     
# Button for giving you a random faction
generate_faction_button = st.button("Give me a random faction")

if generate_faction_button:
    faction = select_faction()
    st.session_state['generated_faction'] = faction[0]
    st.session_state['generated_faction']

# Exporting 
export_character_button = st.button('Export')

if export_character_button:
    filepath = 'ENTER FILEPATH HERE'
    filename = "S&V_generated_NPCs.md"
    "Saving NPC"
    with open((filepath+filename),'a') as f: # Append the NPC to the file 
        f.write("## <NAME> ") # Add a markdown header
        f.write(st.session_state['character_description']) # add the character