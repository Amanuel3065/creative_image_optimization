

from numpy.core.records import array
import streamlit as st
from pickle import load
import pickle
import numpy as np
import sys




def app():

    # Load Saved Results Data
    pickled_model = pickle.load(open('models/07-11-2022-07-33-52-3.07%.pkl', 'rb'))
    #model = load(filename='models/07-11-2022-07-33-52-3.07%.pkl')

    st.title("KPI Model")

    st.header("To calculate KPI, enter values below.")


    st.header("About the creative")

    st.subheader('Word count')
    all_text_word_count = st.number_input('Word count', key='a')

    st.subheader('number of objects')
    form = st.form(key="u")
    allc, uqec = st.columns(2)
    with allc:
        all_objects_count = st.number_input('all objects', key='b')
    with uqec:
        unique_objects_count = st.number_input('unique objects', key='c')

   
   
    st.subheader('preview height')
    form1 = st.form(key="v")
    prevWc, prevHc = st.columns(2)
    with prevWc:
        preview_width = st.number_input('preview width', key='d')
    with prevHc:
        preview_height = st.number_input('preview height', key='e')
   
    
    st.header("engagement button properties")
    st.subheader('size')
    form2 = st.form(key="w")
    engWc, engHc = st.columns(2)
    with engWc:
        eng_width = st.number_input('width of engagement button', key='f')
    with engHc:
        eng_height = st.number_input('height of engagement button', key='g')
        
    
    
    st.header("Logo properties")
    
    LAR = st.number_input('logo proportion to preview area', key='h')
    st.subheader('size')
    form3 = st.form(key="x")
    loWc, loHc = st.columns(2)
    with loWc:
        logo_width = st.number_input('width of logo', key='i')
    with loHc:
        logo_height = st.number_input('height of logo', key='j')

   
    st.header("CTA properties")

    cta_text_word_count = st.number_input('word count', key='k')
    
    st.subheader('size')
    form4 = st.form(key="y")
    ctaWc, ctaHc = st.columns(2)
    with ctaWc:
        cta_width = st.number_input('width', key='l')
    with ctaHc:
        cta_height = st.number_input('height', key='m')
        
    st.subheader('cta color composition')
    form5 = st.form(key="z")
    redc, greenc, bluec = st.columns(3)
    with redc:
        red = st.number_input('red', key='n')
    with greenc:
        green = st.number_input('green', key='o')
    with bluec:
        blue = st.number_input('blue', key='p')

    

    #total_retransmission = st.number_input('Enter tcp retransmission', key='d')
    #average_delay = st.number_input('Enter average delay', key='e')
    #total_throughput = st.number_input('Enter average throughput', key='f')
    

    if st.button('KPI prediction'):
        array = [all_text_word_count, LAR, all_objects_count, unique_objects_count, 
                cta_text_word_count, cta_width, cta_height, red, green, blue, logo_width, 
                logo_height, eng_width, eng_height, preview_width, preview_height]
        val = pickled_model.predict([array])
        KPI = [i[0] for i in val][0]
        st.write(
            "The estimated KPI is: {:.3f}".format(KPI))