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

- v 1.1.0（2023-06-21）【bug fix】
  - computer_science.algorithm.for_dict
    - fix bug in deep_update()，修复了无法更新stem中值为None的部分的问题。
    - 添加了单元测试

  - computer_science.algorithm.for_nested_dict_list

    - 新增模块 name_handler 用于处理名字的解释、构造等

      - parse_name() 解释名字 name 得到：root_node、取值方式 method_ls 、取值时使用的键 node_ls
      - build_name()  根据root_node、取值方式 method_ls 、取值时使用的键 node_ls，来构造名字 name
      - escape_node() 对键进行转义/反转义
      - 添加了单元测试
      - 添加了说明文档
      - 支持了转义字符。对于含有特殊字符 :|@ 的 node，可以对 node 中的这些特殊字符使用 \ 进行转义，避免将这些字符解释为取值方式。

    - 结合 name_handler 修改了 get_value_by_name()、get_nodes()、traverse()、set_value_by_name()

    - 改进了 set_value_by_name()，支持强制创建列表

    - 新增模块 value_parser 用于处理带有引用的值

      - 什么是引用？

        - 对于值，若为字符串类型，且其中含有 `"...<flag>{ref_name}..."` 的形式，则表示解释该值时需要将 `<flag>{ref_name}` 这部分替换为 var 中 ref_name 对应的值

      - parse_references() 解释 var 中包含引用的值

        - ```
          比如对于：
              name=":z", value="<v>{:x}+<v>{:y}"
          的节点，将会返回：
              {":z": {"expression":"p_0+p_1" , "paras": {"p_0":":x","p_1":":y"}}, ...}
          利用 "expression" 和 "paras" 中的内容，将可以很方便得使用 eval() 和 get_value_by_name() 完成对节点值的计算。
          但是由于节点之间可能存在相互引用，因此一般需要通过 cal_relation_between_references() 来确定计算顺序。
          ```

      - cal_relation_between_references() 计算具有引用的节点之间的关系

        - ```
          函数返回值：
              node_s, b_is_DAG, order
          
              node_s:             <dict> 在输入的 node_s 的基础上为每个节点补充 upstream_node 和 downstream_node 字段
                                      其中：
                                          upstream_node 中保存该节点所依赖的上游节点，意味着要等这些上游节点计算完毕后才能计算该节点
                                          downstream_node 中保存对该节点有依赖的下游节点。
              b_is_DAG:           <boolean> 节点关系是否满足有向无环图 DAG
              order:              <list of name> 节点在 DAG 中的顺序
          ```

      - eval_references() 将 var 中的具有引用的值替换为计算结果

  - data_flow.file.kevin_notation

    - 修改 write_contents() 支持通过 b_single_line 参数来明确指定是使用单行or多行模式进行写入
    - 修改 `__setattr__()` 支持通过前缀 "row_ls" or "column_dict" 来指定写入内容的组织形式，支持通过添加后缀 "single_line" or "multi_line" 来明确指定按照单行or多行模式进行写入
      - 例如 self.row_ls_single_line = value 等效于 self.write_contents(row_ls=value, b_single_line=True)

  - computer_science.algorithm.registration

    - 改进 Registry 类
      - 在 add() 中也增加了b_execute_now 来控制延时导入
      - 在 collect_from_paths() 中新增了 path_ls_to_exclude 参数用于指定需要排除的目录
      - 改进了 collect_from_paths() 中路径的搜索方式，改为从深到浅导入，可以避免继承引起的 TypeError: super(type, obj) 类型错误

  - computer_science.algorithm.scheduler

    - 修改 Trigger 类中的 bind() 方法，支持直接读取实例的 update_by_state() 函数进行绑定。同时也新增了 bind_func() 和 bind_obj() 用于在明确待绑定对象类型时使用。

