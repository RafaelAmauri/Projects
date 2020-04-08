xrandr --output $(xrandr --verbose |egrep '\ connected'|cut -d' ' -f1)  --brightness $1
