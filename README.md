# Artifact Hero Names Replacer (AHNR)
Reemplaza los nombres de los héroes de un idioma a otro usando la API de Artifact. El objetivo de este programa es sustituir dichos nombres de un idioma a su versión original (inglesa) para igualarlo a los nombres de Dota 2.

Por ejemplo, si se reemplaza de `spanish` a `english`, se conseguirá que **Ax** pase a ser **Axe**

Las modificaciones se aplican a:
-  Cartas
-  Lore
-  Comentarios de las cartas

Repositorio: `https://github.com/Desvelao/ahnr`

__**IMPORTANTE**__: lee atentamente el contenido de este archivo. Asegúrate de haber realizado una **copia de seguridad** de las carpetas que se mencionan en el proceso de **Aplicación del parche** antes de ejecutar el programa.

Descarga el programa ejecutable desde [aquí](https://github.com/Desvelao/ahnr/releases).

Creado por [Desvelao^^](https://desvelao.github.io/profile/).
Donaciones: a través de [Ko-fi](https://www.ko-fi.com/desvelao) o [Patreon](https://www.patreon.com/desvelao).

# Aplicación del parche

❗ *Es necesario internet para acceder a la API de Artifact*

0. __**IMPORTANTE:**__ Se recomienda realizar una **copia de seguridad** (fuera de la carpeta del juego) por si se necesitara reestablecer los archivos originales (o mira el apartado de **Restauración**), de las siguientes carpetas:
    - `Steam/SteamApps/common/Artifact/game/dcg/panorama/localization`
    - `Steam/SteamApps/common/Artifact/game/dcg/resource`

***Nota:*** *la carpeta de `Steam` suele estar en `Archivos de programa (x86)` para Windows.*

1. Descomprime el contenido del archivo .rar para que quede como se muestra dentro de la carpeta del juego ubicada en `Steam/SteamApps/common/Artifact`. ![Instalation](img/instalation.jpg)

2. Configuración del parche: `ahnr_config.txt`
    - **replace_from**: idioma base al que se modificarán los archivos. Es el mismo que se selecciona para el juego. Ej: Si juegas en Español entonces será `spanish`.
    - **replace_to**: idioma al que se convertirán los nombres de los héroes. Ej: `english`.
    - **sets**: sets id separadas por comas (,). Ej: `00,01`. Recuerda **añadir más sets** cuando se añadan al juego, por ejemplo `00,01,02`.
    - **files**: rutas relativas a archivos de localización separadas por comas (,). Ej: `
        game/dcg/resource/dcg_common_<LANG>.txt,
        game/dcg/panorama/localization/dcg_<LANG>.txt,
        game/dcg/panorama/localization/dcg_glossary_<LANG>.txt
    `
    - **files_sets**: rutas relativas de archivos de localización relacionadas con los sets separadas por comas (,). Ej: `game/dcg/resource/card_set_<SETID>_<LANG>.txt,game/dcg/panorama/localization/dcg_lore_set_<SETID>_<LANG>.txt,game/dcg/panorama/localization/dcg_vo_set_<SETID>_<LANG>.txt`

    ***Nota:***
    - `<SETID>` es la id del set. Ejemplo: 00, 01... Se sustituye en el programa automáticamente según los `sets` establecidos en el archivo de configuración `ahnr_config.txt`. Para saber hasta que id de los sets hay, mira en los directorios mencionados arriba y mira con atención su numeración en los nombres de los archivos.
    - `<LANG>` idioma base al que modificar los archivos. Esto es `replace_from` del `ahnr_config.txt`.

    Estos placeholders se cambiarán automáticamente por sus correspondientes. No borres o sustituyas `<SETID>` y `<LANG>` si no sabes lo que estás haciendo.

    - Idiomas disponibles:
        - `brazilian`
        - `english`
        - `french`
        - `german`
        - `italian`
        - `japanese`
        - `koreana`
        - `latam`
        - `russian`
        - `schinese`
        - `spanish`
        - `tchinese`

3. Inicia el ejecutable.

## Resultados del parche
Tras ejecutar el programa, se mostrarán los resultados de la aplicación del parche a los distintos archivos a reemplazar:

- ❌ **It is patched:** el archivo ya fue parcheado alguna vez anterior a esta ejecución. Los archivos parcheados, contienen al final de su contenido `//PATCHED` y sirve para saber que ese archivo ya fue modificado.
- ❌ **Without changes:** no se encontró ningún reemplazo en este archivo. Ocurrirá en los archivos de localización que no contengan nombres de héroes, aún así, se comprobarán.
- ✅ **FILE PATCHED:** se ha parcheado este archivo y se le añadió `//PATCHED` al final de éste para reconocerlo en posteriores ejecuciones del programa y evitar reparchear y poder romper el reemplazo.

# Actualización del juego
Las actualizaciones del juego pueden modificar los archivos de localización en los que se realizaron reemplazos, por lo que se perdería la traducción realizada. Puedes saberlo si tras una actualización del juego, la fecha de modificación de los archivos que parcheaste previamente ha cambiado o ver si el texto de los archivos que se modificaron tienen al final `//PATCHED`.

❗ **Tras una actualización del juego, recuerda reaplicar el parche para ver si hay algo nuevo que necesite modificarse.**

# Restauración
Si necesitas o quieres restaurar los archivos originales tras aplicar el parche, puedes:
- reestablecer la copia de seguridad que hiciste de los archivos
- verificar la integridad de los archivos (los reestablece a los originales y actualizados)
- reinstalar el juego (como última opción)

❗ Cuidado con mantener **copias de seguridad muy antiguas**, pues al reestablecerlas, si fueron anteriores a alguna actualización que añadió más información a los archivos de localización y ésta no se encuentra, puede dar lugar a errores. Por ello, se recomienda verificar la integridad de los archivos si se quiere restaurarlos.

## Verificar la integridad de los archivos
Desde la biblioteca de Steam, clica con botón derecho del ratón sobre el juego (Artifact) y selecciona `Propiedades`. Luego ve a la pestaña de `Archivos Locales` y por último pulsa `Verificar la integridad de los archivos`. Esto comprabará si los archivos de tu juego son correctos y los que no, los descargará y reemplazará. El parcheo desaparecerá.


# Vista previa
Ej: reemplazo de `spanish` a `english`.

En el archivo de configuración (ahnr_config.txt):
```
replace_from = spanish
replace_to = english
...
```

![game-patched](img/game-patched.png)

# Errores en el programa

Si encuentras algún problema en el programa puedes repórtarlo en los [issues](https://github.com/Desvelao/ahnr/issues) de este mismo repositorio o ponte en contacto conmigo a través de otro medio (en Discord **Desvelao^^#2956**).