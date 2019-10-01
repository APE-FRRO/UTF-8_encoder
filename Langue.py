# -*- coding: utf-8 -*-

# -------------------- LIST OF LANGUAGES --------------------------------
NB_LANGUE = 4

liste_langue = \
 "Language_Degree_",\
 "Langue_Degré_",\
 "Idioma_Grado_",\
 "Язык_Градус_" 
 
nom_langue = \
"const char __ENG[] ",\
"const char __FRA[] ",\
"const char __ESP[] ",\
"const char __RUS[] "

liste_indice = "Tab_English[] ","Tab_French[] ", "Tab_Espagnol[] ", "Tab_Russie[] "

# ------------------------- FUNCTIONS -----------------------------------
# ---- CONVERSION -----
def convUTF8 (string):
    conv = ''
    i = 0

    while i < len(string):                          # for every character include in a specific language
        try:
            conv += hex(ord(string[i]))             # try to find translate ascii to utf-8 value
        except:
            conv += string[i]                       # if it doesn't work, keep utf-16 value, brut

        i+=1                                        # character ++

    result = conv.replace("0x5f","\\0")             # change character "_" = 0x5F to "\0"
    result = result.replace("0x","\\x")             # change character "0x" to "\x"

    return result

# ---- CALCUL INDICE -----
def calcIndice (string):
    indice = '0'
    i = 0

    while i < len(string):                          # for every character include in a specific language
        if (string[i] == "_"):                      # try to find translate ascii to utf-8 value
            indice += ','                           # if it doesn't work, keep utf-16 value, brut
            indice += str(i+1)

        i+=1                                        # character ++
    return indice

# ---- FORMATTAGE LANGUE -----
def formattageLangue (string, nbLangue):            # create array of words like that : "const char __ENG[] = {"\x53...\0"};"
    result = nom_langue[nbLangue]                   # param[in] string : converted file by "convUTF8"
    result += "= {\""                               # param[in] nbLangue : numéro de la langue
    result += string
    result += " \"};"
    result += "\n"
    return result

# ---- FORMATTAGE INDICE -----
def formattageIndice (string, nbLangue):            # create array of index of eeach works like that : "const uint16_t Tab_English[] = {0,9,...};"
    result = "const uint16_t "                      # param[in] string : calculated by "calcIndice"
    result += liste_indice[nbLangue]                # param[in] nbLangue : numéro de la langue    
    result += "= {"
    result += string
    result += "};"
    result += "\n"
    return result

# --------------------------- MAIN ------------------------------------
object = open(".\langue.txt", "w");
i = 0
j = 0
while i < NB_LANGUE:
    langue = formattageLangue(convUTF8 (liste_langue[i]), i)
    object.write(langue);
    i+=1
    
object.write("\n");

while j < NB_LANGUE:
    indice = formattageIndice(calcIndice(liste_langue[j]), j)
    object.write(indice);
    j+=1

object.close()
