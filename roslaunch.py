import roslaunch

package = 'rviz'
executable = 'rviz'
node = roslaunch.core.Node(package, executable)

launch = roslaunch.scriptapi.ROSLaunch()
launch.start()

process = launch.launch(node)
print process.is_alive()
process.stop()
