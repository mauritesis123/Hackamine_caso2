
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#import squarify
import pandas as pd
#import plotly.express as px # Graficar treemap
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px

 





st.title('Dashboard, visualizacion datos')


Menu_items=['Indicadores','Fallas'] #,'Temporalidad fallas'
Menu_choices=st.sidebar.selectbox('Seleccionar opción',Menu_items)


BASE_PATH = Path().resolve().parent
print(BASE_PATH)
PATH_DATA = BASE_PATH.joinpath("Hackamine_caso2\sistema_gestion_monitoreo\Archivos Complementarios")

#C:\Users\ramir\OneDrive\Desktop\Hackamine_caso1\Data\Desafio DF

df = pd.read_excel(PATH_DATA.joinpath("Estadisticas_Indicadores a nivel de Red LTE.xlsx"))
df.drop([ 'Unnamed: 1'], axis=1, inplace=True)
df = df.loc[1:,:]
df = pd.DataFrame(np.row_stack([df.columns, df.values]),columns=df.iloc[0].values.tolist())
df = df.drop(labels=[0,1], axis=0)
df = df.rename(columns={np.nan: 'fecha'})
PATH_DATA_2 = BASE_PATH.joinpath("Hackamine_caso2\Finales")
#frequencyband = pd.read_excel(PATH_DATA_2.joinpath("hm-device.frequencyband.xlsx"))
latency = pd.read_excel(PATH_DATA_2.joinpath("device.latency.xlsx")) 

if Menu_choices=='Indicadores':
    st.subheader("Indicadores")
    #st.text("Esto es texto")
     
    # volumne
    fig1 = px.line(df, x="fecha", y='LTE_5212A',title='Volumen de datos')#,name='Downlink')#name='Downlink'
    fig1.add_scatter(x=df['fecha'], y=df['LTE_5213A'],name='Uplink')
    st.plotly_chart(fig1)
    
    
    
    
    #Throughput
    fig2 = px.line(df, x="fecha", y='LTE_5289D',title='Throughput')#,name='Downlink')#name='Downlink'
    fig2.add_scatter(x=df['fecha'], y=df['LTE_5292D'],name='Promedio Throughput Downlink')
    fig2.add_scatter(x=df['fecha'], y=df['LTE_291B'],name='Maximo Throughput Uplink')
    fig2.add_scatter(x=df['fecha'], y=df['LTE_288B'],name='Maximo Throughput Downlink')
    st.plotly_chart(fig2)
    
    
    
     #Promedio usuarios
    fig3 = px.line(df, x="fecha", y='LTE_5800E',title='Promedio usuarios')#,name='Downlink')#name='Downlink'
    fig3.add_scatter(x=df['fecha'], y=df['LTE_5801E'],name='Promedio usuarios con data en el buffer enlace uplink')
    fig3.add_scatter(x=df['fecha'], y=df['LTE_5802B'],name='Maximo usuarios en le buffer por celda DL')
    fig3.add_scatter(x=df['fecha'], y=df['LTE_5803B'],name='Maximo usuarios en le buffer por celda UL')
    st.plotly_chart(fig3)
    
    
    
    #frequencyband=frequencyband.loc[:100,:]
    latency=latency.loc[:100,:]
    #frequencyband=frequencyband.loc[:100,:]
    latency=latency.loc[:100,:]
    #latency['min']
    fig4 = px.line(latency, x="fecha", y='min',title='Latencia') 
    fig4.add_scatter(x=latency['fecha'], y=latency['max'],name='max')
    st.plotly_chart(fig4)






# RSRP nivel del señal de requerimientos
df_rsrp = pd.read_excel(PATH_DATA_2.joinpath("hm-device.rsrp.xlsx"))



# Las observaciones son tomadas en orden para cada tipo de dispositivo, que se listan aquí
#df_rsrp["device_name"].unique();
#err_occ = [];
#len_device = [];
#for dispositivo in df_rsrp["device_name"].unique():
 #   err_occ.append(np.sum(df_rsrp[df_rsrp["device_name"] == dispositivo]["valor"] < -111))
  #  len_device.append(len(df_rsrp[df_rsrp["device_name"]==dispositivo]))
    
#porc_err_occ = 100*np.divide(err_occ, len_device)
    

#device='ESCCTK293'


if Menu_choices=='Fallas':
    
    device = st.text_input("Seleccionar device a estudiar", 'ESCCTK293')
    df_rsrp_device=df_rsrp.query("`device_name` == '{}'".format(device) ).sort_values(by="fecha")
    cantidad_incidentes=np.sum(df_rsrp_device["valor"] < -111)# desviacion de requerimiento la señal es menor al umbral minimo

    
    
    
    fig21 = px.line(df_rsrp_device, x="fecha", y='valor',title='Nivel de señal de {}'.format(device)) 
    fig21.add_scatter(x=df_rsrp_device['fecha'], y=len(df_rsrp_device)*[-111],name='nivel minimo')
    st.plotly_chart(fig21)
    
    st.write('El porcentaje de falla de {} es {} %'.format(device, 100* cantidad_incidentes/len(df_rsrp_device)   ))
     
         
    
    
    
    
    
    
    