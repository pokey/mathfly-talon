app: lyx
app: LyX.exe
-
tag(): user.maths

#for manipulating second quantization

create <user.key_or_letter>:
    insert("a")
    user.maths_superscript("\\dagger ")

destroy <user.any_alphanumeric_key>:
    insert("a")
    user.maths_subscript(any_alphanumeric_key)
    
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

plain ket:
    insert("\\lvert ")
    insert("vac")
    insert(">")
    key(right)
    key(right)

plain bra:
    insert("<")
    insert("vac")
    insert("\\rvert ")
    # key(right)
    # key(right)