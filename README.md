# 🚀 Bollati y Asociados S.R.L. - Landing Page Corporativa

**"Código que Transforma Negocios"**

Landing page moderna y responsive para empresa de desarrollo de software, construida con Flask, Tailwind CSS y JavaScript.

## 📋 Descripción

Esta landing page corporativa está diseñada para **Bollati y Asociados S.R.L.**, una empresa especializada en desarrollo de software. La página transmite innovación, confianza y profesionalismo para captar clientes que buscan soluciones digitales a medida.

### ✨ Características Principales

- 🎨 **Diseño Moderno**: Estética tech corporativa con paleta de colores profesional
- 📱 **Totalmente Responsive**: Optimizada para todos los dispositivos
- ⚡ **Alto Rendimiento**: Carga rápida y experiencia fluida
- 🔧 **Fácil Mantenimiento**: Código limpio y bien documentado
- 🌐 **APIs Preparadas**: Listo para integrar servicios externos
- 📧 **Formulario de Contacto**: Con validación y envío por email

## 🛠️ Stack Tecnológico

- **Backend**: Python con Flask
- **Frontend**: Tailwind CSS + JavaScript vanilla
- **Tipografías**: Roboto Condensed + Source Sans Variable
- **Iconos**: Font Awesome 6
- **Integración**: APIs REST preparadas

## 🧩 Estructura Modular

El proyecto utiliza una **arquitectura modular** que divide el contenido en secciones separadas para facilitar el mantenimiento y desarrollo:

### Ventajas de la Estructura Modular:
- ✅ **Mantenimiento Simplificado**: Cada sección puede editarse independientemente
- ✅ **Desarrollo en Equipo**: Múltiples desarrolladores pueden trabajar en diferentes secciones
- ✅ **Reutilización**: Las secciones pueden reutilizarse en otras páginas
- ✅ **Debugging Fácil**: Problemas aislados por sección
- ✅ **Escalabilidad**: Fácil agregar o remover secciones

### Cómo Editar Secciones:
1. Navega a `templates/sections/`
2. Edita el archivo HTML correspondiente a la sección deseada
3. Los cambios se reflejarán automáticamente en la página principal

## 🎨 Paleta de Colores

- **Primary Dark**: `#2F4858` - Color principal oscuro
- **Primary Red**: `#E2242A` - Color de acento rojo
- **Secondary Light**: `#F2F2F2` - Fondo claro
- **Secondary Medium**: `#CCCCCC` - Gris medio
- **Secondary Dark**: `#666666` - Gris oscuro
- **Secondary Darker**: `#333333` - Gris muy oscuro

## 📁 Estructura del Proyecto

```
Bollati/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── run.py                # Script alternativo para ejecutar la app
├── .env.example          # Variables de entorno de ejemplo
├── .gitignore           # Archivos a ignorar en Git
├── README.md            # Documentación del proyecto
├── static/
│   └── js/
│       └── main.js      # JavaScript principal
└── templates/
    ├── index.html       # Template principal HTML (modular)
    └── sections/        # Secciones modulares
        ├── header.html      # Navegación y header
        ├── hero.html        # Sección hero principal
        ├── services.html    # Sección de servicios
        ├── portfolio.html   # Sección de portfolio
        ├── technologies.html # Sección de tecnologías
        ├── process.html     # Sección del proceso
        ├── testimonials.html # Sección de testimonios
        ├── contact.html     # Sección de contacto
        └── footer.html      # Footer del sitio
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd Bollati
   ```

2. **Crear entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

## 📖 Secciones de la Landing Page

### 1. 🎯 Hero/Header
- Título principal: "Creamos Software que Impulsa tu Éxito"
- Subtítulo y slogan corporativo
- Botones CTA: "Iniciar Proyecto" y "Ver Portfolio"
- Ilustración SVG animada de código

### 2. 🛠️ Servicios
- **Desarrollo de Aplicaciones Web**: SPAs, PWAs, E-commerce
- **Software a Medida**: ERPs, CRMs, Automatización
- **Cloud Solutions**: AWS/Azure, DevOps, Serverless

### 3. 💼 Portfolio
- Filtros por categoría (Web Apps, Software, Cloud)
- Proyectos destacados con tecnologías utilizadas
- Carga dinámica desde API

### 4. 💻 Tecnologías
- Frontend: HTML5, CSS3, JavaScript, React, Vue.js
- Backend: Python, Flask, Django, Node.js
- Bases de Datos: PostgreSQL, MongoDB, MySQL
- Cloud & DevOps: AWS, Azure, Docker, Kubernetes

### 5. 🔄 Proceso de Trabajo
1. **Análisis**: Entendimiento de necesidades
2. **Diseño**: Prototipos y arquitectura
3. **Desarrollo**: Implementación con mejores prácticas
4. **Entrega**: Despliegue y soporte continuo

### 6. 💬 Testimonios
- Slider automático con testimonios de clientes
- Calificaciones con estrellas
- Carga dinámica desde API

### 7. 📞 Contacto
- Formulario con validación en tiempo real
- Información de contacto completa
- Integración preparada para APIs de email

## 🔧 APIs Disponibles

### Testimonios
```
GET /api/testimonials
```
Retorna lista de testimonios de clientes.

### Portfolio
```
GET /api/portfolio
```
Retorna proyectos del portfolio con filtros.

### Contacto
```
POST /api/contact
```
Procesa formulario de contacto.

**Payload esperado:**
```json
{
  "name": "Nombre del cliente",
  "email": "email@ejemplo.com",
  "company": "Empresa (opcional)",
  "message": "Mensaje del cliente"
}
```

## 🎛️ Personalización

### Colores
Modifica los colores en el archivo `templates/index.html` en la sección de configuración de Tailwind:

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                'gray-900': '#2F4858',
                'red-600': '#E2242A',
                // ... más colores
            }
        }
    }
}
```

### Contenido
- **Servicios**: Modifica las secciones en `templates/index.html`
- **Portfolio**: Actualiza los datos en `app.py` función `get_portfolio()`
- **Testimonios**: Actualiza los datos en `app.py` función `get_testimonials()`

### Integración de Email
Para habilitar el envío real de emails, configura las variables de entorno:

```bash
# Crear archivo .env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=tu-email@gmail.com
SMTP_PASSWORD=tu-password
```

## 🚀 Despliegue en Producción

### Usando Gunicorn
```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

### Variables de Entorno para Producción
```bash
FLASK_ENV=production
SECRET_KEY=tu-clave-secreta-segura
```

## 🧪 Testing

Ejecutar tests (si están configurados):
```bash
pytest
```

## 📝 Funcionalidades JavaScript

- **Menú móvil responsive** con animaciones
- **Smooth scroll** para navegación
- **Slider de testimonios** automático
- **Filtros de portfolio** dinámicos
- **Validación de formularios** en tiempo real
- **Animaciones de scroll** con Intersection Observer
- **Carga dinámica** de contenido desde APIs

## 🔒 Seguridad

- Validación de formularios en frontend y backend
- Sanitización de datos de entrada
- Headers de seguridad configurados
- Protección CSRF preparada

## 🤝 Contribución

Para contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## 📄 Licencia

Este proyecto está desarrollado para **Bollati y Asociados S.R.L.** - Todos los derechos reservados.

## 📞 Soporte

Para soporte técnico o consultas:
- **Email**: contacto@bollatiyasociados.com
- **Teléfono**: +54 11 1234-5678
- **Ubicación**: Buenos Aires, Argentina

---

**Desarrollado con ❤️ para Bollati y Asociados S.R.L.**

*"Código que Transforma Negocios"*