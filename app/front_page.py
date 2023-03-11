# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 21:39:25 2023

@author: Eugene
"""

import streamlit as st
from read_file import get_comments_from_file 
#import pandas as pd 
import csv

def convert_result(result_to_convert):
    # using csv.writer method from CSV package
    # list of name, degree, score 
    col_names = ["Comment num", "Commentor Last name", "Date", "Commentor First name"] 
         
    #df = pd.DataFrame(result_to_convert, columns = col_names) 
    #csv_file = df.to_csv()
    

      
    with open('GFG', 'w') as f:
          
        # using csv.writer method from CSV package
        write = csv.writer(f)
          
        write.writerow(col_names)
        write.writerows(result_to_convert)   
        
    return f

def show_result(result):
    col1.write("Extracted comments: ")
    col1.write(result)
    
    st.sidebar.markdown("\n")
    
    #csv_file = convert_result(result)

    #st.download_button(
    #    label="Download comments as CSV",
    #    data=f,
    #    file_name='large_df.csv',
    #    mime='text/csv'
    #)
    
       

st.set_page_config(layout="wide", page_title="Get comments from Word file")

st.write("Get comments from Word file")
st.write("Try uploading a file to get all comments. Result can be downloaded as csv")
st.sidebar.write("## Upload and download here")

col1 = st.columns(1)[0]

document = st.sidebar.file_uploader("Upload a word file docx", type=["docx"])
#document = "how_to_use_git.docx"

if document is not None:
    result = get_comments_from_file(document)
    show_result(result)
else:
    show_result("ggg")