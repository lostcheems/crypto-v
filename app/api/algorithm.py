from flask import request, jsonify
from . import api  # 导入 api 蓝图
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import random
from sympy import randprime
from math import gcd

@api.route('/algorithm', methods=['POST'])
def run_algorithm():
    data = request.json
    algorithm = data.get('algorithm')
    custom_data = data.get('custom_data')

    if not algorithm or not custom_data:
        return jsonify({'error': 'Invalid input'}), 400

    steps = []
    if algorithm == 'sorting':
        steps = sorting_algorithm(custom_data)
    elif algorithm == 'hashing':
        steps = hashing_algorithm(custom_data)
    elif algorithm == 'encryption':
        steps = encryption_algorithm(custom_data)
    elif algorithm == 'rsa':
        steps = rsa_algorithm(custom_data)
    else:
        return jsonify({'error': 'Unsupported algorithm'}), 400

    return jsonify({'steps': steps})


def sorting_algorithm(data):
    """
    排序算法，返回每一步的操作、数组状态和颜色。
    """
    try:
        array = list(map(int, data.split(',')))  # 将输入数据转换为整数列表
    except ValueError:
        return [{'action': '错误', 'data': '输入数据无效', 'color': '#ff0000'}]  # 红色表示错误

    steps = [{'action': '初始化数组', 'data': str(array), 'color': '#e74c3c'}]  # 红色表示初始化
    n = len(array)

    # 冒泡排序逻辑
    for i in range(n):
        for j in range(0, n - i - 1):
            # 添加比较步骤
            steps.append({'action': f'比较元素', 'data': f'索引 {j} 和 {j + 1}', 'color': '#2ecc71'})  # 绿色表示比较
            if array[j] > array[j + 1]:
                # 交换元素
                array[j], array[j + 1] = array[j + 1], array[j]
                # 添加交换步骤
                steps.append({'action': f'交换元素', 'data': f'索引 {j} 和 {j + 1}', 'color': '#2ecc71'})  # 绿色表示交换
                # 添加交换后的数组状态
                steps.append({'action': f'交换后数组', 'data': str(array), 'color': '#f1c40f'})  # 黄色表示交换后数组

    # 添加排序完成步骤
    steps.append({'action': '排序完成', 'data': str(array), 'color': '#4a90e2'})  # 蓝色表示完成
    return steps


def hashing_algorithm(data):
    import hashlib
    steps = [{'action': '输入字符串', 'data': data}]
    encoded = data.encode('utf-8')
    steps.append({'action': '编码为 UTF-8', 'data': str(encoded)})
    hash_object = hashlib.sha256(encoded)
    hash_hex = hash_object.hexdigest()
    steps.append({'action': '生成哈希', 'data': hash_hex})
    return steps


def encryption_algorithm(data):
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    steps = [{'action': '生成密钥', 'data': key.decode()}]
    encrypted_text = cipher_suite.encrypt(data.encode())
    steps.append({'action': '加密数据', 'data': encrypted_text.decode()})
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    steps.append({'action': '解密数据', 'data': decrypted_text})
    return steps

def rsa_algorithm(data):
    """
    优化后的RSA算法可视化步骤，修正模块连接关系
    """
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        else:
            g, x, y = extended_gcd(b, a % b)
            return g, y, x - (a // b) * y

    steps = []
    p = randprime(2**512, 2**513)
    q = randprime(2**512, 2**513)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    if gcd(e, phi_n) != 1:
        for candidate in range(3, phi_n, 2):
            if gcd(candidate, phi_n) == 1:
                e = candidate
                break
    _, x, _ = extended_gcd(e, phi_n)
    d = x % phi_n

    # Convert input data to integer
    try:
        data_bytes = data.encode('utf-8')
        data_int = int.from_bytes(data_bytes, byteorder='big')
        block_size = (n.bit_length() - 1) // 8  # Calculate maximum block size
    except Exception as e:
        return [{'action': '错误', 'data': f'数据处理失败: {str(e)}', 'color': '#ff0000'}]

    # 1. 生成素数阶段（绿色父模块，红色子模块）
    steps.append({'action': '生成大素数', 'data': '随机生成p和q', 'color': '#2ecc71', 'id': 'gen_primes'})
    steps.append({'action': '生成的素数 p', 'data': f'{p}', 'color': '#e74c3c', 'parent': 'gen_primes', 'position': 'left', 'id': 'prime_p'})
    steps.append({'action': '生成的素数 q', 'data': f'{q}', 'color': '#e74c3c', 'parent': 'gen_primes', 'position': 'right', 'id': 'prime_q'})

    # 2. 计算n阶段（绿色模块，连接p和q）
    steps.append({'action': '计算 n = p * q', 'data': '计算模数', 'color': '#2ecc71', 'parents': ['prime_p', 'prime_q'], 'id': 'calc_n'})
    steps.append({'action': '计算结果 n', 'data': f'{n}', 'color': '#f1c40f', 'parent': 'calc_n', 'id': 'result_n'})

    # 3. 欧拉函数阶段（绿色模块）
    steps.append({'action': '计算欧拉函数 φ(n)', 'data': '(p-1)*(q-1)', 'color': '#2ecc71', 'parent': 'result_n', 'id': 'calc_phi'})
    steps.append({'action': '计算结果 φ(n)', 'data': f'{phi_n}', 'color': '#f1c40f', 'parent': 'calc_phi', 'id': 'result_phi'})

    # 4. 公钥生成阶段（绿色模块）
    steps.append({'action': '选择公钥指数 e', 'data': '与φ(n)互质', 'color': '#2ecc71', 'parent': 'result_phi', 'id': 'choose_e'})
    steps.append({'action': '选择的公钥指数 e', 'data': f'{e}', 'color': '#e74c3c', 'parent': 'choose_e', 'id': 'result_e'})

    # 5. 私钥生成阶段（绿色模块） 
    steps.append({'action': '计算私钥 d', 'data': 'e⁻¹ mod φ(n)', 'color': '#2ecc71', 'parent': 'result_e', 'id': 'calc_d'})
    steps.append({'action': '计算结果 d', 'data': f'{d}', 'color': '#f1c40f', 'parent': 'calc_d', 'id': 'result_d'})

    # 确保以下步骤的 parent 字段正确指向 result_d
    steps.append({
        'action': '导出公钥', 
        'data': f'(e,n)=({e},{n})', 
        'color': '#3498db', 
        'parent': 'result_d',  # 必须指向计算d结果的模块ID
        'position': 'left', 
        'id': 'pub_key'
    })

    steps.append({
        'action': '导出私钥', 
        'data': f'(d,n)=({d},{n})', 
        'color': '#3498db', 
        'parent': 'result_d',  # 必须指向计算d结果的模块ID
        'position': 'right', 
        'id': 'priv_key'
    })
    # 7. 加密阶段（红色父模块）
    steps.append({'action': '准备加密数据', 'data': f'原始数据: {data}', 'color': '#e74c3c', 'parent': 'pub_key', 'id': 'prepare_encrypt'})

    # Encrypt the data
    encrypted_blocks = []
    if data_int >= n:
        # Split data into blocks if it's too large
        steps.append({'action': '数据分块处理', 'data': f'分块大小: {block_size}字节', 'color': '#2ecc71', 'parent': 'prepare_encrypt', 'id': 'split_data'})
        
        for i in range(0, len(data_bytes), block_size):
            block = data_bytes[i:i+block_size]
            block_int = int.from_bytes(block, byteorder='big')
            encrypted_block = pow(block_int, e, n)
            encrypted_blocks.append(str(encrypted_block))
            
            steps.append({
                'action': f'加密块 {i//block_size+1}', 
                'data': f'使用公钥加密\n{block.decode(errors="replace")}', 
                'color': '#2ecc71',
                'parent': 'split_data',
                'id': f'encrypt_block_{i}'
            })
            steps.append({
                'action': f'块 {i//block_size+1}结果', 
                'data': f'密文: {encrypted_block}',
                'color': '#3498db',
                'parent': f'encrypt_block_{i}'
            })
    else:
        encrypted_data = pow(data_int, e, n)
        steps.append({
            'action': '加密计算', 
            'data': f'计算: {data_int}^e mod n',
            'color': '#2ecc71',
            'parent': 'prepare_encrypt',
            'id': 'encrypt_calc'
        })
        steps.append({
            'action': '加密结果', 
            'data': f'密文: {encrypted_data}',
            'color': '#3498db',
            'parent': 'encrypt_calc',
            'id': 'encrypt_result'
        })
        encrypted_blocks = [str(encrypted_data)]

    # 8. 解密阶段（蓝色父模块）
    steps.append({'action': '准备解密数据', 'data': '使用私钥解密', 'color': '#3498db', 'parent': 'encrypt_result' if 'encrypt_result' in [s.get('id') for s in steps] else f'encrypt_block_{len(data_bytes)-block_size}', 'id': 'prepare_decrypt'})

    for i, encrypted_block in enumerate(encrypted_blocks):
        encrypted_int = int(encrypted_block)
        decrypted_int = pow(encrypted_int, d, n)
        decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, byteorder='big')
        
        steps.append({
            'action': f'解密块 {i+1}', 
            'data': f'计算: {encrypted_int}^d mod n',
            'color': '#2ecc71',
            'parent': 'prepare_decrypt',
            'id': f'decrypt_block_{i}'
        })
        steps.append({
            'action': f'块 {i+1}结果', 
            'data': f'明文: "{decrypted_bytes.decode(errors="replace")}"',
            'color': '#3498db',
            'parent': f'decrypt_block_{i}'
        })

    return steps