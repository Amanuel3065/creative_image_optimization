

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
    all_objects_count = st.number_input('all objects', key='a')
    no_of_unique_objects = st.number_input('unique objects', key='b')
    
    st.header("engagement button size in pixels")
    eng_width = st.number_input('width of engagement button', key='c')
    eng_height = st.number_input('height of engagement button', key='d')

    st.header("LAR")
    LAR = st.number_input('logo proportion', key='e')

    st.header("CTA properties")
    cta_text_word_count = st.number_input('word count', key='f')
    cta_width = st.number_input('width', key='g')
    cta_height = st.number_input('height', key='h')
    red, green, blue = st.columns([1,1,1])
    red = st.number_input('red', key='i')
    green = st.number_input('green', key='j')
    blue = st.number_input('blue', key='k')

    #total_retransmission = st.number_input('Enter tcp retransmission', key='d')
    #average_delay = st.number_input('Enter average delay', key='e')
    #total_throughput = st.number_input('Enter average throughput', key='f')
    

    if st.button('KPI prediction'):
        array = [no_of_unique_objects, eng_width, eng_height]
        val = pickled_model.predict([array])
        KPI = [i[0] for i in val][0]
        st.write(
            "The estimated KPI is: {:.3f}".format(KPI))