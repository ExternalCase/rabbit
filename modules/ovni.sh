#!/bin/bash
restartprogram() {
echo "
Esa Opción es incorrecta, elije de nuevo !
Elige entre el [ 1-2-3 ]"
sleep 2
clear
menuoption
}

miIP() {
	read -p " Dale Enter para continuar ! > " enter
	command=$(wget https://ipapi.co/yaml/ -q -O .-)
	echo -e "\e[36m"
	cat .-
	echo " "
	rm .-
	exit
}
tarjetaip() {
    echo ""
	echo ""
	echo -e -n "\e[36m Escribe la dirección IP: \e[0m"
    read -r target
	command=$(wget https://ipapi.co/$target/yaml/ -q -O .-)
	echo -e "\e[36m "
	cat .-
	echo " "
	rm .-
	exit
}
    
menuoption() {
        echo -e ""
	echo -e "\e[1;34m[1]\e[0m" "\e[36mInformación de mi IP\e[0m"
	echo -e "\e[1;34m[2]\e[0m" "\e[36mInformación de una IP\e[0m"
    echo -e "\e[1;32m"
	read -p "[+]~$ " get
	if [ $get -eq 1 ];
		then
			miIP
	elif [ $get -eq 2 ];
		then
			tarjetaip                                            
	else
	echo -e "Opcion incorrecta :!"
		sleep 1
		restartprogram
	fi

}


menuoption
