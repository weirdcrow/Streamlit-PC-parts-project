import streamlit as st
from PIL import Image
def welcome2():
    st.title("Welcome to the completely built PCs page")
    st.text("Here you will find different PCs with their specs and prices.")

price6 = []

def button26():
    if st.button('view price', key = 26):
        price6.append(1149.99)
        st.write("The price is $1,149.99")

def button27():
    if st.button('view price', key = 27):
        price6.append(1749.99)
        st.write("The price is $1,749.99")

def button28():
     if st.button('view price', key = 28):
        price6.append(2499.99)
        st.write("The price is $2,499.99")
         
def button29():
    if st.button('view price', key = 29):
        price6.append(2899.99)
        st.write("The price is 2,899.99")

def pc1_image():
    pcimage1 = Image.open('./Horizon_II.jpg')
    st.image('Horizon_II.jpg')

def pc1_info():
    st.header("Horizon II")
    pc1_image()
    if st.button("View specs", key = 55):
        st.markdown("Specs: CPUIntel Core i5-12400 / CPU CoolerDeepcool AK400 Air Cooler / RAMTeamgroup Delta RGB 16GB DDR4 3600 CL18 (2x8GB) / Graphics CardAMD Radeon™ RX 6650 XT 8GB / MotherboardMSI Pro B660m-a CEC Wifi / Storage1TB Teamgroup Z44A5 PCIe 4.0 NVME / CablesCableMod Pro ModMesh Sleeved Cable Extensions (Black) / Power Supply MSI MPG A650GF Gold / RGB Fans3 Deepcool a-RGB Fans / CaseDeepcool CG560 Mid-Tower (Black) / Op. SystemWindows 11 Home")

def pc2_image():
    Image2 = Image.open('./h2super_hero.jpg')
    st.image('h2super_hero.jpg')

def pc2_info():
    st.header("Horizon II SUPER")
    pc2_image()
    if st.button("View specs", key = 56):
        st.markdown("Specs: CPUIntel Core i5-13600K / CPU CoolerDeepcool LS520 240mm Liquid Cooler / RAMTeamgroup / Delta RGB 32GB DDR5 6000 CL38 (2x16GB) / RGB Fans5 Deepcool a-RGB Fans / Graphics CardGeForce RTX™ 4060 Ti 8GB / MotherboardMSI Pro Z790-A Wifi / Storage1TB Teamgroup Z44A5 PCIe 4.0 NVME / CablesCableMod Pro ModMesh Sleeved / Cable Extensions (Black) / Power SupplyMSI MPG A750GF Gold / CaseDeepcool CK560 Mid-Tower ATX (Black) / Op. SystemWindows 11 Home")

def pc3_image():
    image3 = Image.open('./SENTINELHERO.jpg')
    st.image('SENTINELHERO.jpg')

def pc3_info():
    st.header("The Sentinel")
    pc3_image()
    if st.button("View specs", key = 57):
        st.markdown("Specs: The Sentinel PC Benchmark Testing / Tech Specs / CPUIntel Core i5-13600K / CPU CoolerDeepcool LS720 360mm AIO / Liquid Cooler / RAMTeamgroup Delta RGB 32GB DDR5 6000 CL38 (2x16GB) \ MotherboardMSI Z790 Tomahawk Wifi DDR5 \ Graphics CardGeForce RTX™ 4070 Ti 12GB \ CablesCableMod Pro ModMesh Sleeved Cable Extensions (Black) \ Primary Storage 1TB Teamgroup Z44A5 PCIe 4.0 NVME \ Power SupplyMSI MPG A850G Gold PCIe 5 \ RGB Fans6 x Deepcool FC 120mm \ CaseLian Li PC-011 Dynamic Evo Mid-Tower (Black) \ Add. ComponentsStarforge Platelight \ Op. SystemWindows 11 Home")

def pc4_image():
    Image4 = Image.open('./vc-hero.jpg')
    st.image('vc-hero.jpg')
    
def pc4_info():
    st.header("Voyager Creator")
    pc4_image()
    if st.button("View specs", key = 58):
        st.markdown("specs: CPUIntel Core i7-13700K / CPU CoolerDeepcool LS720 360mm AIO Liquid Cooler / RAMTeamgroup Delta RGB 32GB DDR5 6000 CL38 (2x16GB) / MotherboardMSI Z790 Tomahawk Wifi DDR5 / Graphics / CardGeForce RTX™ 4070 Ti 12GB / CablesCableMod Pro ModMesh Sleeved Cable Extensions (Black) / Primary Storage2TB / Kingston KC3000 PCIe 4.0 NVME / Secondary Storage2TB Teamgroup Z44A5 PCIe 4.0 NVME / Power SupplyMSI MPG A850G / Gold PCIe 5 / RGB Fans6 x Deepcool FC 120mm / CaseLian Li PC-011 Dynamic Evo Mid-Tower (Black) / Add. ComponentsStarforge Platelight / Op. SystemWindows 11 Home")


def showpage():
    welcome2()
    pc1_info()
    button26()
    pc2_info()
    button27()
    pc3_info()
    button28()
    pc4_info()
    button29()

showpage()