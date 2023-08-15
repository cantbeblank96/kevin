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

- v 1.2.5 （2023-08-15）【new feature】【bug fix】
  - nested_dict_list
    - 【bug fix】fix write()，修复了 strictness_level 参数不支持字符串输入的问题。
  - computer_science.algorithm
    - 【new feature】新增了 parallel_and_concurrent 模块用于处理与并行、并发有关的问题。其中包含了：
      - multi_thread_execute(<list/generator/iterator of Executor>, ...) 函数，用于多线程执行给定的执行器序列，该函数使用线程池来管理，可以避免阻塞。
      - 已经添加了对应的测试用例。
  - computer_science.algorithm.for_seq
    - 【new feature】增加了 chunk_generator() 函数，用于构建返回指定批大小的生成器。
    - 已经添加了对应的测试用例。
