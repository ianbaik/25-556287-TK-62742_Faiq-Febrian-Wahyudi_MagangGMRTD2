import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class gambarPersegi(Node):

    def __init__(self):
        super().__init__('gambar_persegi')
        self.cmd_vel_pub = self.create_publisher(Twist,'/turtle1/cmd_vel',10)

        # Timer dipanggil setiap 0.1 detik
        self.timer = self.create_timer(0.1,self.gambar_persegi)
        self.waktu = 0
        self.sisi = 0
        self.get_logger().info('Menggambar persegi dimulai')

    def gambar_persegi(self):
        msg = Twist()
        # 20 kali × 0.1 detik = 2 detik
        # Turtle maju selama 2 detik
        if self.waktu < 20:
            msg.linear.x = 2.0
            msg.angular.z = 0.0

        # 10 kali × 0.1 detik = 1 detik
        # 2 detik + 1 detik = 3 detik
        # Turtle berputar sekitar 90 derajat
        elif self.waktu < 30:
            msg.linear.x = 0.0
            msg.angular.z = 1.57 #dalam radian, 90 derajat = 1.57 radian

        else:
            self.waktu = 0
            self.sisi += 1

        self.cmd_vel_pub.publish(msg)
        self.waktu += 1


def main(args=None):
    rclpy.init(args=args)
    node = gambarPersegi()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()