import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def descrive_obj(df):
  """
  Por cada variable existente en el objeto, calcula las medidas descriptivas para los casos continuos.
  Para cada variable discreta, que calcule la frecuencia.
  """

  for column in df.columns:
    if df[column].dtype == 'float64':
      print('')
      print(column.upper(),': Variable Continua')
      print(df[column].describe())
      

    elif (df[column].dtype == 'object') or (df[column].dtype == 'int64'):
      print('')
      print(column.upper(),': Variable Discreta')
      print(df[column].value_counts())

    else:
      print('Error en tipo de dato')

def list_nan(df , var, print_list = False):
  """
  La función contiene los siguientes argumentos:
    dataframe: La función debe ingresar un objeto DataFrame.
    var: Variable a inspeccionar.
    print_list: Opción para imprimir la lista de observaciones perdidas en la variable. Debe ser False por defecto.
  La función retorna la cantidad de casos perdidos y el porcentaje correspondiente. Cuando print_list = True, retorna la lista de casos.
  """

  filter = df[var].isna()

  if print_list:
    return df[filter]
  else:
    return filter.sum() , filter.sum()/len(df[var])

def histogram (sample_df, full_df, var, true_mean, sample_mean = False):
  """
  La función grafica un histograma de una variable entregada para un DataFrame de muestra. El gráfico debe además señalar las medias de la variable entregada, tanto para el DataFrame de muestra entregado, como para el DataFrame completo correspondiente.
  La función incluye los siguientes argumentos:
    sample_df: La base de datos donde se encuentran los datos específicos (muestra).
    full_df: La base de datos donde se encuentran todos los datos (contiene los datos de la muestra).
    var: La variable a graficar.
    sample_mean: Booleano. Si es verdadero, genera una recta vertical indicando la media de la variable en la selección muestral (sample_df). Por defecto es False.
    true_mean: Booleano. Si es verdadero, genera una recta vertical indicando la media de variable en la base de datos completa (full_df).
  """


  # vamos a eliminar los datos perdidos en la columna con dropna()
  var_dropna = sample_df[var].dropna()
  
  plt.hist(var_dropna, color='blue', alpha=.4, bins=30)
  if sample_mean:
    plt.axvline(var_dropna.mean(), color = 'dodgerblue', linestyle ='--')
    
  if true_mean:
    plt.axvline(full_df[var].dropna().mean(), color = 'tomato', linestyle ='--');
    
  plt.title('Distribución empírica de la variable {} {}'.format(('continua' if sample_df[var].dtype == 'float64' else 'discreta'),var.upper()));
    


def dotplot(df, plot_var, plot_by, statistic = 'mean', global_stat = False):
  """
  función que devuelve un dotplot con las medias por región para una variable entregada
  Cada “punto” del dotplot representa la media, o mediana, de una variable para una región específica.
  La función contiene los siguientes parámetros:
    dataframe: La tabla de datos donde buscar las variables.
    plot_var: Corresponde a una columna del dataframe entregado, de la cual se desea obtener la métrica (puede ser 'mean' o 'median').
    plot_by: Corresponde a otra columna del dataframe entregado. Es la columna por la cual se quiere agrupar el dataframe, para acceder luego a la columna entregada en plot_var.
    statistic: presenta dos opciones; "mean" para la media y "median" para la mediana. Por defecto debe ser "mean".
    global_stat: Booleano. Si es True,  grafica la media (o mediana, según lo indicado en statistic) de la variable plot_var entregada, sin agrupar (para todos los datos entregados en dataframe). Por defecto es False.
  """
  if statistic == 'mean':
    group = round( df.groupby(plot_by)[plot_var].mean() , 2)
    vline = df[plot_var].mean()
  else:
    group = round( df.groupby(plot_by)[plot_var].median() , 2)
    vline = df[plot_var].median()

  plt.rcParams["figure.figsize"] = (5, 5) # Tamaño gráficos
  plt.title(statistic+' '+plot_var+' by '+plot_by)
  plt.plot(group.values , group.index, 'o', color = 'blue')

  if global_stat:
    plt.axvline(vline, color = 'tomato' , linestyle = '--')