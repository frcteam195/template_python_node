import jinja2
import yaml
import pathlib
from typing import List

def render_jinja(arg_src_template, arg_src_file):
    node_name = pathlib.Path(__file__).parent.parent.name
    robot_name = ""

    for item in pathlib.Path.cwd().parent.iterdir():
        if item.is_dir():
            if item.name.count("_Robot") > 0:
                robot_name = str(item.resolve())

    if robot_name == "":
        raise Exception("Unable to determine robot project folder")

    with open(robot_name + '/config/' + node_name + '.yaml', 'r') as stream:
        try:
            yaml_obj = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("Error loading yaml file")
            raise exc


    type_map = {
        None : "rclpy.Parameter.Type.NOT_SET",
        bool : "rclpy.Parameter.Type.BOOL",
        int : "rclpy.Parameter.Type.INTEGER",
        float : "rclpy.Parameter.Type.DOUBLE",
        str : "rclpy.Parameter.Type.STRING",
        bytes : "rclpy.Parameter.Type.BYTE_ARRAY",
        6 : "rclpy.Parameter.Type.BOOL_ARRAY",
        7 : "rclpy.Parameter.Type.INTEGER_ARRAY",
        8 : "rclpy.Parameter.Type.DOUBLE_ARRAY",
        9 : "rclpy.Parameter.Type.STRING_ARRAY",
    }

    params = {}

    for (k, v) in yaml_obj[node_name]["ros__parameters"].items():
        if type(v) is list:
            if all(isinstance(n, bool) for n in v):
                params[k] = type_map[6]
            elif all(isinstance(n, int) for n in v):
                params[k] = type_map[7]
            elif all(isinstance(n, float) for n in v):
                params[k] = type_map[8]
            elif any(isinstance(n, float) for n in v):
                params[k] = type_map[8]
            elif all(isinstance(n, str) for n in v):
                params[k] = type_map[9]
            else:
                params[k] = type_map[None]
            pass
        else:
            params[k] = type_map[type(v)]


    # # Generate unit test template
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('/'), trim_blocks=True)
    src_template = env.get_template(arg_src_template)
    src_result = src_template.render(params=params, node_name=node_name)
    f = open(arg_src_file, "w")
    f.write(src_result)
    f.close()