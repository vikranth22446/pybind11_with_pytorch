import os
from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

# Use ccache for C++ compilation
os.environ["USE_CCACHE"] = "1"

setup(
    name='my_extension',
    ext_modules=[
        CppExtension(
            'my_extension',
            ['my_extension.cpp'],
            extra_compile_args=['-g', '-O2'],  # Enable debug info and optimization
        ),
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
