start_gadget()
{
	while [ "1" = "1" ]
	do
		cd /d/gadget
		bin/gadget >gadget.out 2>&1
	done
}
start_gadget &
