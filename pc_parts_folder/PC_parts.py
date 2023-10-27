import streamlit as st
from PIL import Image

def welcome():

    st.title("Computer Parts Picker")
    st.header("This website is for building a potential PC. It'll help you compare parts and set a budget.")

def main_image():
    mimage = Image.open('C:/Users/anjustice/Documents/pc_parts_folder/Display_PC.jpg')
    st.image('Display_PC.jpg')

def instructions():
    main_image()
    st.markdown("Each page has info and prices for a certain pc part, denoted by its name. Add the parts you want by clicking on their checkbox and your price will be totaled at the shopping cart.")
    st.markdown("Keep in mind that this website doesn't account for compatibility between parts, it only gives you a glimpse into prices and specs")

def links():
    st.header("Where you can find all the parts on these pages")
    st.write("[Pc cases, graphics cards, and hard drives](https://www.microcenter.com/site/products/computer-parts.aspx)")
    st.write("[Mice](https://www.newegg.com/)")
    st.write("[Keyboards](https://mechanicalkeyboards.com/)")
    st.write("[Fully-built PCs](https://starforgesystems.com/pages/our-creators)")


def main():
    welcome()
    instructions()
    links()

if __name__ == '__main__':
    main()