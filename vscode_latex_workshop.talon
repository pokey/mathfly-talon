# Commands to work with the VScode extension LaTeX Workshop
# (https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
app: vscode
title: /\.tex/
title: /\.bib/
-



# latex workshop commands
bar lay [tech]: user.vscode("workbench.view.extension.latex-workshop-activitybar")
(bar | lay) (command | commands): user.vscode("latex-workshop-commands.focus") 
(bar | lay) structure: user.vscode("latex-workshop-structure.focus")

lay (run | build): user.vscode("latex-workshop.build")
lay clean: user.vscode("latex-workshop.clean")
lay demote: user.vscode("latex-workshop.demote")
lay promote: user.vscode("latex-workshop.promote")
lay (sink | sync) [tack | tech]: user.vscode("latex-workshop.synctex")
lay math: user.vscode("latex-workshop.toggleMathPreviewPanel")

# View PDF
lay view [p d f]: user.vscode("latex-workshop.view")
lay view external: user.vscode("latex-workshop.viewExternal")
lay view tab: user.vscode("latex-workshop.tab")

# Bib file
[lay] bib align: user.vscode("latex-workshop.bibalign")
[lay] bib sort: user.vscode("latex-workshop.bibsort")
[lay] bib also: user.vscode("latex-workshop.bibalignsort")


#lay [tech] m k: user.vscode("latex-workshop.recipes")
lay (kill | stop): 
    user.vscode("latex-workshop.kill")
    sleep(30ms)
    user.vscode("latex-workshop.kill")
    sleep(30ms)
    user.vscode("latex-workshop.kill")
lay dock: user.vscode("latex-workshop.texdoc")







