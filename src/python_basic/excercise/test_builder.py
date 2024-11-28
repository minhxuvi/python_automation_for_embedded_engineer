class TestBuilder:
    def __init__(self, os, compiler, core, plugin_dir, build_dir):
        pass

    def build(self):
        """run make command"""
        "make os=... compiler=..."
        print("build")


def main():
    test_builder = TestBuilder("linux", "gcc", "x86_64", "./plugins", "./build")
    test_builder.build()


if __name__ == "__main__":

    main()
