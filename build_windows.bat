@echo off
REM build_windows.bat — Genera el instalador y el portable de Windows
REM
REM Requisitos previos:
REM   - Python 3.10+ instalado y en PATH
REM   - pip install -r requirements.txt ejecutado
REM   - Inno Setup 6 instalado en la ruta por defecto (para el instalador)
REM
REM Que hace este script:
REM   1. Verifica Python y dependencias
REM   2. Instala pywebview si falta
REM   3. Construye el bundle con PyInstaller
REM   4. Empaqueta el ZIP portable
REM   5. Compila el instalador con Inno Setup
REM
REM Uso:
REM   build_windows.bat
REM   build_windows.bat --skip-pyinstaller    (bundle ya existe)
REM   build_windows.bat --skip-inno           (solo bundle + ZIP, sin instalador)

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
set PORTABLE_DIR=release_artifacts

set SKIP_PYINSTALLER=0
set SKIP_INNO=0

for %%A in (%*) do (
    if "%%A"=="--skip-pyinstaller" set SKIP_PYINSTALLER=1
    if "%%A"=="--skip-inno"        set SKIP_INNO=1
)

REM ---------------------------------------------------------------------------
REM BANNER
REM ---------------------------------------------------------------------------

echo.
echo ============================================================
echo   BOOTCAMP PYTHON DS ^| BUILD WINDOWS v%VERSION%
echo ============================================================
echo.

REM ---------------------------------------------------------------------------
REM PASO 1: VERIFICAR PYTHON
REM ---------------------------------------------------------------------------

echo [1/6] Verificando Python...
%PYTHON% --version >nul 2>&1
if errorlevel 1 (
    echo   ERROR: Python no encontrado en PATH.
    echo   Descarga Python 3.10+ desde https://python.org/downloads/
    echo   Marca "Add Python to PATH" durante la instalacion.
    exit /b 1
)
for /f "tokens=*" %%v in ('%PYTHON% --version') do set PYTHON_VER=%%v
echo   OK: !PYTHON_VER!

REM ---------------------------------------------------------------------------
REM PASO 2: VERIFICAR / INSTALAR DEPENDENCIAS
REM ---------------------------------------------------------------------------

echo.
echo [2/6] Verificando dependencias de la app...
%PYTHON% -c "import flask, pandas, sklearn, matplotlib, nbformat" >nul 2>&1
if errorlevel 1 (
    echo   Instalando requirements.txt...
    %PIP% install -r requirements.txt
    if errorlevel 1 (
        echo   ERROR: No se pudieron instalar las dependencias.
        exit /b 1
    )
)
echo   OK: flask, pandas, scikit-learn, matplotlib, nbformat

REM ---------------------------------------------------------------------------
REM PASO 3: VERIFICAR / INSTALAR PYWEBVIEW
REM ---------------------------------------------------------------------------

echo.
echo [3/6] Verificando pywebview...
%PYTHON% -c "import webview" >nul 2>&1
if errorlevel 1 (
    echo   Instalando pywebview...
    %PIP% install pywebview
    if errorlevel 1 (
        echo   ERROR: No se pudo instalar pywebview.
        echo   Intenta manualmente: pip install pywebview
        exit /b 1
    )
)
for /f "tokens=*" %%v in ('%PYTHON% -c "import webview; print(webview.__version__)"') do set WV_VER=%%v
echo   OK: pywebview !WV_VER!

REM ---------------------------------------------------------------------------
REM PASO 4: VERIFICAR / INSTALAR PYINSTALLER
REM ---------------------------------------------------------------------------

echo.
echo [4/6] Verificando PyInstaller...
%PYTHON% -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo   Instalando PyInstaller...
    %PIP% install pyinstaller
    if errorlevel 1 (
        echo   ERROR: No se pudo instalar PyInstaller.
        exit /b 1
    )
)
for /f "tokens=*" %%v in ('%PYTHON% -m PyInstaller --version') do set PYIN_VER=%%v
echo   OK: PyInstaller !PYIN_VER!

REM ---------------------------------------------------------------------------
REM PASO 5: PYINSTALLER — GENERAR EL BUNDLE
REM ---------------------------------------------------------------------------

echo.
if "%SKIP_PYINSTALLER%"=="1" (
    echo [5/6] PyInstaller: OMITIDO --skip-pyinstaller
    if not exist "dist\%APP_NAME%\%APP_NAME%.exe" (
        echo   ERROR: dist\%APP_NAME%\%APP_NAME%.exe no existe. Regeneralo sin --skip-pyinstaller.
        exit /b 1
    )
) else (
    echo [5/6] Construyendo bundle con PyInstaller...
    echo   Spec: %SPEC_FILE%
    echo   Esto puede tardar varios minutos la primera vez...
    echo.

    if exist "build\%APP_NAME%" (
        echo   Limpiando build anterior...
        rmdir /s /q "build\%APP_NAME%"
    )

    %PYTHON% -m PyInstaller %SPEC_FILE% --noconfirm --log-level WARN
    if errorlevel 1 (
        echo.
        echo   ERROR: PyInstaller fallo. Ejecuta con --log-level DEBUG para mas detalle.
        exit /b 1
    )
    echo.
    echo   Bundle generado en: dist\%APP_NAME%\
)

if not exist "dist\%APP_NAME%\%APP_NAME%.exe" (
    echo   ERROR: El ejecutable no fue generado.
    exit /b 1
)
echo   OK: dist\%APP_NAME%\%APP_NAME%.exe

REM ---------------------------------------------------------------------------
REM EMPAQUETAR PORTABLE (ZIP)
REM ---------------------------------------------------------------------------

echo.
echo   Empaquetando version portable...

if not exist "%PORTABLE_DIR%" mkdir "%PORTABLE_DIR%"

set PORTABLE_ZIP=%PORTABLE_DIR%\%APP_NAME%_windows_portable_v%VERSION%.zip

REM Eliminar zip anterior si existe
if exist "%PORTABLE_ZIP%" del /f /q "%PORTABLE_ZIP%"

REM Usar PowerShell para comprimir (disponible en Win10+)
powershell -NoProfile -Command ^
  "Compress-Archive -Path 'dist\%APP_NAME%\*' -DestinationPath '%PORTABLE_ZIP%' -Force"

if errorlevel 1 (
    echo   ADVERTENCIA: No se pudo crear el ZIP portable.
    echo   Puedes comprimir manualmente la carpeta dist\%APP_NAME%\
) else (
    echo   OK: %PORTABLE_ZIP%
)

REM ---------------------------------------------------------------------------
REM PASO 6: INNO SETUP — GENERAR EL INSTALADOR
REM ---------------------------------------------------------------------------

echo.
if "%SKIP_INNO%"=="1" (
    echo [6/6] Inno Setup: OMITIDO --skip-inno
    goto :done
)

echo [6/6] Compilando instalador con Inno Setup...

if not exist %INNO_SETUP% (
    echo.
    echo   ADVERTENCIA: Inno Setup no encontrado en %INNO_SETUP%
    echo   Opciones:
    echo     A) Instalar Inno Setup 6 desde https://jrsoftware.org/isinfo.php
    echo     B) Ajustar la variable INNO_SETUP en este script
    echo     C) Ejecutar con --skip-inno para solo bundle + ZIP portable
    echo.
    goto :done
)

if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

%INNO_SETUP% "%INNO_SCRIPT%"
if errorlevel 1 (
    echo   ERROR: Inno Setup fallo. Revisa installer\setup.iss.
    exit /b 1
)
echo   OK: %OUTPUT_DIR%\%APP_NAME%_Setup_v%VERSION%.exe

REM ---------------------------------------------------------------------------
REM RESUMEN FINAL
REM ---------------------------------------------------------------------------

:done
echo.
echo ============================================================
echo   BUILD COMPLETADO
echo ============================================================
echo.
echo   Portable (descomprimir y ejecutar BootcampPythonDS.exe):
echo     %PORTABLE_ZIP%
echo.
if exist "%OUTPUT_DIR%\%APP_NAME%_Setup_v%VERSION%.exe" (
    echo   Instalador (doble clic para instalar):
    echo     %OUTPUT_DIR%\%APP_NAME%_Setup_v%VERSION%.exe
    echo.
)
echo   NOTA: El ejecutable abre una ventana de escritorio nativa.
echo   No se abre ningun navegador. No usa localhost visible.
echo   Requiere Edge WebView2 Runtime (incluido en Win10 20H2+ y Win11).
echo.
echo ============================================================

endlocal
exit /b 0
