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

# latex workshop commands
bar lay [tech]: user.vscode("workbench.view.extension.latex-workshop-activitybar")
(bar | lay) (command | commands): user.vscode("latex-workshop-commands.focus") 
(bar | lay) structure: user.vscode("latex-workshop-structure.focus")
lay math: user.vscode("latex-workshop.toggleMathPreviewPanel")


lay (run | build): user.vscode("latex-workshop.build")
lay clean: user.vscode("latex-workshop.clean")
lay demote: user.vscode("latex-workshop.demote")
lay promote: user.vscode("latex-workshop.promote")
lay (sink | sync) [tack | tech]: user.vscode("latex-workshop.synctex")
lay math: user.vscode("latex-workshop.toggleMathPreviewPanel")

# View PDF
lay view [p d f]:user.vscode("latex-workshop.view")
lay view external:user.vscode("latex-workshop.viewExternal")
lay view tab:user.vscode("latex-workshop.tab")

# Bib file
[lay] bib align: user.vscode("latex-workshop.bibalign")
[lay] bib sort: user.vscode("latex-workshop.bibsort")
[lay] bib (align sort | also): user.vscode("latex-workshop.bibalignsort")


#lay [tech] m k: user.vscode("latex-workshop.recipes")
lay (kill | stop): user.vscode("latex-workshop.kill")
lay dock: user.vscode("latex-workshop.texdoc")

















{
  "key": "ctrl+alt+m",
  "command": "latex-workshop.toggleMathPreviewPanel",
  "when": "!config.latex-workshop.bind.altKeymap.enabled && editorLangId =~ /^latex$|^latex-expl3$|^rsweave$|^jlweave$|^pweave$/"
}
    {
        "key": "ctrl+l alt+x",
        "command": "workbench.view.extension.latex-workshop-activitybar",
        "when": "config.latex-workshop.bind.altKeymap.enabled"
      }