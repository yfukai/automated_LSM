from System.Diagnostics import Process
from System.IO import File

import sys
from os import path
print(sys.version)

basedir=r'C:/Users/LSM User/Documents/fukai/automated_LSM'
conda_env="auto_microscopy"
python_script_name="test_python_file.py"
python_script_path=path.join(basedir,python_script_name)

conda_path=r'C:/Users/LSM User/anaconda3'
activate_script=path.join(conda_path,r'condabin/activate.bat')

assert path.isfile(python_script_path)
assert path.isfile(activate_script)

### https://stackoverflow.com/questions/49082312/activating-conda-environment-from-c-sharp-code-or-what-is-the-differences-betwe
app = Process()
app.StartInfo.WorkingDirectory = basedir
app.StartInfo.FileName = "cmd.exe"
#app.StartInfo.FileName = batchfile_path
app.StartInfo.UseShellExecute = False
app.StartInfo.RedirectStandardInput = True
app.StartInfo.RedirectStandardOutput = True
app.Start()
app.StandardInput.WriteLine("\""+activate_script+"\"")
app.StandardInput.WriteLine("conda activate "+conda_env)
app.StandardInput.WriteLine("python \""+python_script_path+"\"")
app.StandardInput.WriteLine("exit")

while (not app.StandardOutput.EndOfStream):
    line = app.StandardOutput.ReadLine()
    print(line)

app.WaitForExit()
