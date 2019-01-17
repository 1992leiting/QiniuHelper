import configparser

'''
cp类继承configparser
configparser源码中的optionxform方法会强制转换小写
这里重写这个方法，取消小写转换
'''


class configParserWithoutForcedLowercase(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


def get_dict_from_ini(ini_file, section_name):
    dict_rt = {}
    conf = configParserWithoutForcedLowercase()
    conf.read(ini_file)
    keys = list(conf[section_name].keys())
    vals = list(conf[section_name].values())
    for i in range(len(keys)):
        dict_rt[keys[i]] = vals[i]
    return dict_rt


def write_key_val(ini_file, section_name, key, val):
    conf = configParserWithoutForcedLowercase()
    conf.read(ini_file)
    conf.set(section_name, key, val)
    conf.write(open(ini_file, 'w'))


def add_section(ini_file, section_name):
    conf = configParserWithoutForcedLowercase()
    conf.read(ini_file)
    conf.add_section(section_name)
    conf.write(open(ini_file), 'w')

