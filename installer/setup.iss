; setup.iss — Script de Inno Setup para el Bootcamp Python DS
;
; Genera: BootcampPythonDS_Setup_v1.0.0.exe
;
; Requisitos:
;   - Inno Setup 6+ instalado: https://jrsoftware.org/isinfo.php
;   - PyInstaller ya corrio: dist\BootcampPythonDS\ debe existir
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
AppName=Bootcamp Python para Data Science

; Version del producto
AppVersion=1.0.0

; Identificador unico de la aplicacion (GUID)
; Cambiar si se crea una aplicacion completamente nueva
AppId={{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}

; Publicador — aparece en Agregar o quitar programas
AppPublisher=Bootcamp Python DS

; URL de soporte
AppSupportURL=https://github.com/vladimiracunadev-create/python-data-science-bootcamp

; Carpeta de instalacion por defecto
; {pf} = Program Files (por ejemplo C:\Program Files)
DefaultDirName={pf}\BootcampPythonDS

; Nombre del grupo en el Menu de inicio
DefaultGroupName=Bootcamp Python DS

; Nombre del archivo instalador de salida (sin .exe)
OutputBaseFilename=BootcampPythonDS_Setup_v1.0.0

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
Name: "startup"; Description: "Iniciar el Bootcamp al encender Windows (no recomendado)"; GroupDescription: "Inicio automatico:"; Flags: unchecked

; ---------------------------------------------------------------------------
; ARCHIVOS A INSTALAR
; ---------------------------------------------------------------------------

[Files]
; Copiar todo el directorio generado por PyInstaller
; dest: {app} = directorio de instalacion elegido por el usuario
Source: "..\dist\BootcampPythonDS\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

; NOTA: No se incluyen los archivos fuente (.py) — solo el ejecutable compilado.
; Los datasets y materiales de clase ya estan embebidos en el bundle de PyInstaller.

; ---------------------------------------------------------------------------
; ACCESOS DIRECTOS
; ---------------------------------------------------------------------------

[Icons]
; Menu de inicio
Name: "{group}\Bootcamp Python DS";         Filename: "{app}\BootcampPythonDS.exe";   WorkingDir: "{app}"; Comment: "Iniciar el Bootcamp Python para Data Science"
Name: "{group}\Desinstalar Bootcamp";       Filename: "{uninstallexe}"

; Escritorio (solo si se selecciono la tarea)
Name: "{autodesktop}\Bootcamp Python DS";   Filename: "{app}\BootcampPythonDS.exe";   WorkingDir: "{app}"; Comment: "Iniciar el Bootcamp Python para Data Science"; Tasks: desktopicon

; Barra de inicio rapido (Windows XP/Vista)
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Bootcamp Python DS"; Filename: "{app}\BootcampPythonDS.exe"; WorkingDir: "{app}"; Tasks: quicklaunchicon

; Inicio automatico con Windows (opcional)
Name: "{userstartup}\Bootcamp Python DS"; Filename: "{app}\BootcampPythonDS.exe"; WorkingDir: "{app}"; Tasks: startup

; ---------------------------------------------------------------------------
; EJECUTAR AL TERMINAR LA INSTALACION
; ---------------------------------------------------------------------------

[Run]
; Ofrecer iniciar la aplicacion al cerrar el asistente
Filename: "{app}\BootcampPythonDS.exe"; Description: "Iniciar el Bootcamp ahora"; Flags: nowait postinstall skipifsilent runasoriginaluser; WorkingDir: "{app}"

; ---------------------------------------------------------------------------
; DESINSTALACION
; ---------------------------------------------------------------------------

[UninstallRun]
; Antes de desinstalar, intentar cerrar la aplicacion si esta corriendo
Filename: "taskkill.exe"; Parameters: "/F /IM BootcampPythonDS.exe"; Flags: runhidden; RunOnceId: "KillBootcamp"

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
WelcomeLabel1=Bienvenido al instalador del%nBootcamp Python para Data Science
WelcomeLabel2=Este asistente instalara el Bootcamp Python DS en tu computador.%n%nEl Bootcamp incluye:%n  - 12 clases de Python y Data Science%n  - Laboratorio interactivo local%n  - Datasets de practica%n  - Guias y materiales de clase%n%nNo se requiere conexion a internet.%nAbre una ventana de escritorio nativa (no un navegador).

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
  Result := MsgBox('Deseas desinstalar el Bootcamp Python DS?', mbConfirmation, MB_YESNO) = IDYES;
end;
