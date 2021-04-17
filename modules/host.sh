#!/bin/bash
echo -e "
      ▄   ▄
 ▄█▄ █▀█▀█ ▄█▄
▀▀████▄█▄████▀▀
      ▀█▀█▀

"
echo -e -n "Introduzca la ip: "
read -r host
w3m -dump https://api.hackertarget.com/nmap/?q=$host

echo ""
echo -e "Busqueda Realizada"