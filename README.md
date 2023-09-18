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

- v 1.2.7 （2023-09-18）【bug fix】
  - nested_dict_list
    - 【bug fix】fix bug in set_value()，修复了无法强制设置以@开头的name的问题
    - 【bug fix】fix bug in serializer.read()，修复了在不进行解压时仍然构造temp_dir的问题
    - 【bug fix】fix bug in copy_()，修复了无法复制带有 grad_func 的tensor的问题。
      - 添加了测试用例。
      - 注意：本修复只解决节点是tensor的情况，对于节点是含有不能deepcopy的tensor的变量，比如由带有 grad_func 的tensor组成的tuple等的结构，copy_()函数仍然会报错。考虑到这种情况非常复杂，因此不作解决，只能尽量避免，或者出错时专门排查。
    - 改造模块加载方式，支持通过x.y间接加载子模块，比如 nested_dict_list.serializer 等
    - 【new feature】modify copy_()，增加了 b_keep_internal_references 参数用于控制是否保留内部的引用关系。
      - 当使用 b_keep_internal_references=True 时，将保留 ndl 中结构与结构之间或者节点与节点之间的引用关系。默认为 True（当b_deepcopy=True时与 copy.deepcopy 的行为一致）。
      - 什么是引用关系？
        - 比如我们将某个字典 A 多次加入到某个 list 中，那么这个 list 中的这些字典实际上都指向内存上同一个字典，因此对其中某个字典的修改将影响到其他 list 中的其他元素。这种内存上指向同一个位置的关系就是引用。
      - 与 b_deepcopy 的配合：
        - 当 b_deepcopy=False 进行浅拷贝时，参数 b_keep_internal_references 仅作用于结构，反之则同时作用于结构和节点。
      - 添加了测试用例。
  - nested_dict_list.serializer
    - modify write()，只对输入进行浅拷贝，减少对内存的消耗。
