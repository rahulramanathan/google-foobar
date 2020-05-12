def solution(l):
    # Your code here
    x = [map(int,version.split('.')) for version in l]
    y = ['.'.join(map(str,version))  for version in sorted(x)]
    return y

# version_list1 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
# version_list2 = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]

# print solution(version_list1)
# print solution(version_list2)