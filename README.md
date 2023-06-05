# llm-gpt-sort
New type of sorting algorithm. Use large language model (llm like gpt, chat-gpt or others) to sort collections.

## Algorithm

Simply give a Large Language Model any collectio and ask it to sort it.

## Example

Give GPT a collection of words.

```['playing', 'available', 'home', 'came', 'dame', 'busy', 'winds', 'adaptation', 'named', 'continues', 'lucas', 'connections', 'subscribers', 'administrative', 'glad']```

It returns the results. Results can be compared to the original list that was sorted in a traditional manner.

```
to_sort.sort()
print(f"\nOriginal sorted collection:\n{to_sort}")
print(f"\nLLM sorted collection:\n{sorted_list}")
print(f"\nAre these two list the same? {to_sort == sorted_list}")
```

Results for sorting words:
```
Original sorted collection:
['adaptation', 'administrative', 'available', 'busy', 'came', 'connections', 'continues', 'dame', 'glad', 'home', 'lucas', 'named', 'playing', 'subscribers', 'winds']

LLM sorted collection:
['adaptation', 'administrative', 'available', 'busy', 'came', 'connections', 'continues', 'dame', 'glad', 'home', 'lucas', 'named', 'playing', 'subscribers', 'winds']

Are these two list the same? True
```

Same can be done with numbers:

```
[78, 147, 97, 143, 20, 40, 30, 114, 131, 184, 93, 15, 32, 2, 187, 92, 138, 91, 56, 124, 41, 1, 8, 69, 103, 186, 199, 7, 173, 27, 102, 3, 192, 141, 4, 165, 172, 177, 35, 31, 17, 60, 59, 164, 145, 154, 166, 127, 66, 194, 117, 86, 125, 144, 22, 85, 157, 44, 65, 134, 169, 113, 61, 126, 128, 108, 28, 149, 68, 190, 55, 64, 24, 160, 58, 196, 110, 96, 88, 6, 74, 83, 193, 188, 150, 46, 43, 57, 107, 129, 167, 71, 77, 163, 51, 185, 106, 76, 158, 75, 111, 48, 179, 38, 176, 33, 105, 70, 153, 104, 98, 54, 52, 115, 175, 84, 130, 10, 183, 161, 195, 140, 142, 47, 80, 118, 146, 39, 197, 135, 19, 12, 116, 95, 87, 137, 81, 0, 168, 171, 36, 156, 189, 9, 13, 73, 99, 49, 180, 11, 152, 26, 53, 23, 63, 62, 120, 79, 18, 14, 191, 72, 133, 119, 151, 159, 148, 122, 100, 21, 109, 182, 181, 16, 89, 178, 5, 136, 170, 132, 34, 155, 42, 25, 198, 45, 123, 174, 37, 112, 90, 139, 101, 162, 94, 50, 67, 29, 82, 121]
```

```
Original sorted collection:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]

LLM sorted collection:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]

Are these two list the same? True
```



## Performance

GPT answer:

During inference, the time and space complexity of the GPT (Generative Pre-trained Transformer) model for an input of size n can be approximated as follows:

Time Complexity: The time complexity of GPT during inference can be expressed as O(L * n^2), where L is the number of layers in the model and n is the number of tokens in the input sequence. Each layer of the GPT model involves self-attention and feed-forward computations. The self-attention operation has a time complexity of O(n^2), as it requires pairwise comparisons between all tokens in the input sequence. The feed-forward network has a time complexity of O(n), as it operates on each token independently.

Since the GPT model consists of L layers, the time complexity becomes O(L * n^2), considering the computations performed at each layer.

Space Complexity: The space complexity of the GPT model during inference is primarily determined by the model's parameters. The space complexity can be approximated as O(M), where M represents the total number of parameters in the model. These parameters include the weights and biases of the self-attention layers, feed-forward networks, and other components of the model.

In addition to the model parameters, there is also some memory overhead required for intermediate computations during the inference process. However, this overhead is typically negligible compared to the parameter space complexity.

It's important to note that the mentioned time and space complexities are approximations and can vary depending on the specific implementation, optimizations, and batch size used during inference.
