@echo off
REM build_windows.bat — Script completo para generar el instalador de Windows
REM
REM Requisitos previos:
REM   - Python 3.10+ instalado y en PATH
REM   - pip install -r requirements.txt ejecutado
REM   - Inno Setup 6 instalado en la ruta por defecto
REM
REM Que hace este script:
REM   1. Verifica dependencias (Python, PyInstaller, Inno Setup)
REM   2. Instala PyInstaller si no esta disponible
REM   3. Construye el bundle con PyInstaller usando bootcamp.spec
REM   4. Compila el instalador con Inno Setup
REM   5. Informa la ubicacion del .exe generado
REM
REM Uso:
REM   build_windows.bat
REM   build_windows.bat --skip-pyinstaller    (si el bundle ya existe)
REM   build_windows.bat --skip-inno           (si solo quieres el bundle)

setlocal enabledelayedexpansion

REM ---------------------------------------------------------------------------
REM CONFIGURACION
REM ---------------------------------------------------------------------------

set PYTHON=python
set PIP=pip
set APP_NAME=BootcampPythonDS
set VERSION=1.0.0
set SPEC_FILE=bootcamp.spec
set INNO_SETUP="C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
set INNO_SCRIPT=installer\setup.iss
set OUTPUT_DIR=dist_installer

REM Flags de control (modificados por argumentos de linea de comandos)
set SKIP_PYINSTALLER=0
set SKIP_INNO=0

REM ---------------------------------------------------------------------------
REM PARSEAR ARGUMENTOS
REM ---------------------------------------------------------------------------

for %%A in (%*) do (
    if "%%A"=="--skip-pyinstaller" set SKIP_PYINSTALLER=1
    if "%%A"=="--skip-inno"        set SKIP_INNO=1
)

REM ---------------------------------------------------------------------------
REM BANNER
REM ---------------------------------------------------------------------------

echo.
echo ============================================================
echo   BOOTCAMP PYTHON DS - GENERADOR DE INSTALADOR WINDOWS
echo   Version: %VERSION%
echo ============================================================
echo.

REM ---------------------------------------------------------------------------
REM PASO 1: VERIFICAR PYTHON
REM ---------------------------------------------------------------------------

echo [1/5] Verificando Python...
%PYTHON% --version >nul 2>&1
if errorlevel 1 (
    echo   ERROR: Python no encontrado en PATH.
    echo   Descarga Python 3.10+ desde https://python.org/downloads/
    echo   Asegurate de marcar "Add Python to PATH" durante la instalacion.
    exit /b 1
)

for /f "tokens=*" %%v in ('%PYTHON% --version') do set PYTHON_VER=%%v
echo   OK: !PYTHON_VER!

REM ---------------------------------------------------------------------------
REM PASO 2: VERIFICAR / INSTALAR PYINSTALLER
REM ---------------------------------------------------------------------------

echo.
echo [2/5] Verificando PyInstaller...
%PYTHON% -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo   PyInstaller no encontrado. Instalando...
    %PIP% install pyinstaller
    if errorlevel 1 (
        echo   ERROR: No se pudo instalar PyInstaller.
        exit /b 1
    )
)

for /f "tokens=*" %%v in ('%PYTHON% -m PyInstaller --version') do set PYIN_VER=%%v
echo   OK: PyInstaller !PYIN_VER!

REM Verificar tambien que las dependencias de la app estan instaladas
echo.
echo [3/5] Verificando dependencias de la app...
%PYTHON% -c "import flask, pandas, sklearn, matplotlib, nbformat" >nul 2>&1
if errorlevel 1 (
    echo   Algunas dependencias faltan. Instalando requirements.txt...
    %PIP% install -r requirements.txt
    if errorlevel 1 (
        echo   ERROR: No se pudieron instalar las dependencias.
        exit /b 1
    )
)
echo   OK: flask, pandas, scikit-learn, matplotlib, nbformat

REM ---------------------------------------------------------------------------
REM PASO 3: PYINSTALLER — GENERAR EL BUNDLE
REM ---------------------------------------------------------------------------

echo.
if "%SKIP_PYINSTALLER%"=="1" (
    echo [4/5] PyInstaller: OMITIDO (--skip-pyinstaller)
    if not exist "dist\%APP_NAME%\%APP_NAME%.exe" (
        echo   ADVERTENCIA: dist\%APP_NAME%\%APP_NAME%.exe no existe.
        echo   Ejecuta sin --skip-pyinstaller para generarlo.
        exit /b 1
    )
) else (
    echo [4/5] Construyendo bundle con PyInstaller...
    echo   Spec: %SPEC_FILE%
    echo   Esto puede tardar varios minutos la primera vez...
    echo.

    REM Limpiar build anterior para evitar artefactos
    if exist "build\%APP_NAME%" (
        echo   Limpiando build anterior...
        rmdir /s /q "build\%APP_NAME%"
    )

    REM Ejecutar PyInstaller
    %PYTHON% -m PyInstaller %SPEC_FILE% --noconfirm --log-level WARN
    if errorlevel 1 (
        echo.
        echo   ERROR: PyInstaller fallo. Revisa los mensajes anteriores.
        echo   Consejo: ejecuta con --log-level DEBUG para mas detalle.
        exit /b 1
    )

    echo.
    echo   Bundle generado en: dist\%APP_NAME%\
)

REM Verificar que el .exe existe
if not exist "dist\%APP_NAME%\%APP_NAME%.exe" (
    echo   ERROR: El ejecutable no fue generado.
    exit /b 1
)
echo   OK: dist\%APP_NAME%\%APP_NAME%.exe

REM ---------------------------------------------------------------------------
REM PASO 4: INNO SETUP — GENERAR EL INSTALADOR
REM ---------------------------------------------------------------------------

echo.
if "%SKIP_INNO%"=="1" (
    echo [5/5] Inno Setup: OMITIDO (--skip-inno)
    echo.
    echo   Bundle disponible en: dist\%APP_NAME%\
    goto :done
)

echo [5/5] Compilando instalador con Inno Setup...

REM Verificar que Inno Setup esta instalado
if not exist %INNO_SETUP% (
    echo.
    echo   ADVERTENCIA: Inno Setup no encontrado en:
    echo     %INNO_SETUP%
    echo.
    echo   Opciones:
    echo     A) Instalar Inno Setup 6 desde https://jrsoftware.org/isinfo.php
    echo     B) Ajustar la variable INNO_SETUP en este script con la ruta correcta
    echo     C) Ejecutar con --skip-inno para usar solo el bundle de PyInstaller
    echo.
    echo   El bundle sin instalar esta disponible en: dist\%APP_NAME%\
    goto :done
)

REM Crear directorio de salida
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

REM Compilar el instalador
%INNO_SETUP% "%INNO_SCRIPT%"
if errorlevel 1 (
    echo   ERROR: Inno Setup fallo. Revisa installer\setup.iss.
    exit /b 1
)

echo.
echo   Instalador generado: %OUTPUT_DIR%\%APP_NAME%_Setup_v%VERSION%.exe

REM ---------------------------------------------------------------------------
REM RESUMEN FINAL
REM ---------------------------------------------------------------------------

:done
echo.
echo ============================================================
echo   BUILD COMPLETADO
echo ============================================================
echo.
echo   Bundle (sin instalar):
echo     dist\%APP_NAME%\%APP_NAME%.exe
echo.
if exist "%OUTPUT_DIR%\%APP_NAME%_Setup_v%VERSION%.exe" (
    echo   Instalador:
    echo     %OUTPUT_DIR%\%APP_NAME%_Setup_v%VERSION%.exe
    echo.
)
echo   Para probar el bundle directamente:
echo     dist\%APP_NAME%\%APP_NAME%.exe
echo.
echo ============================================================

endlocal
exit /b 0
