

from PIL import Image
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
    
def convert(inp_img):
    img_gray = cv2.cvtColor(inp_img , cv2.COLOR_BGR2GRAY)
    return(img_gray)
    
    
    
    

if (selected == 'Grey Scale Image'):
    
    # page title
    st.title('Converting To Grey Scale using ML')
    st.write("This Web App is to convert your Rgb Pictures to GrayScale Images")
    
   file_image = st.sidebar.file_uploader("Upload Your Photo",type = ['jpeg','jpg','png'])
        
   if file_image is None:
          st.write("Please Upload Your Image File")
    
    
    
    
    # creating a button for Prediction
    
    if st.button('Convert'):
        img = Image.open(file_image)
        grayscale_image = convert(np.array(input_img))
        
        st.image(grayscale_image, caption='processed image')
        st.success("Processing Completed")
     
    if st.button("Download Sketch Images"):
        im_pil = Image.fromarray(grayscale_image)
        im_pil.save('final_image.jpeg')
        st.write('Download completed')


