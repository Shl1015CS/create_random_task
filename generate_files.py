import os
import random

def generate_random_content(size_in_bytes):
    # 生成随机字节数据
    return os.urandom(size_in_bytes)

def create_file(filename, size_in_bytes):
    with open(filename, 'wb') as f:
        content = generate_random_content(size_in_bytes)
        f.write(content)

def main():
    # 创建输出目录
    output_dir = "generated_files"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 定义文件大小和数量
    file_specs = [
        {"size": 20 * 1024 * 1024, "count": 1000},  # 20MB * 1000个
        {"size": 10 * 1024 * 1024, "count": 1000},  # 10MB * 1000个
        {"size": 1 * 1024 * 1024, "count": 1000},   # 1MB * 1000个
        {"size": 500 * 1024, "count": 7000},        # 500KB * 7000个
    ]

    total_files = 0
    
    # 生成文件
    for spec in file_specs:
        size = spec["size"]
        count = spec["count"]
        
        for i in range(count):
            filename = os.path.join(output_dir, f"file_{size}_{i}.dat")
            print(f"正在生成文件 {filename}")
            create_file(filename, size)
            total_files += 1
            
            # 每生成100个文件显示一次进度
            if total_files % 100 == 0:
                print(f"已生成 {total_files} 个文件")

    print(f"完成！共生成了 {total_files} 个文件")

if __name__ == "__main__":
    main() 