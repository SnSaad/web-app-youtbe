#Imports

import streamlit as st
import pandas as pd
import seaborn as sns

#Title and Subheader
st.title('Data Analysis')
st.subheader('Data Analysis Using Python & Streamlit')

#Upload Dataset
upload = st.file_uploader('Upload Your Dataset (in csv format)')
if upload is not None:
    data = pd.read_csv(upload)
    
#Show Dataset
if upload is not None:
    if st.checkbox('Preview Dataset'):
        if st.button('Head'):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail())

# Check the datatype of each column
if upload is not None:
    if st.checkbox('DataType of Each column'):
        st.write(data.dtypes)

# Find Shape of Our dataset
if upload is not None:
    if st.checkbox('Want to check the dimensions'):
        d = st.radio('What Dimension do you want to check?',('Rows','Columns'))
        
        if d=='Rows':
            st.write("The number of rows are: ",data.shape[0])
        if d=='Columns':
            st.write("The number of columns are: ",data.shape[1])

# Find Null Values in The Dataset
if upload is not None:
    test=data.isnull().values.any()
    if st.checkbox('Is there any null values?'):
        if test==False:
            st.write('No null values')
        if test==True:
            st.write("Yes there are null values")
            sns.heatmap(data.isnull())
            st.pyplot()

# Find Duplicate Values in the dataset
if upload is not None:
    test = data.duplicated().any()
    if st.checkbox('Check Duplicates'):
        if test==True:
            st.warning('Contains Duplicates')
            dup = st.radio('Want to remove duplicates?',('Select One','Yes','No'))
            
            if dup=='Yes':
                data=data.drop_duplicates()
                st.text('Duplicate Values are removed')
            if dup =='No':
                st.text('Ok No problem')
        if test==False:
            st.text('Congrats! no duplicate values')
            
# Get overall statistics
if upload is not None:
    if st.checkbox('Check the statistics'):
        st.write(data.describe())

if st.button('About App'):
    st.text('Built with Streamlit')
    st.text('Thanks to Streamlit')

if st.button('About the developer'):
    st.text('Saad Shaikh')