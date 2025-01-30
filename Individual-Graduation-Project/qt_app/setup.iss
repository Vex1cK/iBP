[Setup]
AppName=BriefTalkAI
AppVersion=1.0
DefaultDirName={pf}\BriefTalkAI
DefaultGroupName=BriefTalkAI
OutputDir=.
OutputBaseFilename=BriefTalkAI_Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\BriefTalkAI\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{commondesktop}\BriefTalkAI"; Filename: "{app}\BriefTalkAI.exe"

[Run]
Filename: "{app}\BriefTalkAI.exe"; Description: "Запустить BriefTalkAI"; Flags: nowait postinstall skipifsilent
