import os
import sys
from pprint import pprint

import ecal
import ecal.measurement.hdf5
from ximea import xiapi


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
    channel_type = meas.get_channel_type(
        channel_name)  # sensor_msgs/msg/PointCloud2
    # https://eclipse-ecal.github.io/ecal/_api/structeCAL_1_1eh5_1_1SEntryInfo.html#_CPPv4N4eCAL3eh510SEntryInfoE
    entries_info = meas.get_entries_info(channel_name)
    data_size = meas.get_entry_data_size(entry_id=entries_info[0]['id'])
    data = meas.get_entry_data(entry_id=entries_info[0]['id'])

    pprint(channel_type)
    pprint(data_size)


if __name__ == "__main__":
    main()