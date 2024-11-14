class GoBackNARQ:
    def __init__(self, window_size, total_frames):
        self.window_size = window_size  # Size of the sender window
        self.total_frames = total_frames  # Total number of frames to send
        self.sent_frames = []  # Track sent frames
        self.acknowledged_frames = set()  # Track acknowledged frames
        self.current_frame = 0  # Frame index to be sent next
        self.base = 0  # Oldest frame that has been sent but not yet acknowledged

    def send_frame(self, frame_id):
        """Send a frame and store it in sent_frames list."""
        print(f"Sending frame {frame_id}")
        self.sent_frames.append(frame_id)

    def receive_acknowledgement(self, ack_id):
        """Receive an acknowledgement and update base."""
        if ack_id not in self.acknowledged_frames:
            print(f"Received acknowledgement for frame {ack_id}")
            self.acknowledged_frames.add(ack_id)

        # Slide the window if the base frame is acknowledged
        while self.base in self.acknowledged_frames:
            print(f"Sliding window: base frame {self.base} acknowledged.")
            self.base += 1

    def simulate_transmission(self):
        """Simulate the transmission of frames using Go-Back-N ARQ."""
        while self.base < self.total_frames:
            # Send frames within the window
            while self.current_frame < self.base + self.window_size and self.current_frame < self.total_frames:
                self.send_frame(self.current_frame)
                self.current_frame += 1

            # Simulate receiving acknowledgements for all frames in window except one (to trigger Go-Back-N)
            if self.base < self.total_frames:
                if (self.base + self.window_size - 1) < self.total_frames:
                    print(f"Simulating loss for frame {self.base + self.window_size - 1}")
                for ack in range(self.base, min(self.base + self.window_size - 1, self.total_frames)):
                    self.receive_acknowledgement(ack)

            # Check if all frames have been acknowledged
            if self.base >= self.total_frames:
                print("All frames successfully transmitted.")
                break
            else:
                # If one frame is lost, Go-Back-N will retransmit from the base frame
                print(f"Timeout: Resending from frame {self.base} onward...")
                self.current_frame = self.base  # Reset current frame to the base

# Example usage
window_size = 4
total_frames = 10
goback_n = GoBackNARQ(window_size, total_frames)
goback_n.simulate_transmission()