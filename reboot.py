#!/usr/bin/env python3

import ctypes
from enum import Enum
import platform
from argparse import ArgumentParser
import signal
import os
import sys
from socket import *

libc = ctypes.CDLL(None)

class CPU_Arch(Enum):
    x86_64 = "x86_64"
    riscv64 = "riscv64"
    arm = "arm"
    aarch64 = "aarch64"

def system_get_cpu_arch() -> CPU_Arch:
    machine = platform.machine()
    return CPU_Arch(machine)

reboot_syscall_nr = {
    CPU_Arch.x86_64: 169,
    CPU_Arch.riscv64: 142,
    CPU_Arch.aarch64: 142,
}

def reboot():
    try:
        print("reboot!")
        sys.stdout.flush()
    except:
        pass # may fail, if process is disowned

    libc.syscall(
        reboot_syscall_nr[system_get_cpu_arch()],
        0xfee1dead,
        0x28121969,
        0x01234567,
        None
    )

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("server_mode", nargs="?", choices=["server"])
    
    if parser.parse_args().server_mode:
        port = 1234

        print(f"Running in server mode: To reboot either 1) send SIGUSR1 to PID {os.getpid()} or 2) connect to port {port}")

        signal.signal(signal.SIGUSR1, lambda *_: reboot())
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(("0.0.0.0", port))
        s.listen(1)
        conn, addr = s.accept()
        conn.close()
        reboot()
    else:
        reboot()