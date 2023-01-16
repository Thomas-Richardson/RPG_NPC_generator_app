import streamlit as st
import pandas as pd
import random as rd
import datetime as dt
st.set_page_config(layout="wide")

# =========== Functions ====================================

@st.cache
def import_data(data_file_name):
    with open(data_file_name, "r") as file:
        data = file.readlines()
        data = [word for line in data for word in line.split()]
    return data

def generate_NPC():
    
    sex = rd.sample(['male','female'],1)[0]    
    
    if sex == 'male':
        names = rd.sample(male_names_list,2)
    elif sex == 'female':
        names = rd.sample(female_names_list,2)
    
    alias = rd.sample(aliases_list,1)[0]    
    physical_appearance = rd.sample(physical_traits_list,2)
    clothing = rd.sample(clothing_list,1)[0]
    race = rd.sample(races_list,1)[0]
    personality = rd.sample(personality_traits_list,2)
    flavour = rd.sample(flavours_list,1)[0]
    
    description  = f"""\n
    NAME OPTIONS: {names}.\n
    ALIAS: {alias}.\n
    PHYSICAL APPEARANCE: {[physical_appearance,sex, race]}.\n
    CLOTHING: {clothing}.\n
    PERSONALITY: {personality}.\n
    FLAVOUR: {flavour}.\n
    OCCUPATION: .\n
    GOALS: .\n
    FACTION: .\n
    RESOURCES: .\n
    NOTES FROM PLAYER INTERACTIONS: .\n
    CREATED DATE: {dt.datetime.now().strftime("%Y-%m-%d %H:%M")}. \n
    """
    return description

def select_faction():
    faction = rd.sample(factions_list,1)
    return faction

def generate_extra_flavour():
    new_flavour = rd.sample(flavours_list,1)
    return new_flavour

# Import the data
personality_traits_list = import_data('data_files/personalities.txt')
physical_traits_list = import_data('data_files/physical_traits.txt')
clothing_list = import_data('data_files/clothing.txt')
flavours_list = import_data('data_files/flavours.txt')
male_names_list = import_data('data_files/male_names.txt')
female_names_list = import_data('data_files/female_names.txt')
aliases_list = import_data('data_files/aliases.txt')
races_list = import_data('data_files/races.txt')
factions_list = import_data('data_files/factions.txt')
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
    filepath = 'FILEPATH HERE'
    filename = "S&V_generated_NPCs.md"
    "Saving NPC"
    NPC_to_export = st.session_state['character_description']
    NPC_to_export = NPC_to_export.replace('.\n','.')
    
    with open((filepath+filename),'a') as f: # Append the NPC to the file 
        f.write("## <NAME> ") # Add a markdown header
        f.write(NPC_to_export) # add the character