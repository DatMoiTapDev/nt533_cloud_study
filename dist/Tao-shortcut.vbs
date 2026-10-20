Option Explicit
Dim sh, fso, folder, shortcut
Set sh = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
folder = fso.GetParentFolderName(WScript.ScriptFullName)
Set shortcut = sh.CreateShortcut(sh.SpecialFolders("Desktop") & "\CloudLab.lnk")
shortcut.TargetPath = folder & "\Mo-CloudLab.cmd"
shortcut.WorkingDirectory = folder
shortcut.Description = "CloudLab - Hoc Dien toan dam may offline"
shortcut.IconLocation = "shell32.dll, 20"
shortcut.Save
MsgBox "Da tao shortcut CloudLab tren Desktop. Giu nguyen vi tri thu muc ung dung.", 64, "CloudLab"
