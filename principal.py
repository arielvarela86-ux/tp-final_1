from sensores import limpiar_registro_sensor, generar_resumen_sensores

if __name__ == "__main__":
    
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": " 38.2 °C ", "ubicacion": ""},
        {"sensor_id": " SENSOR-003 ", "temperatura": "19.0C", "ubicacion": "Planta Sur"},
        {"sensor_id": "SENSOR-004", "temperatura": "41.8 C", "ubicacion": "Calderas Principales"}
    ]

    print("=== PROCESAMIENTO Y LIMPIEZA DE DATOS CRUDOS ===")
    
    
    registros_limpios = [limpiar_registro_sensor(reg) for reg in registros_crudos]
    
    
    UMBRAL_ALERTA = 35.0
    
    
    sensores_alerta, promedio_global = generar_resumen_sensores(registros_limpios, UMBRAL_ALERTA)
    
    
    print("\n" + "="*50)
    print("         REPORTE CONSOLIDADO ECOTECH SOLUTIONS")
    print("="*50)
    print(f"  Temperatura Global Promedio : {promedio_global:.2f} °C")
    print(f"  Umbral de Alerta Configurado : {UMBRAL_ALERTA} °C")
    print(f" Dispositivos en Alerta        : {len(sensores_alerta)} ({', '.join(sensores_alerta)})")
    
    print("\n--- DETALLE DE REGISTROS SANITIZADOS ---")
    for reg in registros_limpios:
        alerta_txt = " [¡ALERTA!]" if reg["temperatura"] > UMBRAL_ALERTA else " [Normal]"
        print(f" • ID: {reg['sensor_id']:<12} | Temp: {reg['temperatura']:>5.1f} °C | Ubicación: {reg['ubicacion']}{alerta_txt}")
    print("="*50)
    