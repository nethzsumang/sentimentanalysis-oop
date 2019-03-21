import sys
import os
from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Packager.PackageInstaller import version_check
from framework.Utilities.Security.Hash.Hash import Hash


s_command = sys.argv[1]
a_params = sys.argv[2 : len(sys.argv)]
s_root_dir = os.path.dirname(os.path.realpath(__file__))

if s_command == "init":
    s_file_path = "config" + os.sep + "app.json"
    a_data = JSONFile(s_file_path, "r").read()

    if a_data is None:
        raise Exception("App config JSON file not found!")

    a_data["ROOT_DIR"] = s_root_dir
    a_data["APP_KEY"] = Hash.generate_key()
    JSONFile(s_file_path, "w").write(a_data)

if s_command == "set":
    s_command_param = a_params[0]
    a_command_param = s_command_param.split("=")
    s_file_path = "config" + os.sep + "app.json"
    a_data = JSONFile(s_file_path, "r").read()
    a_data[a_command_param[0]] = a_command_param[1]
    JSONFile(s_file_path, "w").write(a_data)

if s_command == "edit_dependency":
    s_packagename = a_params[0]
    s_version = a_params[1]
    s_file_path = "config" + os.sep + "packages.json"
    a_data = JSONFile(s_file_path, "r").read()
    a_data["dependencies"][s_packagename] = s_version
    JSONFile(s_file_path, "w").write(a_data)

if s_command == "install":
    version_check()

if s_command == "add_support":
    s_type = a_params[0]
    s_file_path = "config" + os.sep + "packages.json"
    a_data = JSONFile(s_file_path, "r").read()

    if s_type == "image":
        a_data["dependencies"]["opencv-python"] = "1.0.0"
        a_data["dependencies"]["scikit-image"] = "1.0.0"
        a_data["dependencies"]["matplotlib"] = "1.0.0"
    elif s_type == "ann":
        a_data["dependencies"]["tensorflow"] = "1.0.0"
    elif s_type == "charts":
        a_data["dependencies"]["matplotlib"] = "1.0.0"
    elif s_type == "mysql":
        a_data["dependencies"]["mysqlclient"] = "1.0.0"
    else:
        print(s_type + " not supported!")
        exit(0)

    JSONFile(s_file_path, "w").write(a_data)
    version_check()

if s_command == "reset_support":
    s_file_path = "config" + os.sep + "packages.json"
    a_data = JSONFile(s_file_path, "r").read()
    a_data["dependencies"] = {}
    a_data["dependencies"]["var_dump"] = "1.0.0"
    JSONFile(s_file_path, "w").write(a_data)
