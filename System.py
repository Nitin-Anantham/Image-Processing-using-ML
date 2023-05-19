


import streamlit as st
from streamlit_option_menu import option_menu
import cv2



# sidebar for navigation()
with st.sidebar:
    
    selected = option_menu('Image Processing',
                          
                          ['Grey Scale Image',
                           'Resize Image'
                           ],
                          icons=['image-alt','image'],     # Streamlit suppports bootstrap icons 
                          default_index=0)
    
                        # default_index = 0 , 
    

if (selected == 'Grey Scale Image'):
    
    # page title
    st.title('Converting To Grey Scale using ML')
    
    
    # getting the input data from the user
    col1 = st.columns(1)
    
    with col1:
        link = st.text_input('Enter The Image Address')
        
   
    
    
    
    
    # creating a button for Prediction
    
    if st.button('Convert'):
        img = cv2.imread(link)
        grayscale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    st.success(cv2_imshow(grayscale_image))




