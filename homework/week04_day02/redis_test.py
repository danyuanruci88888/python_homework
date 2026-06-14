import redis


def main():
    # 连接 Redis
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    # 1. 写入 key，设置 30 秒过期
    r.set('hello', 'world', ex=30)
    print("已写入 key: hello = world，过期时间 30 秒")

    # 2. 读取并打印
    value = r.get('hello')
    print(f"读取到的值: {value}")

    # 3. 删除 key
    r.delete('hello')
    print("key 已删除")


if __name__ == "__main__":
    main()
