import streamlit as st
from PIL import Image
def welcome2():
    st.title("Welcome to the graphics card page")
    st.text("Here you will find different graphics cards with their specs and prices.")


price = []

def button1():
    if st.button('view price', key = 1):
        price.append(799.99)
        st.write("The price is $799.99")

def button2():
    if st.button('view price', key = 2):
        price.append(2199.99)
        st.write("The price is $2,199.99")

def button3():
     if st.button('view price', key = 3):
        price.append(549.99)
        st.write("The price is $549.99")
         
def button4():
    if st.button('view price', key = 4):
        price.append(1819.99)
        st.write("The price is $1,819.99")

def button5():
    if st.button('view price', key = 5):
        price.append(799.99)
        st.write("The price is $799.99")


def gcard1_image():
    image1 = Image.open('C:/Users/anjustice/Documents/pc_parts_folder/asus_nvidia.jpg')
    st.image('asus_nvidia.jpg')

def gcard1_info():
    st.header("Gigabyte NVIDIA GeForce RTX 4070 Ti Windforce Overclocked Triple Fan 12GB GDDR6X PCIe 4.0 Graphics Card")
    gcard1_image()
    if st.button("View specs", key = 30):
        st.markdown(" Specs:\n 12GB GDDR6X 192-bit Memory \n 7680 x 4320 Maximum Resolution \n PCIe 4.0 \n Full Height, Triple Slot \n DisplayPort 1.4 HDMI 2.1")

def gcard2_image():
    Image2 = Image.open('C:/Users/anjustice/Documents/pc_parts_folder/gigabyte_nvidia.jpg')
    st.image('gigabyte_nvidia.jpg')

def gcard2_info():
    st.header("ASUS NVIDIA GeForce RTX 4090 ROG Strix LC Overclocked Liquid Cooled 24GB GDDR6X PCIe 4.0 Graphics Card")
    gcard2_image()
    if st.button("View specs", key = 31):
        st.markdown("24GB GDDR6X 384-bit Memory \n 7680 x 4320 Maximum Resolution \n PCIe 4.0 \n Full Height, Triple Slot \n DisplayPort 1.4a, HDMI 2.1a")

def gcard3_image():
    image3 = Image.open('C:/Users/anjustice/Documents/pc_parts_folder/zotac_nvidia.jpg')
    st.image('zotac_nvidia.jpg')

def gcard3_info():
    st.header("Zotac NVIDIA GeForce RTX 4070 Twin Edge Spider-Man Across the Spider-Verse Bundle Overclocked Dual Fan 12GB GDDR6X PCIe 4.0 Graphics Card")
    gcard3_image()
    if st.button("View specs", key = 32):
        st.markdown("specs:\n12GB GDDR6X 192-bit Memory \n7680 x 4320 Maximum Resolution \nPCIe 4.0 \nFull Height, Dual Slot \nDisplayPort 1.4a, HDMI 2.1")

def gcard4_image():
    Image4 = Image.open('C:/Users/anjustice/Documents/pc_parts_folder/ASUS_NVIDIA_GeForceRTX4090.jpg')
    st.image('ASUS_NVIDIA_GeForceRTX4090.jpg')
    
def gcard4_info():
    st.header("ASUS NVIDIA GeForce RTX 4090 TUF Gaming Overclocked Triple Fan 24GB GDDR6 PCIe 4.0 Graphics Card")
    gcard4_image()
    if st.button("View specs", key = 33):
        st.markdown("specs: \n24GB GDDR6X 384-bit Memory \n 7680 x 4320 Maximum Resolution \n PCIe 4.0 \n Full Height, Quad Slot \n DisplayPort 1.4a, HDMI 2.1a")

def gcard5_image():
    image5 = Image.open('C:/Users/anjustice/Documents/pc_parts_folder/EVGA_NVIDIA.jpg')
    st.image('EVGA_NVIDIA.jpg')

def gcard5_info():
    st.header('EVGA NVIDIA GeForce RTX 3080 Ti FTW3 Ultra Gaming Triple-Fan 12GB GDDR6X PCIe 4.0 Graphics Card (Refurbished)')
    gcard5_image()
    if st.button("View specs", key = 34):
        st.markdown("specs \n12GB GDDR6X 384-bit Memory \n7680 x 4320 Maximum Resolution \nPCIe 4.0 \nFull Height, Triple Slot \nDisplayPort 1.4a, HDMI 2.1")

def showpage():
    welcome2()
    gcard1_info()
    button1()
    gcard2_info()
    button2()
    gcard3_info()
    button3()
    gcard4_info()
    button4()
    gcard5_info()
    button5()

showpage()