

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

    st.header("number of objects")
    form = st.form(key="w")
    allc, uqec = st.columns(3)
    with allc:
        all_objects_count = st.number_input('all objects', key='a')
    with uqec:
        no_of_unique_objects = st.number_input('unique objects', key='b')
   
    
    



    st.header("engagement button properties")

    form = st.form(key="x")
    engWc, engHc = st.columns(3)
    with engWc:
        eng_width = st.number_input('width of engagement button', key='c')
    with engHc:
        eng_height = st.number_input('height of engagement button', key='d')
        
    
    

    st.header("LAR")
    LAR = st.number_input('logo proportion', key='e')


   
    st.header("CTA properties")
    cta_text_word_count = st.number_input('word count', key='f')
   
    form = st.form(key="y")
    ctaWc, ctaHc = st.columns(3)
    with ctaWc:
        cta_width = st.number_input('width', key='g')
    with ctaHc:
        cta_height = st.number_input('height', key='h')
        

    form = st.form(key="z")
    redc, greenc, bluec = st.columns(3)
    with redc:
        red = form.number_input('red', key='i')
    with greenc:
        green = form.number_input('green', key='j')
    with bluec:
        blue = form.number_input('blue', key='k')

    

    #total_retransmission = st.number_input('Enter tcp retransmission', key='d')
    #average_delay = st.number_input('Enter average delay', key='e')
    #total_throughput = st.number_input('Enter average throughput', key='f')
    

    if st.button('KPI prediction'):
        array = [no_of_unique_objects, eng_width, eng_height]
        val = pickled_model.predict([array])
        KPI = [i[0] for i in val][0]
        st.write(
            "The estimated KPI is: {:.3f}".format(KPI))