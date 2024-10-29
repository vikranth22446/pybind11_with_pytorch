import torch
import my_extension

input_tensor = torch.tensor([1.0, 2.0, 3.0])
result = my_extension.my_custom_function(input_tensor)
print("Result:", result)  # Should output tensor([2.0, 4.0, 6.0])
