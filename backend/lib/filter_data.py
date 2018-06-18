def filter_country(confs, arg):
    country_list = arg.split(',')

    return [conf for conf in confs if conf.get('country') in country_list]


def filter_bbox(confs, arg):
    coords = arg.split(',')

    if len(coords) != 4:
        raise ValueError('Provide 4 coordinates seperated by \',\'')
    try:
        x1 = float(coords[0])
        y1 = float(coords[1])
        x2 = float(coords[2])
        y2 = float(coords[3])
    except ValueError:
        raise ValueError('Could not parse coords')

    def filter_func(conf):
        x = float(conf['coords']['lon'])
        y = float(conf['coords']['lat'])
        return (x1 <= x <= x2 or x2 <= x <= x1) and \
               (y1 <= y <= y2 or y2 <= y <= y1)

    return [conf for conf in confs if filter_func(conf)]