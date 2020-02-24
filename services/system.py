import psutil


async def gather_info():
    info = dict()

    info['cpu_percent'] = psutil.cpu_percent(interval=1)
    info['load_avg'] = psutil.getloadavg()

    info['memory'] = psutil.virtual_memory()
    info['swap'] = psutil.swap_memory()

    info['disk'] = psutil.disk_usage('/')

    return info
