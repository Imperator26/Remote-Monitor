import psutil


async def gather_info():
    info = dict()

    info['cpu_percent'] = psutil.cpu_percent(interval=1)
    info['load_avg'] = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]

    info['memory'] = psutil.virtual_memory()
    info['swap'] = psutil.swap_memory()

    info['disk'] = psutil.disk_usage('/')


    try:
        info['sensors_temperature'] = psutil.sensors_temperatures()
    except AttributeError:
        pass

    return info
