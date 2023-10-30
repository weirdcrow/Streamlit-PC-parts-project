import streamlit as st
from PIL import Image

def render():
    st.title("Welcome to the hard drive page")
    st.text("Here you will find different hard drives with their specs and prices.")

price2 = []

def button6():
    if st.button('view price', key = 6):
        price2.append(49.99)
        st.write("The price is $49.99")

def button7():
    if st.button('view price', key = 7):
        price2.append(119.99)
        st.write("The price is $119.99")

def button8():
     if st.button('view price', key = 8):
        price2.append(224.99)
        st.write("The price is $224.99")
         
def button9():
    if st.button('view price', key = 9):
        price2.append(129.99)
        st.write("The price is $129.99")

def button10():
    if st.button('view price', key = 10):
        price2.append(74.99)
        st.write("The price is $74.99")

def display_hard_drive1():
    st.header("Seagate BarraCuda 1TB 5400 RPM SATA III 6Gb/s 2.5 in Internal SMR Hard Drive")
    hard_drive1 = Image.open('./hard_drive1.jpg')
    st.image(hard_drive1, caption='')
    if st.button("View specs", key = 36):
        st.markdown("2.5in , SATA 3.0 6.0Gb/s, 5,400 RPM, 128MB")

def display_hard_drive2():
    st.header("Seagate BarraCuda 8TB 5400 RPM SATA III 6Gb/s 3.5 in OEM Internal SMR Hard Drive")
    hard_drive2 = Image.open('./hard_drive2.jpg')
    st.image(hard_drive2, caption='')
    if st.button("View specs", key = 37):
        st.markdown("3.5in, SATA 3.0 6.0Gb/s, 5,400 RPM, 256MB")

def display_hard_drive3():
    st.header("Seagate FireCuda 8TB 7200 RPM SATA III 6Gb/s 3.5 in Internal CMR Hard Drive")
    hard_drive3 = Image.open('./hard_drive3.jpg')
    st.image(hard_drive3, caption='')
    if st.button("View specs", key = 38):
        st.markdown("3.5 in, SATA 3.0 6.0Gb/s, 7,200 RPM, 256MB")

def display_hard_drive4():
    st.header("Seagate FireCuda 4TB 7200 RPM SATA III 6Gb/s 3.5 in Internal CMR Hard Drive")
    hard_drive4 = Image.open('./hard_drive4.jpg')
    st.image(hard_drive4, caption='')
    if st.button("View specs", key = 39):
        st.markdown("3.5 in, SATA 3.0 6.0Gb/s, 7,200 RPM, 256MB")

def display_hard_drive5():
    st.header("Seagate Barracuda 2TB 5400 RPM SATA III 6Gb/s 2.5 in Internal SMR Hard Drive")
    hard_drive5 = Image.open('./hard_drive5.jpg')
    st.image(hard_drive5, caption='')
    if st.button("View specs", key = 40):
        st.markdown("2.5 in, SATA 3.0 6.0Gb/s, 5,400 RPM, 128MB")

render()
display_hard_drive1()
button6()
display_hard_drive2()
button7()
display_hard_drive3()
button8()
display_hard_drive4()
button9()
display_hard_drive5()
button10()