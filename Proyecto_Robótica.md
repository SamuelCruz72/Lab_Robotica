# Proyecto Robótica Industrial - Automatización del Proceso de Preparación de Arepas
En este informe se describe el proceso de desarrollo de un sistema robótico para automatizar el proceso de preparación de arepas, para ello se detalla el proceso de diseño y construcción de un gripper para que el robot ABB IRB-140 agarre las arepas de una mesa, las coloque en una parrilla, las voltee una vez estén cocidas y las recoja de la parrilla una vez estén totalmente cocinadas; a su vez se describe el proceso de generación de trayectorias para que el robot se acerque a las arepas, las tome, las voltee y las deje en los lugares deseados.

## Diseño del Gripper y las Arepas

En primer lugar se diseñó el mecanismo del gripper, para ello se propusieron algunos bocetos del mecanismo que abría y cerraba una pinza mediante el accionamiento de un gripper electroneumático MCHA-20, estas fueron algunas de las opciones propuestas: 

<p align="center">
   <img src="Figuras\Proyecto\Boceto general.jpg" alt="boceto" width="100"><br> 

<p align="center">
   <img src="Figuras\Proyecto\boceto mecanismo.jpg" alt="boceto2" width="100"><br> 

Se terminó optando por la segunda opción dado que permitía el ajuste en la apertura máxima y el cierre mínimo del gripper con tan solo modificar la distancia de los eslabones que componen el mecanismo, con lo cual el siguiente paso fue determinar la longitud de cada uno de los eslabones que componen el mecanismo, para ello se empleó el software de Inventor y por medio del modelado por boceto con una serie de iteraciones se halló la siguiente configuración óptima de longitudes de eslabones que permitía un cierre adecuado para el agarre de las arepas:

<p align="center">
   <img src="Figuras\Proyecto\Boceto Inventor.jpg" alt="boceto Inventor" width="700"><br> 

Consiguientemente, se diseñó la pinza que agarraría las arepas, esta debía tratar a las arepas con suavidad para evitar que se desarmen y debía evitar que se desplazaran horizontalmente cuando el gripper se cerrara para garantizar un correcto agarre de la arepa. Al igual que con el mecanismo, se propusieron algunos bocetos para garantizar la función deseada:

<p align="center">
   <img src="Figuras\Proyecto\Boceto Pinza.jpg" alt="boceto pinza" width="300"><br> 

<p align="center">
   <img src="Figuras\Proyecto\Pinza boceto.jpg" alt="boceto2 pinza" width="150"><br> 

El diseño electo fue la primera opción dado que reducía considerablemente el desplazamiento de la arepa al momento del cierre y evitaba que la arepa se cayera de la pinza cuando se volteara de la estufa. Posteriormente, se modelaron todas las piezas que componen el mecanismo y se ensamblaron con el software Inventor de la siguiente forma:


Finalmente, con dicho modelado se imprimió todo el mecanismo con filamento de PLA en una impresora 3D y se ensambló con tornillos de 3 mm de diámetro: 


## Distribución del Espacio

## Secuencia General de Movimientos
