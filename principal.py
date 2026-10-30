
from sensores import limpiar_registro_sensor, generar_resumen_sensores

if __name__ == "__main__":
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": " 38.2 °C ", "ubicacion": ""},
        {"sensor_id": " SENSOR-003 ", "temperatura": "19.0C", "ubicacion": "Planta Sur"},
        {"sensor_id": "SENSOR-004", "temperatura": "41.8 C", "ubicacion": "Calderas Principales"}
    ]

    print("=== PROCESAMIENTO MODULAR ===")
    
    
from sensores import limpiar_registro_sensor, generar_resumen_sensores

if __name__ == "__main__":
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": " 38.2 °C ", "ubicacion": ""},
        {"sensor_id": " SENSOR-003 ", "temperatura": "19.0C", "ubicacion": "Planta Sur"},
        {"sensor_id": "SENSOR-004", "temperatura": "41.8 C", "ubicacion": "Calderas Principales"}
    ]

    print("=== PROCESAMIENTO MODULAR ===")
    
    
    registros_limpios = [limpiar_registro_sensor(reg) for reg in registros_crudos]
    
    UMBRAL_ALERTA = 35.0
    sensores_alerta, promedio_global = generar_resumen_sensores(registros_limpios, UMBRAL_ALERTA)
    
    print(f"Temperatura Global Promedio: {promedio_global:.2f} °C")
    print(f"Dispositivos en Alerta: {sensores_alerta}")
    registros_limpios = [limpiar_registro_sensor(reg) for reg in registros_crudos]
    
    UMBRAL_ALERTA = 35.0
    sensores_alerta, promedio_global = generar_resumen_sensores(registros_limpios, UMBRAL_ALERTA)
    
    print(f"Temperatura Global Promedio: {promedio_global:.2f} °C")
    print(f"Dispositivos en Alerta: {sensores_alerta}")