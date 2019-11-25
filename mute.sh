
set $sink `pactl list short sinks | grep RUNNING | cut -f1`
if [ $sink -z ]
then
	pactl set-sink-mute @DEFAULT_SINK@ toggle 
else
	pactl set-sink-mute $sink toggle 
fi
