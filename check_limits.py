def check_limit(value, low, high, name):
    if not (low <= value <= high):
        print(f'{name} is out of range!')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    checks = [
        (temperature, 0, 45, 'Temperature'),
        (soc, 20, 80, 'State of Charge'),
        (charge_rate, 0, 0.8, 'Charge rate')
    ]
    return all(check_limit(val, low, high, name) for val, low, high, name in checks)

if __name__ == '__main__':
    assert battery_is_ok(4, 21, 1.0) is False
    assert battery_is_ok(50, 85, 0) is False
    assert battery_is_ok(25, 70, 0.5) is True
