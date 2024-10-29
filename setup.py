import os
from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

# Use ccache for C++ compilation
os.environ["USE_CCACHE"] = "1"

setup(
    name='slo_extension',
    ext_modules=[
        CppExtension(
            'slo_extension',
            ['slo_extension.cpp'],
            extra_compile_args=['-g', '-O2'],  # Enable debug info and optimization
        ),
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
