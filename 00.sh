#!/bin/bash

for i in {1..33}
do
    if [ $i -lt 10 ]
    then
        touch 0$i.py
    else
        touch $i.py
    fi
done

i=1
for file in `ls`
do
    filelist[$i]=$file
    i=`expr $i + 1`
done

for file in ${filelist[@]}
do
    if [ "$file" != "00.sh" ]
    then
        echo "#!/bin/python" > $file
        chmod +x $file
    fi
done
