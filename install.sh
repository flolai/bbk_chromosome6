html=~/WWW/html/biocomp2
cgi=~/WWW/cgi-bin/biocomp2

mkdir -p $html
mkdir -p $cgi

cp -R html/* $html
cp -R html/css/* $html
cp -R cgi-biocomp2/bl/*.py $cgi
cp -R cgi-biocomp2/db/*.py $cgi
cp -R cgi-biocomp2/cgi/*.py $cgi
