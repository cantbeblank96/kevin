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

- v 1.2.1（2023-07-25）【bug fix】【new feature】
  - nested_dict_list
    - fix bug in backend ":skip:simple" registered in SERIALIZER_BACKEND，修复了没有拒绝具有结构复杂的元素的 tuple 的问题。【bug fix】
    - fix bug in write()，补充了参数 settings 缺少的默认值。【bug fix】
  - data_flow.file【new feature】
    - add new module markdown，包括 generate_link()、generate_list()、generate_table() 等方法，用于创建 markdown 格式的链接、多级列表、表格。
