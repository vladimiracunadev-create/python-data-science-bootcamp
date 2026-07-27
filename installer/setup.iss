; setup.iss — Script de Inno Setup para el Python Data Science Program
;
; Genera: PythonDSProgram_Setup_v3.9.0.exe
;
; Requisitos:
;   - Inno Setup 6+ instalado: https://jrsoftware.org/isinfo.php
;   - PyInstaller ya corrio: dist\PythonDSProgram\ debe existir
;
; Uso desde linea de comandos:
;   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer\setup.iss
;
; O abrir este archivo en el IDE de Inno Setup y presionar F9.

; ---------------------------------------------------------------------------
; INFORMACION DEL INSTALADOR
; ---------------------------------------------------------------------------

[Setup]
; Nombre de la aplicacion — aparece en Agregar o quitar programas
AppName=Python Data Science Program

; Version del producto
AppVersion=3.9.0

; Identificador unico de la aplicacion (GUID)
; Cambiar si se crea una aplicacion completamente nueva
AppId={{B7C8D9E0-F1A2-3B4C-5D6E-7F8A9B0C1D2E}

; Publicador — aparece en Agregar o quitar programas
AppPublisher=Python Data Science Program

; URL de soporte
AppSupportURL=https://github.com/vladimiracunadev-create/python-data-science-program

; Carpeta de instalacion por defecto
; {pf} = Program Files (por ejemplo C:\Program Files)
DefaultDirName={pf}\PythonDSProgram

; Nombre del grupo en el Menu de inicio
DefaultGroupName=Python Data Science Program

; Nombre del archivo instalador de salida (sin .exe)
OutputBaseFilename=PythonDSProgram_Setup_v3.9.0

; Directorio de salida del instalador generado
OutputDir=..\dist_installer

; Comprension del instalador
; lzma/ultra da el mejor ratio a costa de tiempo de compilacion
Compression=lzma/ultra
SolidCompression=yes

; Icono del instalador
; SetupIconFile=..\installer\icon.ico

; Mostrar asistente con bienvenida
DisableWelcomePage=no

; Permitir instalacion sin permisos de administrador
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog

; Idioma del asistente
; Inno Setup soporta espanol con el archivo SpanishStandard.isl
; Si no esta instalado, usa English
; LanguageDetectionMethod=locale

; ---------------------------------------------------------------------------
; IDIOMAS
; ---------------------------------------------------------------------------

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

; ---------------------------------------------------------------------------
; TAREAS (checkboxes durante la instalacion)
; ---------------------------------------------------------------------------

[Tasks]
; Acceso directo en el escritorio
Name: "desktopicon"; Description: "Crear acceso directo en el Escritorio"; GroupDescription: "Accesos directos:"; Flags: unchecked

; Acceso directo en la barra de inicio rapido
Name: "quicklaunchicon"; Description: "Agregar al area de inicio rapido"; GroupDescription: "Accesos directos:"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

; Iniciar automaticamente con Windows
Name: "startup"; Description: "Iniciar el Programa al encender Windows (no recomendado)"; GroupDescription: "Inicio automatico:"; Flags: unchecked

; ---------------------------------------------------------------------------
; ARCHIVOS A INSTALAR
; ---------------------------------------------------------------------------

[Files]
; Copiar todo el directorio generado por PyInstaller
; dest: {app} = directorio de instalacion elegido por el usuario
Source: "..\dist\PythonDSProgram\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

; NOTA: No se incluyen los archivos fuente (.py) — solo el ejecutable compilado.
; Los datasets y materiales de clase ya estan embebidos en el bundle de PyInstaller.

; ---------------------------------------------------------------------------
; ACCESOS DIRECTOS
; ---------------------------------------------------------------------------

[Icons]
; Menu de inicio
Name: "{group}\Python Data Science Program";         Filename: "{app}\PythonDSProgram.exe";   WorkingDir: "{app}"; Comment: "Iniciar el Python Data Science Program"
Name: "{group}\Desinstalar Python DS Program";       Filename: "{uninstallexe}"

; Escritorio (solo si se selecciono la tarea)
Name: "{autodesktop}\Python Data Science Program";   Filename: "{app}\PythonDSProgram.exe";   WorkingDir: "{app}"; Comment: "Iniciar el Python Data Science Program"; Tasks: desktopicon

; Barra de inicio rapido (Windows XP/Vista)
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Python Data Science Program"; Filename: "{app}\PythonDSProgram.exe"; WorkingDir: "{app}"; Tasks: quicklaunchicon

; Inicio automatico con Windows (opcional)
Name: "{userstartup}\Python Data Science Program"; Filename: "{app}\PythonDSProgram.exe"; WorkingDir: "{app}"; Tasks: startup

; ---------------------------------------------------------------------------
; EJECUTAR AL TERMINAR LA INSTALACION
; ---------------------------------------------------------------------------

[Run]
; Ofrecer iniciar la aplicacion al cerrar el asistente
Filename: "{app}\PythonDSProgram.exe"; Description: "Iniciar el Programa ahora"; Flags: nowait postinstall skipifsilent runasoriginaluser; WorkingDir: "{app}"

; ---------------------------------------------------------------------------
; DESINSTALACION
; ---------------------------------------------------------------------------

[UninstallRun]
; Antes de desinstalar, intentar cerrar la aplicacion si esta corriendo
Filename: "taskkill.exe"; Parameters: "/F /IM PythonDSProgram.exe"; Flags: runhidden; RunOnceId: "KillProgram"

[UninstallDelete]
; Eliminar los notebooks guardados por los alumnos (directorio de trabajo)
; ADVERTENCIA: si el alumno guardo trabajo ahi, se pierde.
; Comentar esta linea para NO borrar los datos del alumno al desinstalar.
; Type: filesandordirs; Name: "{app}\app\saved_notebooks"

; ---------------------------------------------------------------------------
; MENSAJES PERSONALIZADOS
; ---------------------------------------------------------------------------

[Messages]
; Mensaje en la pagina de bienvenida
WelcomeLabel1=Bienvenido al instalador del%nPython Data Science Program
WelcomeLabel2=Este asistente instalara el Python Data Science Program en tu computador.%n%nEl programa incluye:%n  - 232 clases de Python y Data Science (9 partes)%n  - Viewer Qt nativo (PySide6) con READMEs y notebooks%n  - Material descargable (PDFs y PPTX por clase)%n%nNo se requiere conexion a internet.%nAbre una ventana de escritorio Qt nativa (no usa navegador, no levanta servidor local).

; ---------------------------------------------------------------------------
; CODIGO PASCAL (logica personalizada)
; ---------------------------------------------------------------------------

[Code]
// Verificar que Windows 10 o superior esta instalado
function InitializeSetup(): Boolean;
var
  WindowsVersion: TWindowsVersion;
begin
  GetWindowsVersionEx(WindowsVersion);
  if WindowsVersion.Major < 10 then
  begin
    MsgBox('Este instalador requiere Windows 10 o superior.', mbError, MB_OK);
    Result := False;
  end
  else
    Result := True;
end;

// Mostrar confirmacion antes de desinstalar
function InitializeUninstall(): Boolean;
begin
  Result := MsgBox('Deseas desinstalar el Python Data Science Program?', mbConfirmation, MB_YESNO) = IDYES;
end;
