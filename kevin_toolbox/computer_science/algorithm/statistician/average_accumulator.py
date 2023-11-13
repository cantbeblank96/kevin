from kevin_toolbox.computer_science.algorithm.statistician import Accumulator_Base


class Average_Accumulator(Accumulator_Base):
    """
        用于计算平均值的累积器
    """

    def __init__(self, **kwargs):
        """
            参数：
                data_format:            指定数据格式
                like:                   指定数据格式
                    指定输入数据的格式，有三种方式：
                        1. 显式指定数据的形状和所在设备等。
                            data_format:        <dict of paras>
                                    其中需要包含以下参数：
                                        type_:              <str>
                                                                "numpy":        np.ndarray
                                                                "torch":        torch.tensor
                                        shape:              <list of integers>
                                        device:             <torch.device>
                                        dtype:              <torch.dtype>
                        2. 根据输入的数据，来推断出形状、设备等。
                            like:               <torch.tensor / np.ndarray / int / float>
                        3. 均不指定 data_format 和 like，此时将等到第一次调用 add()/add_sequence() 时再根据输入来自动推断。
                        以上三种方式，默认选用最后一种。
                        如果三种方式同时被指定，则优先级与对应方式在上面的排名相同。
        """
        super(Average_Accumulator, self).__init__(**kwargs)

    def add_sequence(self, var_ls, **kwargs):
        for var in var_ls:
            self.add(var)

    def add(self, var, **kwargs):
        """
            添加单个数据

            参数:
                var:                数据
        """
        if self.var is None:
            self.var = self._init_var(like=var)
        # 累积
        self.var += var
        self.state["total_nums"] += 1

    def get(self, **kwargs):
        """
            获取当前累加的平均值
                当未有累积时，返回 None
        """
        if len(self) == 0:
            return None
        return self.var / len(self)


if __name__ == '__main__':
    import torch

    seq = list(torch.tensor(range(1, 10)))
    avg = Average_Accumulator()
    for i, v in enumerate(seq):
        avg.add(var=v)
        print(i, v, avg.get())
