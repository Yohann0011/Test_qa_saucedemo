Este proyecto contiene pruebas automatizadas y manuales para la aplicación de demostración SauceDemo, una tienda de e-commerce ficticia usada comúnmente para practicar pruebas de software.

El objetivo es validar que los flujos principales (login, carrito, checkout) funcionen correctamente, además de probar casos de borde, seguridad y problemas conocidos, como los del usuario problem_user.

#Tecnologías usadas#
Python 3.13
Selenium 4.39
Pytest (con plugin HTML para reportes)
Microsoft Edge (navegador)
Page Object Model (POM) para mantener el código limpio y reutilizable

#Qué incluye este repositorio#
• 28 casos de prueba (18 automatizados + 10 manuales)
• Validación de seguridad: XSS, caracteres inválidos (como Alt+255), longitud extrema
• Pruebas con usuarios especiales: problem_user, performance_glitch_user, locked_out_user
• Reporte de bugs reales: por ejemplo, que la app permite caracteres no imprimibles en el checkout
• Estructura organizada: código separado por responsabilidades

#Cómo ejecutar las pruebas#
Prerrequisitos
• Tener Microsoft Edge instalado (viene por defecto en Windows 11)
• El archivo msedgedriver.exe ya está incluido en la carpeta /drivers
Pasos
1. Clonar o descomprimir este repositorio
2. Abrir PowerShell o CMD en la carpeta del proyecto
3. Crear y activar el entorno virtual:

en powershell:

python -m venv venv
venv\Scripts\Activate.ps1

4. Instalar dependencias

pip install -r requirements.txt

5. Ejecutar las pruebas automatizadas:
 
pytest tests/ -v --html=report.html

6. Ver el reporte: abre report.html en tu navegador
Las pruebas manuales se documentan en el plan de pruebas y deben ejecutarse visualmente.

#Estructura del proyecto#

Test_saucedemo.com/
├── drivers/                # EdgeDriver incluido (no necesitas descargar nada)
├── pages/                  
├── data/                   
├── utils/                  
├── tests/                  
├── plan_pruebas.md         
├── requirements.txt        
└── README.md               

