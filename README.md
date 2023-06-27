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

- v 1.1.2（）【bug fix】

  - computer_science.algorithm.for_nested_dict_list
    - 改进 get_value_by_name()
      - 新增了参数 b_pop 用于支持取值的同时将该值从 var 中移除
      - 新增了参数 default 用于设置取值失败时是报错还是返回默认值
  - computer_science.algorithm.registration
    - Registry
      - 【bug fix】修复了问题：当已有实例的 uid 为正整数 n，同时 cls.__counter 为 n 时，不指定 uid 再创建实例将错误地返回 uid=n 的已有实例而不是新建一个。
      - 将 self.pop() 函数的功能合并到 self.get(... ,b_pop=...) 中
  - computer_science.algorithm.scheduler
    - 改进 Trigger
      - 使用 Registry 来管理触发目标
      - 新增 self.unbind() 函数来解除绑定
      - 在 update_by_state() 中新增了 target_names 参数来决定调用哪些目标
      - 新增 Trigger 的状态管理相关函数
        - self.clear_state_dict(): 清除 Trigger 中保存的状态
        - self.load_state_dict(): 加载
        - self.state_dict(): 获取
        - load_state_dict 和 state_dict 的接口名称是为了和 pytorch 中模型、优化器的状态加载、获取保持一致。

  

