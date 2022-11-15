

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

    st.header("")
    no_of_unique_objects = st.number_input('unique objects', key='a')
    eng_width = st.number_input('width of engagement button', key='b')
    eng_height = st.number_input('height of engagement button', key='c')
    #total_retransmission = st.number_input('Enter tcp retransmission', key='d')
    #average_delay = st.number_input('Enter average delay', key='e')
    #total_throughput = st.number_input('Enter average throughput', key='f')
    

    if st.button('KPI prediction'):
        array = [no_of_unique_objects, eng_width, eng_height]
        val = pickled_model.predict([array])
        KPI = [i[0] for i in val][0]
        st.write(
            "The estimated KPI is: {:.3f}".format(KPI))