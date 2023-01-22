import streamlit as st
import random as rd
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(layout="wide")

# =========== Functions ====================================

@st.cache # don't re-import data every time the app re-runs
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

def generate_colour():
    colour = rd.sample(colours_list,1)
    return colour

def select_location():
    location = rd.sample(locations_list,1)
    return location

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
colours_list = import_data('data_files/colours.txt')
locations_list = import_data('data_files/locations.txt')

# ========== APP =============================

"# Scum and Villainy NPC creator"

create_character_button = st.button("Create NPC")

if create_character_button:
    description = generate_NPC()
    st.session_state['character_description'] = description

# This is so the description you generate doesn't disappear if you click other buttons
if 'character_description' in st.session_state:
    st.markdown(st.session_state['character_description']) # basically, if you generated an NPC, print that NPC

col1a, col2a = st.columns(2)
col1b, col2b = st.columns(2)


# Button for giving you a random extra flavour
generate_flavour_button = col1a.button("Give me an extra flavour")

if generate_flavour_button:
    new_flavour = generate_extra_flavour()
    st.session_state['generated_flavour'] = new_flavour[0]
    col1a.write(st.session_state['generated_flavour'])
     
# Button for giving you a random faction
generate_faction_button = col2a.button("Give me a random faction")

if generate_faction_button:
    faction = select_faction()
    st.session_state['generated_faction'] = faction[0]
    col2a.write(st.session_state['generated_faction'])

# Button for giving you a random colour
generate_colour_button = col1b.button("Need a random colour for clothes skin, hair etc?")

if generate_colour_button:
    colour = generate_colour()
    st.session_state['generated_colour'] = colour[0]
    col1b.write(st.session_state['generated_colour'])
    
# Button for giving you a random location
generate_location_button = col2b.button("Sample random sub-system")

if generate_location_button:
    location = select_location()
    st.session_state['generated_location'] = location[0]
    col2b.write(st.session_state['generated_location'])

# Exporting 
if 'character_description' in st.session_state:
    NPC_to_export = st.session_state['character_description']
    NPC_to_export = NPC_to_export.replace('.\n','.')

    export_character_button = st.download_button(label = 'Download',
                                                data = NPC_to_export, 
                                                file_name = 'character.txt')