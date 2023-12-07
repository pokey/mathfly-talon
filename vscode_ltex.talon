app: vscode
title: /\.tex/
title: /\.md/
title: /\.bib/
-


# Editing with the ltex extension
(l | al) fix: 
    key(ctrl-.)
    
(l | al) accept:
    key(ctrl-.)
    sleep(30ms)    
    key(enter)

(l | al) activate:
    user.vscode("ltex.activateExtension")

(l | al) check this: 
    user.vscode("ltex.checkSelection")

(l | al) check file: 
    user.vscode("ltex.checkCurrentDocument")

(l | al) check all: 
    user.vscode("ltex.checkAllDocumentsInWorkspace")

(l | al) clear file: 
    user.vscode("ltex.clearDiagnosticsInCurrentDocument")

(l | al) clear all: 
    user.vscode("ltex.clearAllDiagnostics")

(l | al) [show] status: 
    user.vscode("ltex.showStatusInformation")

(l | al) request feature: 
    user.vscode("ltex.requestFeature")