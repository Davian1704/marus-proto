# Introduction
This repository contains the [Protocol Buffers](https://developers.google.com/protocol-buffers) 
definitions used for communication with the LABUST marine simulator.

# Contributing
You should add or edit the files in the `protos` directory of the `main` branch. 
Source files for used programming languages (e.g., C#, Python) will be automatically 
generated in their corresponding orphan branches. You can use the generated code in 
your project by checking out the corresponding branch. This can be done manually or 
by adding this branch via [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) 
into your versioning.

## Naming convention
Please follow the naming conventions already in the proto files, i.e., `camelCase` for
variable naming and uppercase first letter for type (e.g. ImuStream).

## Aligning files with ROS
Used ROS message packets correspond to individual `proto` files (e.g., `std_msgs` are in `std.proto`). 
When extending add any new ROS based messages to their logical `proto` file. 

### Streaming files
To allow automatic streaming of individual ROS topics, all messages used for exchange have 
a streaming counter part. E.g, for `Imu` there is an `ImuStream` message which containes the `Imu` 
message itself coupled with the corresponding `address` variable indicating the ROS topic.