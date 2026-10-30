
def limpiar_registro_sensor(registro_raw):
    sensor_id = str(registro_raw.get("sensor_id", "")).strip()
    
    temp_raw = str(registro_raw.get("temperatura", "0"))
    for caracter in ["°C", "°c", "C", "c", "°", " "]:
        temp_raw = temp_raw.replace(caracter, "")
        
    try:
        temperatura = float(temp_raw)
    except ValueError:
        temperatura = 0.0
        
    ubicacion = registro_raw.get("ubicacion")
    if not ubicacion or not str(ubicacion).strip():
        ubicacion = "Planta General (No especificada)"
    else:
        ubicacion = str(ubicacion).strip()
        
    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    lista_sensores_alerta = []
    suma_temperaturas = 0.0
    total_sensores = len(lista_sensores_limpios)
    
    if total_sensores == 0:
        return [], 0.0

    for sensor in lista_sensores_limpios:
        temp = sensor.get("temperatura", 0.0)
        suma_temperaturas += temp
        
        if temp > umbral_temperatura:
            lista_sensores_alerta.append(sensor.get("sensor_id"))
            
    promedio_temperatura = suma_temperaturas / total_sensores
    return lista_sensores_alerta, promedio_temperatura