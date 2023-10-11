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

- v 1.2.8 （）【new feature】
  - data_flow.file.markdown
    - 【new feature】modify generate_table()
      - 支持两种输入模式（新增了第二种模式）
        1. 简易模式：
                    ` content_s = {<title>: <list of value>, ...}`
                     此时键作为标题，值作为标题下的一系列值。
                     由于字典的无序性，此时标题的顺序是不能保证的，若要额外指定顺序，请使用下面的 完整模式。
        2. 完整模式:
                    `content_s = {<index>: {"title": <title>,"values":<list of value>}, ...}`
                    此时将取第 `<index>` 个 "title" 的值来作为第 `<index>` 个标题的值。values 同理。
                    该模式允许缺省某些 `<index>`，此时这些 `<index>` 对应的行/列将全部置空。
      - 部分兼容旧版的输入（对应于上面的简易模式），但是不再支持通过 ordered_keys 来指定简易模式下的标题顺序。若要实现类似功能，请直接使用 collections.OrderedDict 作为输入。
      - 支持通过 chunk_nums 和 chunk_size 参数实现表格的分割并列显示。
      - 支持通过 b_allow_misaligned_values 参数来允许不对齐的 values。
      - 支持通过 f_gen_order_of_values 来指定 values 的排序顺序。
      - 添加了对应的测试用例。
  - patches.for_numpy.linalg
    - 【new feature】modify softmax()
      - 新增了 temperature 参数，该参数起到对输入中的相对小/大值的抑制/增强作用。
      - 新增了 b_use_log_over_x 参数，用于简化 softmax(log(x)) 计算。
      - 添加了对应的测试用例。
