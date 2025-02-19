-- 算法表
CREATE TABLE algorithms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 评估系统表
CREATE TABLE evaluation_systems (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    description TEXT,
    evaluation_result TEXT,
    created_by INT NOT NULL,  -- 关联用户管理数据库的 users.id
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 评估项表
CREATE TABLE evaluation_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 算法-系统关联表
CREATE TABLE algorithm_system (
    id INT AUTO_INCREMENT PRIMARY KEY,
    evaluation_system_id INT NOT NULL,
    algorithm_id INT NOT NULL,
    evaluation_item_id INT NOT NULL,
    risk_level ENUM('高', '中', '低') NOT NULL,
    evaluation_result TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (evaluation_system_id) REFERENCES evaluation_systems(id) ON DELETE CASCADE,
    FOREIGN KEY (algorithm_id) REFERENCES algorithms(id) ON DELETE CASCADE,
    FOREIGN KEY (evaluation_item_id) REFERENCES evaluation_items(id) ON DELETE CASCADE
);