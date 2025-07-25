# -*- coding: utf-8 -*-
"""
Bollati y Asociados S.R.L. - Landing Page Corporativa
Aplicación Flask principal para la landing page de la empresa de desarrollo de software

Autor: Desarrollado para Bollati y Asociados S.R.L.
Descripción: Landing page moderna y responsive con Flask + Tailwind CSS
"""

from flask import Flask, render_template, request, jsonify
import json
import os

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bollati-dev-secret-key-2024'

# Configuración para producción
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

@app.route('/')
def index():
    """
    Ruta principal - Renderiza la landing page completa
    Incluye todas las secciones: Hero, Servicios, Portfolio, etc.
    """
    return render_template('index.html')

@app.route('/about')
def about():
    """
    Página sobre nosotros - Información adicional de la empresa
    """
    return {
        'empresa': 'Bollati y Asociados S.R.L.',
        'descripcion': 'Empresa líder en desarrollo de software y soluciones tecnológicas',
        'servicios': [
            'Desarrollo Web',
            'Aplicaciones Móviles', 
            'Cloud Solutions',
            'Consultoría IT'
        ],
        'ubicacion': 'Argentina',
        'fundada': '2020',
        'mensaje': 'Transformamos ideas en soluciones digitales innovadoras'
    }

# Rutas de debug removidas para producción
# Las rutas /test, /debug y /simple han sido eliminadas para optimizar la aplicación

@app.route('/api/contact', methods=['POST'])
def contact_form():
    """
    API endpoint para procesar el formulario de contacto
    Preparado para integrar con servicios de email externos
    """
    try:
        data = request.get_json()
        
        # Validación básica de datos
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'success': False, 
                    'message': f'El campo {field} es requerido'
                }), 400
        
        # Aquí se puede integrar con APIs de email como SendGrid, Mailgun, etc.
        # Por ahora simulamos el envío exitoso
        print(f"Nuevo contacto: {data['name']} - {data['email']}")
        print(f"Mensaje: {data['message']}")
        
        return jsonify({
            'success': True,
            'message': 'Mensaje enviado correctamente. Te contactaremos pronto.'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Error interno del servidor'
        }), 500

@app.route('/api/testimonials')
def get_testimonials():
    """
    API endpoint para obtener testimonios
    Preparado para integrar con bases de datos o APIs externas
    """
    # Datos de ejemplo - pueden venir de una base de datos o API externa
    testimonials = [
        {
            'id': 1,
            'name': 'María González',
            'company': 'TechStart Solutions',
            'position': 'CEO',
            'message': 'Bollati y Asociados transformó completamente nuestro negocio con una plataforma web increíble.',
            'rating': 5
        },
        {
            'id': 2,
            'name': 'Carlos Mendoza',
            'company': 'Innovate Corp',
            'position': 'CTO',
            'message': 'Excelente calidad de código y cumplimiento de tiempos. Altamente recomendados.',
            'rating': 5
        },
        {
            'id': 3,
            'name': 'Ana Rodríguez',
            'company': 'Digital Ventures',
            'position': 'Directora de Tecnología',
            'message': 'Su expertise en cloud solutions nos ayudó a escalar nuestro negocio de manera eficiente.',
            'rating': 5
        }
    ]
    
    return jsonify(testimonials)

@app.route('/api/portfolio')
def get_portfolio():
    """
    API endpoint para obtener proyectos del portfolio
    Preparado para integrar con CMS o bases de datos
    """
    portfolio_items = [
        {
            'id': 1,
            'title': 'E-commerce Avanzado',
            'description': 'Plataforma de comercio electrónico con integración de pagos y gestión de inventario.',
            'technologies': ['Python', 'Django', 'PostgreSQL', 'AWS'],
            'category': 'web-app',
            'image': '/static/images/portfolio/ecommerce.jpg'
        },
        {
            'id': 2,
            'title': 'Sistema de Gestión Empresarial',
            'description': 'ERP personalizado para optimizar procesos internos y reporting.',
            'technologies': ['Flask', 'React', 'MongoDB', 'Docker'],
            'category': 'software',
            'image': '/static/images/portfolio/erp.jpg'
        },
        {
            'id': 3,
            'title': 'Migración a Cloud',
            'description': 'Migración completa de infraestructura legacy a AWS con alta disponibilidad.',
            'technologies': ['AWS', 'Kubernetes', 'Terraform', 'CI/CD'],
            'category': 'cloud',
            'image': '/static/images/portfolio/cloud.jpg'
        }
    ]
    
    return jsonify(portfolio_items)

if __name__ == '__main__':
    # Configuración para desarrollo local
    # En producción, Gunicorn manejará la aplicación
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)