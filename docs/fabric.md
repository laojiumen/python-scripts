# python fabric 运维例子

## 直接使用
```python
fab -H vagrant@192.168.33.100 -- echo 'hello world'
```
> 并行运行加 -P

## 启动

```python
# 查看task
fab -f test_function.py -l

# 运行task
fab -f test_function.py test_local()
```

## 功能包含

1. 本地操作
2. 上传下载
3. 远程操作
4. 远程sudo操作
5. 当作库集成使用

## PS

例子中的自己的vagrant服务器