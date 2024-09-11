from .data_validation import validar_string
from .functions import buscar_en_lista

def ingresar_datos():
  partidos = []
  candidatos = []

  ## INGRESO DE PARTIDOS ##
  partido = input("Ingrese el primer partido (finaliza con el caracter x): ").upper()
  while partido != "X":
    if validar_string(partido):
      partidos.append(partido)
      candidatos.append([])
    else:
      print("¡Partido inválido! Intente nuevamente.")
    partido = input("Ingrese el siguiente partido: ").upper()

  ## INGRESO DE CANDIDATOS ##
  candidato = input("Ingrese el primer candidato (finaliza con el caracter x): ").upper()
  while candidato != "X":
    partido = ""
    if validar_string(candidato): # --> Si existe el candidato
      print(f"Partidos disponibles: {partidos}")
      partido = input("Ingrese el partido del candidato: ").upper() # --> Se ingresa el partido del candidato

      partidoIndex = buscar_en_lista(partidos, partido)
      while partidoIndex == -1: # --> Si el partido no existe
        print("¡Partido inválido! Intente nuevamente.")
        partido = input("----Ingrese el partido del candidato: ").upper()
        partidoIndex = buscar_en_lista(partidos, partido)

      if candidato not in candidatos[partidoIndex]: # --> Si el candidato no está en el partido se agrega al partido
          candidatos[partidoIndex].append(candidato)    
    else:
      print("¡Candidato inválido! Intente nuevamente.")
    candidato = input("Ingrese el siguiente candidato: ").upper()

  return candidatos, partidos