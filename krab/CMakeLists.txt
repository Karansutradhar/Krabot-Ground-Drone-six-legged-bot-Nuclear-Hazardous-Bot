cmake_minimum_required(VERSION 2.8.3)

project(krab)

find_package(catkin REQUIRED COMPONENTS
  urdf
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
