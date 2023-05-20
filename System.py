

from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
import cv2
import numpy as np





# sidebar for navigation()
with st.sidebar:
    
    selected = option_menu('Image Processing',
                          
                          ['Grey Scale Image',
                           'Resize Image',
                           'Photo to Cartoon'
                           ],
                          icons=['image-alt','image','vector-pen'],     # Streamlit suppports bootstrap icons 
                          default_index=0)
    
                        # default_index = 0 , 
    
def convert1(inp_img):
    img_gray = cv2.cvtColor(inp_img , cv2.COLOR_BGR2GRAY)
    return(img_gray)
    
def convert2(inp_img,d1,d2):
    img_resized = inp_img.resize((d1,d2))
    
    

if (selected == 'Grey Scale Image'):
    
    # page title
    st.title('Converting To Grey Scale using ML')
    st.write("This Web App is to convert your Rgb Pictures to GrayScale Images")
    
    file_image = st.sidebar.file_uploader("Upload Your Photo",type = ['jpeg','jpg','png'])
        
    if file_image is None:
           st.write("Please Upload Your Image File")
    
    
    
    
    
    
    if st.button('Convert'):
        img = Image.open(file_image)
        grayscale_image = convert(np.array(img))
        
        st.image(grayscale_image, caption='processed image')
        st.success("Processing Completed")
     
    if st.button("Download Sketch Images"):
        im_pil = Image.fromarray(grayscale_image)
        im_pil.save('final_image.jpeg')
        st.write('Download completed')


        
if (selected == 'Resize Image'): 
    st.title('Resize Images using ML')
    st.write("This Web App is to Resize your Images")
    
    file_image = st.sidebar.file_uploader("Upload Your Photo",type = ['jpeg','jpg','png'])
        
    if file_image is None:
           st.write("Please Upload Your Image File")
    
    col1, col2 = st.columns(2)
    
    with col1:
        d1 = st.text_input("Enter Height")
        d2 = st.text_input("Enter Width")
    
    
    if st.button('Resize'): 
    
        img = Image.open(file_image)
        resized_image = convert2(img,d1,d2)
    
        st.image(resized_image, caption='processed image')
        st.success("Processing Completed")
    
    
    if st.button("Download Sketch Images"):
        im_pil = Image.fromarray(resized_image)
        im_pil.save('final_image.jpeg')
        st.write('Download completed')    
    
    
        
