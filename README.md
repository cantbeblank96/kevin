# kevin_toolbox

一个通用的工具代码包集合



环境要求

```shell
numpy>=1.19
pytorch>=1.2
```

安装方法：

```shell
pip install kevin-toolbox  --no-dependencies
```



[项目地址 Repo](https://github.com/cantbeblank96/kevin_toolbox)

[使用指南 User_Guide](./notes/User_Guide.md)

[免责声明 Disclaimer](./notes/Disclaimer.md)

[版本更新记录](./notes/Release_Record.md)：

- v 1.0.12（2023-06-13）
  - computer_science.algorithm.registration
    - 添加了 Registry 注册器类，它具有以下功能：
      - 管理成员，包括添加 add()、获取 get() pop() 成员等
      - 支持通过装饰器 register() 来添加成员
      - 支持通过 collect_from() 搜索指定的路径，当该路径下的模块被 register() 装饰器包裹时，将自动导入（用于解决python中的模块是惰性的问题）

  - fix bug in kevin_toolbox/developing/design_pattern/singleton/singleton_for_uid.py
    - 即使`__new__`函数返回一个已经存在的实例，`__init__`还是会被调用的，所以要特别注意`__init__`中对变量的赋值，避免对已经存在的实例中的变量重新进行初始化




