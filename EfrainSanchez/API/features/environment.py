import yaml

global info_dict
generic_data = yaml.load(open("config/config.yml"))

def before_all(context):
    context.host = generic_data["app"]["host"]
    context.method = generic_data["app"]["method"]
    context.codes = generic_data["codes"]
    #print(context.host)
#before_all(h)