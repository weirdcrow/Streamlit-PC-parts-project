import streamlit as st
import PIL
from PIL import Image

price5 = []

def button21():
    if st.button('view price', key = 21):
        price5.append(59.99)
        st.write("The price is $59.99")

def button22():
    if st.button('view price', key = 22):
        price5.append(129.99)
        st.write("The price is $129.99")

def button23():
     if st.button('view price', key = 23):
        price5.append(199.99)
        st.write("The price is $199.99")
         
def button24():
    if st.button('view price', key = 24):
        price5.append(169.99)
        st.write("The price is $169.99")

def button25():
    if st.button('view price', key = 25):
        price5.append(139.99)
        st.write("The price is $139.99")

def render():
    st.title("Welcome to the PC case page")
    st.text("Here you will find different PC cases with their specs and prices.")

def display_cheap_case():
    st.header("Montech X3 Mesh Tempered Glass ATX Mid-Tower Computer Case - Black")
    cheap_case = Image.open('C:/Users/anjustice/Documents/pc_parts_folder/cheap_computer_case.jpg')
    st.image(cheap_case, caption='')
    if st.button("View specs", key = 50):
        st.markdown("ATX, Mid-Tower, 3 x 140mm RGB, 3 x 120mm RGB Fans, Liquid Cooling Ready, Steel Frame, Tempered Glass Side Panel,7 x Slots; 2 x Internal 2.5 in, Drive Bays; 1 x Internal 3.5 in Drive Bays")

def display_mid_case():
    #129.99
    st.header("NZXT H5 Flow Tempered Glass ATX Mid-Tower Computer Case - Black")
    mid_case = Image.open('C:/Users/anjustice/Documents/pc_parts_folder/computercase1.jpg')
    st.image(mid_case, caption='')
    if st.button("View specs", key = 51):
        st.markdown("ATX, Mid-Tower, 2 x 120mm Fans, Liquid Cooling Ready, Steel Frame, Tempered Glass Side Panel, 7 x Slots; 2 x Internal 2.5in Drive Bays; 1 x, Internal 3.5in Drive Bays")

def display_expensive_case():
    #199.99
    st.header("HYTE Y60 Modern Aesthetic Dual Chamber Panoramic Tempered Glass Mid-Tower ATX Computer Gaming Case - Black - PCIe 4.0 Riser Cable Included")
    expensive_case = Image.open('C:/Users/anjustice/Documents/pc_parts_folder/computercase2.jpg')
    st.image(expensive_case, caption='')
    if st.button("View specs", key = 52):
        st.markdown("ATX, Mid-Tower, 3 x 120mm Fans, Liquid Cooling Ready, Steel Frame, Tempered Glass Side Panels, 2 x Internal 3.5in Drive Bays; 2 x Internal, 2.5in, Drive Bays; 9 x Slots")

def display_case():
    #169.99
    st.header("Fractal Design North Tempered Glass ATX Mid-Tower Computer Case - White/Oak")
    case = Image.open('C:/Users/anjustice/Documents/pc_parts_folder/computercase3.jpg')
    st.image(case, caption='')
    if st.button("View specs", key = 53):
        st.markdown("ATX, Mid-Tower, 2 x 140mm Fans, Liquid Cooling Ready, Steel Frame, 7 x Slots; 3 x Internal 3.5in Drive Bays; 2 x Internal 2.5in Drive Bays")

def display_case2():
    #139.99
    st.header("Corsair iCUE 4000D RGB AIRFLOW Tempered Glass ATX Mid-Tower Computer Case - Black")
    case2 = Image.open('C:/Users/anjustice/Documents/pc_parts_folder/computercase4.jpg')
    st.image(case2, caption='')
    if st.button("View specs", key = 54):
        st.markdown("ATX, Mid-Tower, 3 x 120mm RGB Fans, Liquid Cooling Ready, Steel Frame, Tempered Glass Side Panel, 2 x Internal 3.5in Drive Bays; 2 x Internal 2.5in Drive Bays; 9 x Slots")

render()
display_cheap_case()
button21()
display_mid_case()
button22()
display_expensive_case()
button23()
display_case()
button24()
display_case2()
button25()

