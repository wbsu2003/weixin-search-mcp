FROM python:3.12-slim

WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

# 复制应用代码
COPY main.py .
COPY index.html .
COPY img/ ./img/

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 
