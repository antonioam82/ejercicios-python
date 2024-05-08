from robot_control_class import RobotControl
import argparse

rc = RobotControl(robot_name="summit")

def main():
    parser = argparse.ArgumentParser(prog="ROBOT-CONTROL",conflict_handler='resolve',
                                     description="Mnipulate Summit Robot")
    parser.add_argument('-mv','--move',required=True,choices=["straight","turn"],type=str,help="...")
    parser.add_argument('-dir','--direction',required=True,choices=["up","back"],type=str,help="...")
    parser.add_argument('-tm','--time',required=True,type=int,help="Time in seconds")
    parser.add_argument('-spd','--speed',required=True,type=float,help="Distance")

    args = parser.parse_args()

    if args.move == "straight":
        movements = {"up":"forward","back":"backward"}
        rc.move_straight_time(movements[args.direction],args.speed,args.time)
    else:
        movements = {"up":"clockwise","back":"counter-clockwise"}
        rc.turn(movements[args.direction],args.speed,args.time)

if __name__=='__main__':
    main()
