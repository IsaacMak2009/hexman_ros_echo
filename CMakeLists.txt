cmake_minimum_required(VERSION 3.0.2)
project(xpkg_demo)

set(X_ROS_VERSION $ENV{ROS_VERSION})
message(STATUS "Your ROS version is ROS${X_ROS_VERSION}")

add_definitions(-DX_ROS_VERSION=${X_ROS_VERSION}) 

if (${X_ROS_VERSION} STREQUAL "1")

    find_package(catkin REQUIRED COMPONENTS
      roscpp rospy
    )

    catkin_package(

    )

    include_directories(
    # include
      ${catkin_INCLUDE_DIRS}
    )

elseif (${X_ROS_VERSION} STREQUAL "2")

    cmake_minimum_required(VERSION 3.8)
    
    if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
        add_compile_options(-Wall -Wextra -Wpedantic)
    endif()

    # find dependencies
    find_package(ament_cmake REQUIRED)
    find_package(rclcpp REQUIRED)

    if(BUILD_TESTING)
        find_package(ament_lint_auto REQUIRED)
        ament_lint_auto_find_test_dependencies()
    endif()

    ament_package()

    install(
        DIRECTORY demo_vehicle/ROS2
        DESTINATION share/${PROJECT_NAME}/demo_vehicle
    )

else ()
    message(FATAL_ERROR "Unknown ROS version, please install the ros_environment package")
endif ()
