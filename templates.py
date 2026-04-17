"""
Templates HTML para la aplicación de boletines
Contiene los strings HTML listos para usar
"""

# Template HTML para mostrar un boletín
BOLETIN_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Boletín {id}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
        
        .container {{
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
            max-width: 800px;
            width: 100%;
            padding: 40px;
        }}
        
        h1 {{
            color: #333;
            margin-bottom: 10px;
            text-align: center;
        }}
        
        .info {{
            background: #f5f5f5;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            font-size: 14px;
            color: #666;
        }}
        
        .contenido {{
            background: #f9f9f9;
            padding: 20px;
            border-left: 4px solid #667eea;
            margin: 20px 0;
            border-radius: 4px;
            line-height: 1.6;
            color: #333;
        }}
        
        .imagen {{
            text-align: center;
            margin: 30px 0;
        }}
        
        .imagen img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }}
        
        .link-seccion {{
            margin: 20px 0;
            padding: 15px;
            background: #e8f4f8;
            border-radius: 5px;
        }}
        
        .link-seccion a {{
            color: #667eea;
            text-decoration: none;
            word-break: break-all;
            font-weight: 500;
        }}
        
        .link-seccion a:hover {{
            text-decoration: underline;
        }}
        
        .estado-leido {{
            text-align: center;
            color: #27ae60;
            font-weight: bold;
            margin-top: 20px;
            padding: 10px;
            background: #d5f4e6;
            border-radius: 5px;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            font-size: 12px;
            color: #999;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📬 Boletín</h1>
        
        <div class="info">
            <strong>ID del boletín:</strong> {id}<br>
            <strong>Correo:</strong> {correo_electronico}<br>
            <strong>Fecha de creación:</strong> {fecha_creacion}
        </div>
        
        <div class="contenido">
            <h2>Contenido del boletín</h2>
            <p>{contenido}</p>
        </div>
        
        <div class="imagen">
            <h3>Archivo adjunto</h3>
            <img src="{imagen_url}" alt="{nombre_archivo}" />
        </div>
        
        <div class="link-seccion">
            <strong>📎 Enlace del archivo en S3:</strong><br>
            <a href="{imagen_url}" target="_blank">{imagen_url}</a>
        </div>
        
        <div class="estado-leido">
            ✓ Boletín marcado como leído
        </div>
        
        <div class="footer">
            <p>Sistema de Boletines - Práctica 4</p>
        </div>
    </div>
</body>
</html>
"""
