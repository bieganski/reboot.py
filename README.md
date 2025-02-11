# Usage

### Immediate reboot
```bash
python3 reboot.py
```

### Postponed reboot (server mode)

```bash
python3 reboot.py server
```

`server mode` waits for `SIGUSR1`, then reboot. Assuming it's running as a PID 123, trigger reboot by following command:

```bash
builtin kill -SIGUSR1 123
```

# Supported platforms

* `x86_64`
* `aarch64`
* `arm32`
* `riscv64`