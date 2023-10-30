import streamlit as st
from PIL import Image
def welcome2():
    st.title("Welcome to the mechanical keyboards page")
    st.text("Here you will find different keyboards with their specs and prices.")


price3 = []

def button11():
    if st.button('view price', key = 11):
        price3.append(139.00)
        st.write("The price is $139.00")

def button12():
    if st.button('view price', key = 12):
        price3.append(129.00)
        st.write("The price is $129.00")

def button13():
     if st.button('view price', key = 13):
        price3.append(119.00)
        st.write("The price is $119.00")
         
def button14():
    if st.button('view price', key = 14):
        price3.append(129.00)
        st.write("The price is $129.00")

def button15():
    if st.button('view price', key = 15):
        price3.append(129.00)
        st.write("The price is $129.00")

def kb_image():
    ImageK1 = Image.open('./Ducky_x_MK_Strawberry.jpg')
    st.image('Ducky_x_MK_Strawberry.jpg')

def kb1_info():
    st.header("Ducky x MK Strawberry Frog One 3 Mini Hotswap 60% RGB Keyboard w/ Quack Mechanics")
    kb_image()
    if st.button("View specs", key = 41):
        st.markdown("Ducky x MK designed Limited Edition Strawberry Frog One 3 Mini Beautiful Strawberry Frog artwork exclusive to the first production round only! Incredible XDA profile PBT keycaps with Dye Sub print Strawberry Frog themed keypuller and braided USB-C cable Dual layer hotswap PCB w/ Kailh yellow hotswap sockets QUACK Mechanics with dual-layer high-grade silicone and EVA foam sound dampeners Improved PCB design, V2 stabilizers, remapped macro layout, and per-key programmable RGB")
        

def kb2_image():
    KBImage2 = Image.open('./Ducky_One_3_SF.jpg')
    st.image('Ducky_One_3_SF.jpg')

def kb2_info():
    st.header("Ducky One 3 SF Aura Clear White 65% Hotswap RGB LED Double Shot ABS Mechanical Keyboard")
    kb2_image()
    if st.button("View specs", key = 42):
        kbspecs2 = st.markdown("Featuring Ducky's all new QUACK Mechanics design philosophy Dual layer PCB w/ exclusive Kailh yellow hotswap sockets Equipped with dual-layer high-grade silicone and EVA foam sound dampeners Thick PBT Double Shot AC-style keycaps (translucent sides with opaque tops and white legends) Per-key programmable RGB 3-level adjustable feet and detachable braided USB-C cable Improved PCB design, V2 stabilizers, and remapped macro layout")

def kb3_image():
    image3 = Image.open('./Ducky_One_3_Fuji_Hotswap.jpg')
    st.image('Ducky_One_3_Fuji_Hotswap.jpg')

def kb3_info():
    st.header("Ducky One 3 Fuji Hotswap Double Shot PBT QUACK Mechanical Keyboard")
    kb3_image()
    if st.button("View specs", key = 43):
        st.markdown("Featuring Ducky's all new QUACK Mechanics design philosophy Dual layer Hotswap PCB w/ exclusive Kailh yellow hotswap sockets Equipped with dual-layer, high-grade silicone and EVA foam sound dampeners Thick, PBT Double-shot seamless keycaps 3 level adjustable feet and detachable braided USB-C cable Improved PCB design, V2 stabilizers, and remapped macro layout")

def kb4_image():
    Image4 = Image.open('./MK_Duo.jpg')
    st.image('MK_Duo.jpg')
    
def kb4_info():
    st.header("MK Duo 60% XT Keyboard w/ MK Dose Dual Contact Mechanical Switches")
    kb4_image()
    if st.button("View specs", key = 44):
        st.markdown("specs: Equipped with MK Dose switches: the market's only Dual Contact keyboard switch. Choose one of four modes per switch: speed, typist, agile (tactile dual-actuation), or parallel (tactile dual actuation). Unique 60% XT layout is designed to maximize keys near your left hand. Works with Duo software designed to maximize Dose switch functionality in Windows, Mac, and Linux Allows up to four profiles: one preset layer and three programmable layers Heavy, high-end construction with PBT keycaps, clean lines, and seamless finish")

def kb5_image():
    image5 = Image.open('./Varmilo_x_MK_Glintstone.jpg')
    st.image('Varmilo_x_MK_Glintstone.jpg')

def kb5_info():
    st.header('Varmilo x MK Glintstone Minilo VXT67 65% Hotswap Triple Mode Bluetooth + Wireless 2.4 GHz RGB Mechanical Keyboard')
    kb5_image()
    if st.button("View specs", key = 45):
        st.markdown("Triple mode - wired with USB-C cable, Bluetooth 5.1, and 2.4 GHz Per-key RGB backlighting 1.5mm thick ABS Double Shot keycaps Flashing indicator light warns of low battery and Escape key lights up while charging Features Type-Cool sound dampening Indicator lights next to arrows for Caps Lock and F-row function Connect up to 3 devices wirelessly NKRO in wired mode and 6 key rollover in wireless mode Hotswap sockets New, MK-exclusive colorway of the popular Minilo series 1000 Hz polling rate when using wired or with 2.4 GHz")

def showpageKB():
    welcome2()
    kb1_info()
    button11()
    kb2_info()
    button12()
    kb3_info()
    button13()
    kb4_info()
    button14()
    kb5_info()
    button15()

showpageKB()