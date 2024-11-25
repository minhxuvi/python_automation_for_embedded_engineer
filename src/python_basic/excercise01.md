Viết một class TestBuilder()
Có các properties: os, compiler, core, test_suite, platform
method build() return đường dẫn tới binary output.

B1: clone ipcf, ipcf-tests
B2: viết python script test_builders.py #tham khảo trong ipcf-tools/itf/components/tests_builder.py
gợi ý: Hardcode biến môi trường

CROSS_COMPILE =
NXP_RTOS =
cur_env = os.environ
cur_env[CROSS_COMPILE] =
cmd = f"make .... platform {platform}"
subprocess.run(cmd, env = cur_env) # tham khảo run_in_cygwin trong ipcf-tools/itf/components/tests_base.py
