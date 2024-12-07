import logging
import matplotlib.pyplot as plt
import numpy as np

# The class for data loader.
class log_plotter:
    def __init__(self, filename):
        self.filename = filename
        self.cwnd = []
        self.ssthresh = []
        self.__load_file()

    def __load_file(self):
        with open (self.filename,'r') as file:
            log_lines = file.readlines()
            if self.filename == "data/tcp_metrics_bbr_5drop.log":
                index = 2
                while (index < len(log_lines)):
                    log_line = log_lines[index]
                    index += 3
                    cwnd = log_line.split("cwnd:")[1].split()[0]
                    ssthresh = log_line.split("ssthresh:")[1].split()[0]
                    self.cwnd.append(cwnd)
                    self.cwnd = list(map(int, self.cwnd))
                    if ssthresh == "56587":
                        continue
                    self.ssthresh.append(ssthresh)
                    self.ssthresh = list(map(int, self.ssthresh))

            elif self.filename == "data/tcp_metrics_bbr_10drop.log":
                index = 2
                while (index < len(log_lines)):
                    log_line = log_lines[index]
                    index += 3
                    cwnd = log_line.split("cwnd:")[1].split()[0]
                    ssthresh = log_line.split("ssthresh:")[1].split()[0]
                    self.cwnd.append(cwnd)
                    self.cwnd = list(map(int, self.cwnd))
                    if ssthresh == "56587":
                        continue
                    self.ssthresh.append(ssthresh)
                    self.ssthresh = list(map(int, self.ssthresh))

            elif self.filename == "data/tcp_metrics_bbr.log":
                index = 2
                while (index < len(log_lines)):
                    log_line = log_lines[index]
                    index += 3
                    cwnd = log_line.split("cwnd:")[1].split()[0]
                    ssthresh = log_line.split("ssthresh:")[1].split()[0]
                    self.cwnd.append(cwnd)
                    self.cwnd = list(map(int, self.cwnd))
                    if ssthresh == "56587":
                        continue
                    self.ssthresh.append(ssthresh)
                    self.ssthresh = list(map(int, self.ssthresh))

            elif self.filename == "data/tcp_metrics_cubic_5drop.log":
                index = 2
                while (index < len(log_lines)):
                    log_line = log_lines[index]
                    index += 3
                    cwnd = log_line.split("cwnd:")[1].split()[0]
                    ssthresh = log_line.split("ssthresh:")[1].split()[0]
                    self.cwnd.append(cwnd)
                    self.cwnd = list(map(int, self.cwnd))
                    if ssthresh == "56587":
                        continue
                    self.ssthresh.append(ssthresh)
                    self.ssthresh = list(map(int, self.ssthresh))

            elif self.filename == "data/tcp_metrics_cubic_10drop.log":
                index = 1
                while (index < len(log_lines)):
                    log_line = log_lines[index]
                    index += 3
                    cwnd = log_line.split("cwnd:")[1].split()[0]
                    ssthresh = log_line.split("ssthresh:")[1].split()[0]
                    self.cwnd.append(cwnd)
                    self.cwnd = list(map(int, self.cwnd))
                    if ssthresh == "56587":
                        continue
                    self.ssthresh.append(ssthresh)
                    self.ssthresh = list(map(int, self.ssthresh))

            elif self.filename == "data/tcp_metrics_cubic.log":
                index = 2
                while (index < len(log_lines)):
                    log_line = log_lines[index]
                    index += 3
                    cwnd = log_line.split("cwnd:")[1].split()[0]
                    ssthresh = log_line.split("ssthresh:")[1].split()[0]
                    self.cwnd.append(cwnd)
                    self.cwnd = list(map(int, self.cwnd))
                    if ssthresh == "56587":
                        continue
                    self.ssthresh.append(ssthresh)
                    self.ssthresh = list(map(int, self.ssthresh))

            else:
                index = 1
                while (index < len(log_lines)):
                    log_line = log_lines[index]
                    index += 2
                    cwnd = log_line.split("cwnd:")[1].split()[0]
                    self.cwnd.append(cwnd)
                    self.cwnd = list(map(int, self.cwnd))

        return

# Get the data ready.
my_plotter_cubic = log_plotter("data/tcp_metrics_cubic.log")
cubic_cwnd = my_plotter_cubic.cwnd
cubic_ssthresh = my_plotter_cubic.ssthresh

my_plotter_BBR = log_plotter("data/tcp_metrics_bbr.log")
BBR_cwnd = my_plotter_BBR.cwnd
BBR_ssthresh = my_plotter_BBR.ssthresh

my_plotter_cubic_5drop = log_plotter("data/tcp_metrics_cubic_5drop.log")
cubic_cwnd_5drop = my_plotter_cubic_5drop.cwnd
cubic_ssthresh_5drop = my_plotter_cubic_5drop.ssthresh

my_plotter_BBR_5drop = log_plotter("data/tcp_metrics_bbr_5drop.log")
BBR_cwnd_5drop = my_plotter_BBR_5drop.cwnd
BBR_ssthresh_5drop = my_plotter_BBR_5drop.ssthresh

my_plotter_cubic_10drop = log_plotter("data/tcp_metrics_cubic_10drop.log")
cubic_cwnd_10drop = my_plotter_cubic_10drop.cwnd
cubic_ssthresh_10drop = my_plotter_cubic_10drop.ssthresh

my_plotter_BBR_10drop = log_plotter("data/tcp_metrics_bbr_10drop.log")
BBR_cwnd_10drop = my_plotter_BBR_10drop.cwnd
BBR_ssthresh_10drop = my_plotter_BBR_10drop.ssthresh

my_plotter_video_cubic = log_plotter("data/video_metrics_cubic.log")
video_cubic_cwnd = my_plotter_video_cubic.cwnd

my_plotter_video_cubic_5drop = log_plotter("data/video_metrics_cubic_5drop.log")
video_cubic_cwnd_5drop = my_plotter_video_cubic_5drop.cwnd

my_plotter_video_cubic_10drop = log_plotter("data/video_metrics_cubic_10drop.log")
video_cubic_cwnd_10drop = my_plotter_video_cubic_10drop.cwnd

my_plotter_video_BBR = log_plotter("data/video_metrics_BBR.log")
video_BBR_cwnd = my_plotter_video_BBR.cwnd

my_plotter_video_BBR_5drop = log_plotter("data/video_metrics_BBR_5drop.log")
video_BBR_cwnd_5drop = my_plotter_video_BBR_5drop.cwnd

my_plotter_video_BBR_10drop = log_plotter("data/video_metrics_BBR_10drop.log")
video_BBR_cwnd_10drop = my_plotter_video_BBR_10drop.cwnd

# Plot for iperf3 cwnd cubic and bbr.
plt.figure()
length = min(len(BBR_cwnd),len(cubic_cwnd))
time_steps = np.array(range(length)) * 10
plt.plot(time_steps, BBR_cwnd[:length], label = "BBR")
plt.plot(time_steps, cubic_cwnd[:length], label = "Cubic")
plt.axvline(x=190, color='red', linestyle='--', linewidth=1, label="Cubic Slow Start|AIMD")
plt.axvline(x=540, color='green', linestyle='--', linewidth=1, label="BBR Slow Start|AIMD")

plt.xlabel("Time/ms")
plt.ylabel("CWND Value")
plt.title("CWND Growth Over Time")
plt.legend()

plt.savefig("figure/cwnd")

# Plot for iperf3 ssthresh.
plt.figure()

length = min(len(BBR_ssthresh),len(cubic_ssthresh))
time_steps = np.array(range(length)) * 10
plt.plot(time_steps, BBR_ssthresh[:length], label = "BBR")
plt.plot(time_steps, cubic_ssthresh[:length], label = "Cubic")

plt.xlabel("Time/ms")
plt.ylabel("ssthresh")
plt.title("ssthresh Growth Over Time")
plt.legend()

plt.savefig("figure/ssthresh")

# Plot for iperf3 cubic packet loss. 
plt.figure()

length = min(len(cubic_cwnd_5drop),len(cubic_cwnd_10drop),len(cubic_cwnd))
time_steps = np.array(range(length)) * 10
plt.plot(time_steps, cubic_cwnd[:length], label = "no drop")
plt.plot(time_steps, cubic_cwnd_5drop[:length], label = "0.005%")
plt.plot(time_steps, cubic_cwnd_10drop[:length], label = "0.01%")

plt.xlabel("Time/ms")
plt.ylabel("CWND Value")
plt.title("CWND Growth Over Time")
plt.legend()

plt.savefig("figure/cubic_cwnd_drop")

# Plot for iperf3 BBR packet loss.
plt.figure()

length = min(len(BBR_cwnd_5drop),len(BBR_cwnd_10drop),len(BBR_cwnd))
time_steps = np.array(range(length)) * 10
plt.plot(time_steps, BBR_cwnd[:length], label = "no drop")
plt.plot(time_steps, BBR_cwnd_5drop[:length], label = "0.005%")
plt.plot(time_steps, BBR_cwnd_10drop[:length], label = "0.01%")

plt.xlabel("Time/ms")
plt.ylabel("CWND Value")
plt.title("CWND Growth Over Time")
plt.legend()

plt.savefig("figure/BBR_cwnd_drop")

# Plot for video cwnd.
plt.figure()
length = min(len(video_BBR_cwnd),len(video_cubic_cwnd))
time_steps = np.array(range(length)) * 10
plt.plot(time_steps, video_BBR_cwnd[:length], label = "BBR")
plt.plot(time_steps, video_cubic_cwnd[:length], label = "Cubic")
# plt.axvline(x=190, color='red', linestyle='--', linewidth=1, label="Cubic Slow Start|AIMD")
# plt.axvline(x=540, color='green', linestyle='--', linewidth=1, label="BBR Slow Start|AIMD")

plt.xlabel("Time/ms")
plt.ylabel("CWND Value")
plt.title("CWND Growth Over Time")
plt.legend()

plt.savefig("figure/video_cwnd")

# Plot for video cubic drop.

plt.figure()

length = min(len(video_cubic_cwnd_5drop),len(video_cubic_cwnd_10drop),len(video_cubic_cwnd))
time_steps = np.array(range(length)) * 10
plt.plot(time_steps, video_cubic_cwnd[:length], label = "no drop")
plt.plot(time_steps, video_cubic_cwnd_5drop[:length], label = "0.005%")
plt.plot(time_steps, video_cubic_cwnd_10drop[:length], label = "0.01%")

plt.xlabel("Time/ms")
plt.ylabel("CWND Value")
plt.title("CWND Growth Over Time")
plt.legend()

plt.savefig("figure/video_cubic_cwnd_drop")

# Plot for video BBR drop.

plt.figure()

length = min(len(video_BBR_cwnd_5drop),len(video_BBR_cwnd_10drop),len(video_BBR_cwnd))
time_steps = np.array(range(length)) * 10
plt.plot(time_steps, video_BBR_cwnd[:length], label = "no drop")
plt.plot(time_steps, video_BBR_cwnd_5drop[:length], label = "0.005%")
plt.plot(time_steps, video_BBR_cwnd_10drop[:length], label = "0.01%")

plt.xlabel("Time/ms")
plt.ylabel("CWND Value")
plt.title("CWND Growth Over Time")
plt.legend()

plt.savefig("figure/video_BBR_cwnd_drop")

print(128 * 64 * 30 / 1024)