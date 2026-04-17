import boto3
import uuid
import json
from fastapi import FastAPI, UploadFile, Form

expediente = "750519"
nombre_completo = "Barraza Cárdenas Diego Alejandro"

app = FastAPI(title="Practica 4")

# Configurar clientes de AWS
s3_client = boto3.client('s3', region_name='us-east-1')
sqs_client = boto3.client('sqs', region_name='us-east-1')

BUCKET_NAME = f"practica-4-{expediente}"
QUEUE_NAME = "cola-boletines"


@app.post("/boletines")
async def crear_boletin(
    file: UploadFile,
    contenido: str = Form(...),
    correoElectronico: str = Form(...)
):
    """
    Endpoint para crear un nuevo boletín.
    """
    try:
        # Generar nombre único para el archivo
        file_id = str(uuid.uuid4())
        file_name = f"{file_id}-{file.filename}"
        
        # Leer contenido del archivo
        file_content = await file.read()
        
        # Subir archivo a S3
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=file_content,
            ContentType=file.content_type
        )
        
        # Generar URL de S3
        s3_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{file_name}"
        
        # Obtener URL de la cola SQS
        queue_response = sqs_client.get_queue_url(QueueName=QUEUE_NAME)
        queue_url = queue_response['QueueUrl']
        
        # Preparar mensaje para SQS
        mensaje = {
            "boletin_id": file_id,
            "contenido": contenido,
            "correoElectronico": correoElectronico,
            "imagen_url": s3_url,
            "nombre_archivo": file.filename
        }
        
        # Enviar mensaje a SQS
        sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(mensaje)
        )
        
        return {
            "mensaje": "Boletín creado exitosamente",
            "boletin_id": file_id,
            "imagen_url": s3_url
        }
    
    except Exception as e:
        return {
            "error": str(e),
            "mensaje": "Error al crear el boletín"
        }

preguntas = """
1. ¿Qué función cumple SQS dentro de esta arquitectura?
   - SQS actúa como un desacoplador entre el emisor y el receptor, permitiendo que el emisor envíe mensajes
     sin esperar a que el receptor los procese. Proporciona persistencia, garantizando que los mensajes
     no se pierdan aunque el receptor esté temporalmente inactivo.

2. ¿Por qué es útil desacoplar el emisor del receptor?
   - El desacoplamiento permite que cada servicio escale independientemente, mejora la resiliencia del sistema
     (si un servicio falla, el otro continúa), permite procesamiento asincrónico, y facilita el desarrollo
     y mantenimiento de cada componente de forma independiente.

3. ¿Qué ventajas ofrece SNS en este flujo?
   - SNS permite enviar notificaciones de manera asincrónica a múltiples suscriptores. En este caso, se usa
     para notificar al usuario por correo electrónico sobre nuevos boletines, sin que el receptor tenga que
     consultar constantemente la base de datos.

4. ¿Qué ventajas y desventajas ves al utilizar colas para gestionar la comunicación entre contenedores en contraste a protocolos sincrónicos como HTTP?
   - Ventajas: Desacoplamiento, escalabilidad, persistencia de mensajes, tolerancia a fallos.
   - Desventajas: Mayor latencia, consistencia eventual, mayor complejidad en implementación y debugging.
     HTTP es más simple e inmediato pero crea dependencias fuertes que limitarían la escalabilidad.

5. ¿Cuál consideras que sería una manera de incrementar la resiliencia de la aplicación en caso de que el envío de un mensaje falle?
   - Implementar reintentos automáticos para mensajes fallidos. Usar Dead-Letter Queue para guardar errores.
     Hacer que los receptores sean repetibles (procesar duplicados sin crear registros múltiples).

6. ¿Qué otro método crees que exista para el monitoreo de mensajes de manera sincrónica además de colas/notificaciones?
   - WebSockets/Server-Sent Events (SSE) para comunicación bidireccional en tiempo real.
     Webhooks donde servicios notifican activamente a otros. Polling de BD con cambios. Kafka como alternativa a SQS.
"""

conclusiones = """
Esta práctica permitió comprender la importancia de la arquitectura de microservicios y la comunicación asincrónica.

- La utilidad de AWS SQS para desacoplar servicios
- Cómo S3 facilita el almacenamiento de archivos en la nube
- La importancia de SNS para notificaciones en tiempo real
- Cómo Docker y contenedores permiten desplegar múltiples servicios de forma independiente
- La resiliencia que proporciona una arquitectura basada en colas de mensajes
"""

if __name__ == "__main__":
    print("Evaluación de la práctica 4")
    print(f"Nombre del alumno: {nombre_completo}")
    print(f"Expediente: {expediente}")
    print(preguntas)
    print(conclusiones)
