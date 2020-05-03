html=/var/WWW/html/biocomp2
cgi=/var/WWW/cgi-bin/biocomp2

mkdir -p $html
mkdir -p $cgi

cp -R html/* $html
cp -R html/css/* $html
cp -R cgi-biocomp2/* $cgi

