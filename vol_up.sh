
set $sink `pactl list short sinks | grep RUNNING | cut -f1`
if [ $sink -z ]
then
	pactl set-sink-volume @DEFAULT_SINK@ +5%
else
	pactl set-sink-volume $sink +5%
fi
