import os
import sys
from pprint import pprint

import ecal
import ecal.measurement.hdf5
import ecal.measurement.measurement
from ximea import xiapi

import rclpy
from sensor_msgs.msg import PointCloud2


# deserialize an ecal measurement having ROS2 topics and get the PCL data from sensor_msgs/msg/PointCloud2 topics.
def get_pcl_data(meas, channel_name):
    channel_type = meas.get_channel_type(
        channel_name)  # sensor_msgs/msg/PointCloud2
    print(channel_type)
    entris_info = meas.get_entries_info(channel_name)
    data_size = meas.get_entry_data_size(entry_id=entris_info[0]['id'])

    # deserialize the entry data
    pc = PointCloud2()  # point cloud data
    pc.data = meas.get_entry_data(entry_id=entris_info[0]['id'])
    pprint(pc)

    return pc


def main():
    meas_path = "data/test/2022-11-30_15-17-43.373_measurement"

    meas = ecal.measurement.hdf5.Meas(meas_path)
    if not meas.is_ok():
        sys.exit(f'Error: cannot open {meas_path}')

    pprint(meas.get_channel_names())

    # image
    cam_context_path = os.path.join(meas_path, "cam_context.bin")
    out_path_rgb = os.path.join(meas_path, "rgb/")
    out_path_raw = os.path.join(meas_path, "raw/")

    # get PCL data (rt/livox/lidar, rt/livox/imu)
    channel_name = 'rt/livox/lidar'
    # https://eclipse-ecal.github.io/ecal/_api/structeCAL_1_1eh5_1_1SEntryInfo.html#_CPPv4N4eCAL3eh510SEntryInfoE
    pcd = get_pcl_data(meas, channel_name)


if __name__ == "__main__":
    main()