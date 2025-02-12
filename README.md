# Usage

### Immediate reboot
```bash
python3 reboot.py
```

### Postponed reboot (server mode)

```bash
python3 reboot.py server
```

`server mode` waits infitely for a ping, then reboot. The ping can be either an Unix signal or a network connection.

##### Unix signal

Assuming it's running as a PID 123, trigger reboot by following command:

```bash
builtin kill -SIGUSR1 123
```

##### Network

Assuming it's IP is 192.168.0.2, run following command from a different process (or machine from same network)

```bash
wget 192.168.0.2:1234
```

# Supported platforms

* `x86_64`
* `aarch64`
* `arm32`
* `riscv64`