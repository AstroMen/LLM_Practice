home=$HOME/BERT/binary
out=$HOME/BERT/output

cd $home
for lib in *
do
    if [ ! "$lib" = "openssl" ]; then  # fix: add missing ]
        cd $home/$lib
        for lib_version in *
        do

            cd $home/$lib/$lib_version
            echo $home/$lib/$lib_version
            libname_version="$lib@$lib_version"
        mkdir -p $out/$libname_version
            for bin in *
            do
                rm /home/lian/BERT/ghidra/diff* -r
                cd /home/lian/BERT
            /home/administrator/Downloads/Lian/ghidra_9.2.2_PUBLIC/support/analyzeHeadless /home/lian/BERT/ghidra diff -import $home/$lib/$lib_version/$bin -scriptPath /home/lian/BERT/ -postScript preprocess.py $libname_version/$bin
            done

        done
        echo $lib
    else
        echo "Skipping $lib"
    fi
done