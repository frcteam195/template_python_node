"""
Class definition of the TemplatePythonNode.
"""
from threading import Thread

import rospy

from frc_robot_utilities_py_node.frc_robot_utilities_py import register_for_robot_updates, robot_status
from frc_robot_utilities_py_node.RobotStatusHelperPy import RobotMode

class TemplatePythonNode():
    """
    TemplatePythonNode
    """

    def __init__(self) -> None:
        register_for_robot_updates()

        loop_thread = Thread(target=self.loop)
        loop_thread.start()

        rospy.spin()

        loop_thread.join(5)

    def loop(self) -> None:
        """
        Periodic function for the TemplatePythonNode.
        """
        rate = rospy.Rate(20)

        # Put your code in the appropriate sections in this if statement/while loop.
        while not rospy.is_shutdown():
            if robot_status.get_mode() == RobotMode.AUTONOMOUS:
                pass
            elif robot_status.get_mode() == RobotMode.TELEOP:
                pass
            elif robot_status.get_mode() == RobotMode.DISABLED:
                pass
            elif robot_status.get_mode() == RobotMode.TEST:
                pass

            rate.sleep()
