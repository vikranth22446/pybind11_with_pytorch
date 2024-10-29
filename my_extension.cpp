#include <torch/extension.h>

torch::Tensor my_custom_function(torch::Tensor input) {
    return input * 2;
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("my_custom_function", &my_custom_function, "A function that doubles each element");
}


// Write a test for the custom function