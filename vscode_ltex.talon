app: vscode
title: /\.tex/
title: /\.md/
-


# Editing with the ltex extension
(l | al | lay) fix: 
    key(ctrl-.)
    
(l | al | lay) quick:
    key(ctrl-.)
    sleep(30ms)
    key(enter)

(l | al | lay) feature request: 
    user.vscode("ltex.requestFeature")

(l | al | lay) check this: 
    user.vscode("ltex.checkSelection")