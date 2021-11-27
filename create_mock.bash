#!/bin/bash

declare -a cpf
declare -a first_name
declare -a last_name
declare -a email
declare -a card_sus


first_name=("Pedro" "Sandro" "andre" "gustavo")
last_name=("silva" "fonseca" "matos" "henrique")
cpf=("124414141414" "12314141414" "12312313131" "2313131313")
email=("pedro@gmail.com" "sandro@gmail.com" "matos@gmail.com" "henrique@gmail.com")
password=("qwe123" "qwe123" "qwe123" "qwe123")


count=0
for item in ${first_name[@]}
do  
    echo "from apps.user.models import User; User.objects.create_user(cpf='${cpf[$count]}', first_name='${first_name[$count]}',email='${email[$count]}', password='${password[$count]}',card_sus='${card_sus[$count]}', last_name='${last_name[$count]}')" | python manage.py shell
    count=$count+1
done
    

