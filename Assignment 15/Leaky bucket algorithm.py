import time

class LeakyBucket:
    def __init__(self, bucket_size, leak_rate):
        """
        Initialize the Leaky Bucket.
        
        :param bucket_size: Maximum capacity of the bucket (in packets).
        :param leak_rate: Rate at which the bucket leaks (in packets per second).
        """
        self.bucket_size = bucket_size
        self.leak_rate = leak_rate
        self.current_fill = 0
        self.last_check = time.time()

    def add_packet(self, packet_size):
        """
        Add a packet to the bucket.
        
        :param packet_size: Size of the packet (in packets).
        :return: True if the packet was added successfully, False if it was dropped.
        """
        self._leak()

        if packet_size > self.bucket_size:
            print(f"Packet of size {packet_size} is too large to fit in the bucket.")
            return False

        if self.current_fill + packet_size > self.bucket_size:
            print(f"Bucket overflow! Dropping packet of size {packet_size}.")
            return False

        self.current_fill += packet_size
        print(f"Packet of size {packet_size} added. Current fill level: {self.current_fill}/{self.bucket_size}")
        return True

    def _leak(self):
        """
        Leak packets from the bucket according to the leak rate.
        """
        now = time.time()
        time_elapsed = now - self.last_check
        leaked_amount = time_elapsed * self.leak_rate

        if leaked_amount > 0:
            self.current_fill = max(0, self.current_fill - leaked_amount)
            self.last_check = now
            print(f"Leaked {leaked_amount:.2f} packets. Current fill level: {self.current_fill}/{self.bucket_size}")

# Example usage:
bucket_size = 10  # Bucket can hold 10 packets
leak_rate = 1     # Leaking at a rate of 1 packet per second

bucket = LeakyBucket(bucket_size, leak_rate)

# Simulate incoming packets
packets = [2, 3, 1, 4, 8, 1]  # List of packet sizes

for packet in packets:
    time.sleep(0.5)  # Wait for half a second between packets
    bucket.add_packet(packet)
