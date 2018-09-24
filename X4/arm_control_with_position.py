#-------------------------------------------------------
#
# arm-control program
#
#-------------------------------------------------------
import sys
import arm_control

args = sys.argv

x_position = int(args[1])
y_position = int(args[2])

# x

if   x_position < 124:
  x_degree = -10
elif x_position < 221:
  x_degree = -8
elif x_position < 310:
  x_degree = -5
elif x_position < 394:
  x_degree = -2
elif x_position < 496:
  x_degree = 0
elif x_position < 602:
  x_degree = 3
elif x_position < 692:
  x_degree = 5
elif x_position < 783:
  x_degree = 8
elif x_position < 879:
  x_degree = 10
else:
  x_degree = 11

# y

if   y_position < 123:
  y_degree = 17
elif y_position < 234:
  y_degree = 13
elif y_position < 350:
  y_degree = 9
elif y_position < 470:
  y_degree = 6
elif y_position < 595:
  y_degree = 0
elif y_position < 723:
  y_degree = -6
else:
  y_degree = -7

# debugging now
arm_control.arm_control( x_degree, y_degree, 0.1, 0 )
