import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LaserScanFilterPublisher(Node):

    def __init__(self):
        super().__init__('laser_scan_filter_publisher')

        
        self.scan_subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

      
        self.filtered_scan_publisher = self.create_publisher(
            LaserScan,
            '/filtered_scan',
            10)

       
        self.min_angle = 0.0  
        self.max_angle = 2.094 

    def scan_callback(self, msg):
      
        filtered_ranges = []
        filtered_intensities = []
        for i, angle in enumerate(msg.ranges):
            angle = i * msg.angle_increment  
            if self.min_angle <= angle <= self.max_angle:
                filtered_ranges.append(msg.ranges[i])
                filtered_intensities.append(msg.intensities[i])

       
        filtered_scan = LaserScan()
        filtered_scan.header = msg.header
        filtered_scan.angle_min = self.min_angle
        filtered_scan.angle_max = self.max_angle
        filtered_scan.angle_increment = msg.angle_increment
        filtered_scan.range_min = msg.range_min
        filtered_scan.range_max = msg.range_max
        filtered_scan.ranges = filtered_ranges
        filtered_scan.intensities = filtered_intensities

        
        self.filtered_scan_publisher.publish(filtered_scan)

def main(args=None):
    rclpy.init(args=args)

    laser_scan_filter_publisher = LaserScanFilterPublisher()

    rclpy.spin(laser_scan_filter_publisher)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
