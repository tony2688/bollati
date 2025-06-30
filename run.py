#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bollati y Asociados S.R.L. - Script de inicio
Script alternativo para ejecutar la aplicación Flask
"""

import os
import sys
from app import app

if __name__ == '__main__':
    # Configuración para desarrollo
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print("🚀 Iniciando Bollati y Asociados Landing Page...")
    print(f"📍 Servidor disponible en: http://localhost:{port}")
    print(f"🔧 Modo debug: {debug}")
    print("\n" + "="*50)
    print("  BOLLATI Y ASOCIADOS S.R.L.")
    print("  'Código que Transforma Negocios'")
    print("="*50 + "\n")
    
    try:
        app.run(
            host='0.0.0.0',
            port=port,
            debug=debug,
            use_reloader=debug
        )
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido por el usuario")
    except Exception as e:
        print(f"❌ Error al iniciar el servidor: {e}")
        sys.exit(1)