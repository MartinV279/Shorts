import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set if dist.project_name[0] != "-"]
call("pip install --upgrade " + ' '.join(packages), shell=True)
