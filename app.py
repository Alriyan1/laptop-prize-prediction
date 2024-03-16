import streamlit as st
import numpy as np
import pandas as pd
import pickle

pipe=pd.read_pickle(open('pipe.pkl','rb'))
df=pd.read_pickle(open('df.pkl','rb'))

st.title('Laptop predictor')

company=st.selectbox('Brand',df['Company'].unique())

type=st.selectbox('Type',df['TypeName'].unique())

ram=st.selectbox('RAM in GB',[2,4,6,8,12,16,24,32,64])

weight=st.number_input('Weight of the Laptop')

touchscreen=st.selectbox('Touchscreen',['NO','YES'])

ips=st.selectbox('IPS',['NO','YES'])

screen_size=st.number_input('Screen Size')

resolution=st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160',
                                             '3200x1800','2880x1800','2560x1600','2560x1440',
                                             '2304x1440'])

cpu=st.selectbox('Brand',df['Cpu brand'].unique())

hdd=st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd=st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu=st.selectbox('GPU',df['Gpu brand'].unique())

os=st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    ppi=None
    if touchscreen=='YES':
        touchscreen=1
    else:
        touchscreen=0
    if ips=='YES':
        ips=1
    else:
        ips=0
    x_res=int(resolution.split('x')[0])
    y_res=int(resolution.split('x')[1])
    ppi=((x_res**2)+(y_res**2))**0.5/screen_size
    query=np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    query=query.reshape(1,12)
    st.title(int(np.exp(pipe.predict(query)[0])))