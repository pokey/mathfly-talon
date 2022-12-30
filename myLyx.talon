app: lyx
app: LyX.exe
app: LyX2.3.exe
app: LyX for Windows
-
tag(): user.maths

creation:
    insert("a")
    user.maths_superscript(“\\dagger ”)

ket:
    insert("\\lvert ")
    insert(">")
    key(left)
    insert("\\mbox ") 
bra:
    insert("<")
    insert("\\rvert ")
    key(left)
    insert("\\mbox ") 