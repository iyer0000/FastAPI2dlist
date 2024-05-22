from concurrent.futures import ProcessPoolExecutor
def get_output(n):
    return sum(n)

input_list = [[1,2],[3,4]]
output_list = []

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as pool:
        output_list.extend(pool.map(get_output, input_list))

if len(output_list)>0:
    print(output_list)