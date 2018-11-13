#CREANDO DATA FRAMES CON "python" Y "pandas".

#IMPORTAMOS LIBRERIA.
import pandas as pd
 
#CREAMOS DATA FRAME.
df_demografia = pd.DataFrame({
    'CAPITALES':['MADRID','LONDRES','PARIS'],
    'Población':[3207247,8787892,2206488],
    'Densidad':[5266,5590,21258]
 
})

#AÑADIMOS NUEVO DATA FRAME
df_natur = pd.DataFrame({
    'CAPITALES':['MADRID','LONDRES','PARIS'],
    'Extensión':[604.45,105.4,1572],
    'Clima':['Transi','Oceánico','Oceánico']

})


#CREAMOS ARCHIVO EXCEL. 
with pd.ExcelWriter('capitales_datos.xls') as writer:
    df_demografia.to_excel(writer,sheet_name="demografia")
    #AÑADIMOS LA NUEVA HOJA AL EXCEL.
    df_natur.to_excel(writer,"fisica")
    

