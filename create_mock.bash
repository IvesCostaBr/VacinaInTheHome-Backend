#!/bin/bash

declare -a cpf
declare -a first_name
declare -a last_name
declare -a email
declare -a card_sus
declare -a mother
declare -a data_nascimento
declare -a rg


first_name=("Pedro" "Sandro" "andre" "gustavo","ives")
last_name=("silva" "fonseca" "matos" "henrique", "costa")
cpf=("124414141414" "12314141414" "12312313131" "2313131313","026.653.922-08")
email=("pedro@gmail.com" "sandro@gmail.com" "matos@gmail.com" "henrique@gmail.com", "ivessantoscosta@gmail.com")
password=("qwe123" "qwe123" "qwe123" "qwe123")
rg=("5923572-9","235897-2","1490822-3", "8123241-2")
mother=("MARIA VIEIRA DOS SANTOS")
data_nascimento=("2021-11-29")


count=0
for item in ${first_name[@]}
do  
    echo "from apps.user.models import User; User.objects.create_user(cpf='${cpf[$count]}', first_name='${first_name[$count]}',email='${email[$count]}', password='${password[$count]}',card_sus='${card_sus[$count]}', last_name='${last_name[$count]}', rg='${rg[$count]}', mother='${mother[$count]}')" | python manage.py shell
    count=$count+1
done
    

