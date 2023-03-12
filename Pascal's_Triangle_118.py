class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nested_array = [[1]]  # the minimum output

        for i in range(2, numRows+1):
            array = []  # new arrays
            # to make two direct above number for corner values
            array_with_dummy_value = [0] + nested_array[-1] + [0]

            for j in range(len(nested_array[-1])+1):
                # new value from direct two above numbers
                value = array_with_dummy_value[j] + array_with_dummy_value[j+1]
                array.append(value)
            nested_array.append(array)
        return nested_array
